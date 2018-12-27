from argparse import ArgumentParser
from gitlab import query_gitlab
from github import query_github
from enum import Enum
from os import environ
from descriptor import write_descriptor


class Source(Enum):
    gitlab = 'gitlab'
    github = 'github'

    def __str__(self):
        return self.value


parser = ArgumentParser()
parser.add_argument('source', type=Source, choices=list(Source))

opts = parser.parse_args()

if str(opts.source) == 'gitlab':
    try:
        gitlab_url = environ["GITLAB_URL"]
        gitlab_project_id = environ["GITLAB_PROJECT_ID"]
        gitlab_token = environ["GITLAB_TOKEN"]
        ganttilla_output_filename = environ["GANTTILLA_OUTPUT_FILENAME"]
    except KeyError as e:
        exit("Environment variables GITLAB_URL, GITLAB_TOKEN, \
        GITLAB_PROJECT_ID and GANTTILLA_OUTPUT_FILENAME need to be set")
    gitlab_pem = environ.get("GITLAB_PEM")
    result = query_gitlab(gitlab_url,
                          gitlab_project_id,
                          gitlab_token,
                          gitlab_pem)
    write_descriptor(result, ganttilla_output_filename)
elif str(opts.source) == "github":
    try:
        github_user = environ['GITHUB_USERNAME']
        github_repo = environ['GITHUB_REPOSITORY']
        github_token = environ['GITHUB_TOKEN']
        ganttilla_output_filename = environ["GANTTILLA_OUTPUT_FILENAME"]
    except KeyError as e:
        exit("Environment variables GITHUB_USERNAME, GITHUB_REPOSITORY, \
        GITHUB_TOKEN and GANTTILLA_OUTPUT_FILENAME need to be set")
    result = query_github(github_user,
                          github_repo,
                          github_token)
    write_descriptor(result, ganttilla_output_filename)
