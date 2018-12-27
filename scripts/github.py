from requests import get
from descriptor import create_descriptor
from response import verify_response


def query_github(owner, repo, token):
    url = f'https://api.github.com/repos/{owner}/{repo}/milestones'
    headers = {"Authorization": f"token {token}"}
    response = get(url, headers=headers)
    verify_response(response)
    return parse_github(response.json())


def parse_github(response):
    milestones = []
    for entry in response:
        create_descriptor(entry['created_at'],
                          entry['due_on'],
                          entry['description'],
                          entry['title'],
                          entry['html_url'],
                          milestones)
    return milestones
