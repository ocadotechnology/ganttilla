from sys import path
from os.path import dirname
from os.path import abspath
import requests_mock
here = dirname(dirname(abspath(__file__)))
path.insert(0, here)


from github import parse_github, query_github

created_at = 1234
due_on = 1234
html_url = "https://api.github.com/repos/user/repo/milestones/1"
payload = [{"created_at": created_at,
            "due_on": due_on,
            "description": "description",
            "title": "title",
            "html_url": html_url}]


def test_github_parsing():
    milestones = parse_github(payload)[0]
    print(milestones)
    assert milestones["start_date"] == created_at
    assert milestones["due_date"] == due_on
    assert milestones["link"] == html_url


def test_github_query():
    with requests_mock.Mocker() as m:
        m.get('https://api.github.com/repos/user/repo/milestones',
              json=payload)
        result = query_github("user", "repo", "")[0]
        assert result["start_date"] == created_at
