#!/bin/sh

echo "Please enter the GitHub username (e.g. ocadotechnology)"

read username

echo "Please enter the GitHub repository (e.g. ganttilla)"

read repository

echo "Please enter the GitHub token"

read token

echo "Please enter the Ganttilla output file name"

read fileName

export GITHUB_USERNAME=$username
export GITHUB_REPOSITORY=$repository
export GITHUB_TOKEN=$token
export GANTTILLA_OUTPUT_FILENAME="/ganttilla/generated-descriptors/$fileName"

mkdir -p /ganttilla/generated-descriptors

python3 /ganttilla/scripts/run.py github
