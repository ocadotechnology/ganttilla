from requests import get
from descriptor import create_descriptor


def query_gitlab(url, projectid, token, pem=None):
    url = f'{url}/api/v4/projects/{projectid}/milestones'
    querystring = {"state": "active"}
    headers = {'Private-Token': token}
    if pem is None:
        response = get(url, headers=headers, params=querystring,
                       verify=False)
    else:
        response = get(url, headers=headers, params=querystring,
                       verify=pem)
    return parse_gitlab(response.json())


def parse_gitlab(response):
    milestones = []
    for entry in response:
        create_descriptor(entry['start_date'],
                          entry['due_date'],
                          entry['description'],
                          entry['title'],
                          entry['web_url'],
                          milestones)
    return milestones
