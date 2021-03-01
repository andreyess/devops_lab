import requests


def git_request(state, owner="alenaPy", repo="devops_lab", per_page=100):
    if not state:
        url = f"https://api.github.com/repos/{owner}/{repo}/pulls?state=all&per_page={per_page}"
    elif state in ('open', 'closed'):
        url = f"https://api.github.com/repos/{owner}/{repo}/pulls?state={state}&per_page={per_page}"
    else:
        url = "https://api.github.com/search/issues?" \
            f"q=is:pr%20label:\"{state}\"%20repo:{owner}/{repo}&per_page={per_page}"
    pull_requests = requests.get(url).json()
    return pull_requests if state in (None, 'open', 'closed') else pull_requests['items']


def get_pulls(state):
    git_response = git_request(state)
    return list(
        map(
            lambda request:
            {
                'link': request['html_url'],
                'title': request['title'],
                'num': request['number']
            },
            git_response
        )
    )
