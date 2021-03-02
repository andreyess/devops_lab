import requests


def git_request(state, owner="alenaPy", repo="devops_lab", per_page=100):
    if not state:
        url = f"https://api.github.com/repos/{owner}/{repo}/pulls?state=all&per_page={per_page}"
    elif state in ('open', 'closed'):
        url = f"https://api.github.com/repos/{owner}/{repo}/pulls?state={state}&per_page={per_page}"
    else:
        url = "https://api.github.com/search/issues?" \
            f"q=is:pr%20label:\"{state}\"%20repo:{owner}/{repo}&per_page={per_page}"

    response = requests.get(url)
    if state in (None, 'open', 'closed'):
        return (response.status_code, response.json())
    else:
        return (response.status_code, response.json()['items'])


def convert_to_list(response):
    return list(
        map(
            lambda pull_request:
            {
                'link': pull_request['html_url'],
                'title': pull_request['title'],
                'num': pull_request['number']
            },
            response
        )
    )


def get_pulls(state):
    git_response = git_request(state)
    if git_response[0] == 200:
        return convert_to_list(git_response[1])
    else:
        return []
