from requests import post
from requests.auth import HTTPBasicAuth
from descriptor import create_descriptor


def query_jira(url, user, token, project, jira_start_date_field,
               jira_end_date_field, jira_custom_jql):
    search_url = f'{url}/rest/api/2/search'
    if jira_custom_jql:
        querystring = {'jql': jira_custom_jql}
    else:
        querystring = {'jql': f'project = {project}'}
    headers = {'Content-Type': 'application/json', 'Accept': '*/*'}
    response = post(search_url,
                    auth=HTTPBasicAuth(user, token),
                    headers=headers,
                    json=querystring,
                    verify=False)
    print(response.text)
    return parse_jira(url,
                      response.json(),
                      jira_start_date_field,
                      jira_end_date_field)


def parse_jira(url, response, start_date_field, end_date_field):
    milestones = []
    issues = response['issues']
    for entry in issues:
        create_descriptor(entry['fields'].get(start_date_field, None),
                          entry['fields'].get(end_date_field, None),
                          entry['fields']['description'],
                          entry['fields']['summary'],
                          url + "/browse/" + entry['key'],
                          milestones)
    return milestones
