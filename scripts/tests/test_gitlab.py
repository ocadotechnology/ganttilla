from sys import path
from os.path import dirname
from os.path import abspath
import requests_mock
here = dirname(dirname(abspath(__file__)))
path.insert(0, here)


from gitlab import parse_gitlab, query_gitlab

start_date = 1234
due_date = 1234
web_url = "https://gitlab.com"
payload = [{"start_date": start_date,
            "due_date": due_date,
            "description": "description",
            "title": "title",
            "web_url": web_url}]


def test_gitlab_parsing():
    milestones = parse_gitlab(payload)[0]
    assert milestones["start_date"] == start_date
    assert milestones["due_date"] == due_date
    assert milestones["link"] == web_url


def test_gitlab_query():
    with requests_mock.Mocker() as m:
        m.get('https://gitlab.com/api/v4/projects/1/milestones', json=payload)
        result = query_gitlab("https://gitlab.com", 1, "")[0]
        assert result["start_date"] == start_date
