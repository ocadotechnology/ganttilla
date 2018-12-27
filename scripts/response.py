def verify_response(response):
    if response.status_code == 404:
        exit(f"Request to {response.url} has failed. \
        Please check the environment variables you've used.")
    elif len(response.json()) == 0:
        exit("There are no milestones to be visualised here.")
    elif response.status_code == 200:
        pass
