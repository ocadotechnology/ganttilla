from argparse import ArgumentParser
from gitlab import query_gitlab
from github import query_github
from jira import query_jira
from enum import Enum
from os import environ, getenv
from descriptor import write_descriptor


class Source(Enum):
    gitlab = 'gitlab'
    github = 'github'
    jira = 'jira'

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
    except KeyError:
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
    except KeyError:
        exit("Environment variables GITHUB_USERNAME, GITHUB_REPOSITORY, \
        GITHUB_TOKEN and GANTTILLA_OUTPUT_FILENAME need to be set")
    result = query_github(github_user,
                          github_repo,
                          github_token)
    write_descriptor(result, ganttilla_output_filename)
elif str(opts.source) == "jira":
    try:
        jira_project = environ['JIRA_PROJECT']
        jira_url = environ['JIRA_URL']
        jira_username = environ['JIRA_USERNAME']
        jira_token = environ['JIRA_TOKEN']
        jira_start_date_field = environ['JIRA_START_DATE_FIELD']
        jira_end_date_field = environ['JIRA_END_DATE_FIELD']
        ganttilla_output_filename = environ["GANTTILLA_OUTPUT_FILENAME"]
    except KeyError:
        exit("Environment variables JIRA_PROJECT, JIRA_URL, \
        JIRA_USERNAME, JIRA_TOKEN, JIRA_START_DATE_FIELD, JIRA_END_DATE_FIELD \
        and GANTTILLA_OUTPUT_FILENAME need to be set")
    jira_custom_jql = getenv("JIRA_CUSTOM_JQL")

    result = query_jira(jira_url,
                        jira_username,
                        jira_token,
                        jira_project,
                        jira_start_date_field,
                        jira_end_date_field,
                        jira_custom_jql)
    write_descriptor(result, ganttilla_output_filename)
