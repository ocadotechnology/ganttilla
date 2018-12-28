#!/bin/sh

echo "Please enter the GitLab url (e.g. https://gitlab.com)"

read url

echo "Please enter the GitLab project id"

read projectId

echo "Please enter the GitLab token"

read token

echo "Please enter the Ganttilla output file name"

read fileName

export GITLAB_URL=$url
export GITLAB_PROJECT_ID=$projectId
export GITLAB_TOKEN=$token
export GANTTILLA_OUTPUT_FILENAME="/ganttilla/generated-descriptors/$fileName"

mkdir -p /ganttilla/generated-descriptors

python3 /ganttilla/scripts/run.py gitlab
