from unittest import TestCase
import handlers.pulls as pulls


class TestPulls(TestCase):

    def setUp(self):
        """Init"""

    def test_response_codes(self):
        self.assertEqual(pulls.git_request(None)[0], 200)
        self.assertEqual(pulls.git_request("open")[0], 200)
        self.assertEqual(pulls.git_request("closed")[0], 200)
        self.assertEqual(pulls.git_request("accepted")[0], 200)
        self.assertEqual(pulls.git_request("need work")[0], 200)

    def test_to_list_convertation(self):
        test_data = [
            {'html_url': 'http://test1.com', 'title': 'test1', 'number': 1, 'trash_field': 'blabl'},
            {'html_url': 'http://test2.com', 'title': 'test2', 'number': 2, 47: ['check']},
            {'html_url': 'http://test3.com', 'title': 'test3', 'number': 3, (10, 14): (22, '177')},
        ]

        list_data = pulls.convert_to_list(test_data)
        self.assertTrue(len(list_data) == 3)
        self.assertTrue(list_data[0]['title'] == 'test1')
        self.assertTrue(list_data[1]['link'] == 'http://test2.com')
        self.assertTrue(list_data[2]['num'] == 3)

        with self.assertRaises(KeyError):
            list_data[0]['trash_field']

    def test_whole_request(self):
        response = pulls.get_pulls(None)
        self.assertTrue(len(response) <= 100)

    def tearDown(self):
        """Finish"""
