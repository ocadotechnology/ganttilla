from json import dumps


def create_descriptor(start_date, due_date, description, title,
                      web_url, milestones):
    milestones.append({'start_date': start_date,
                       'end_date': due_date,
                       'description': description,
                       'title': title,
                       'link': web_url})


def write_descriptor(result, output_file):
    with open(output_file, 'w') as output:
        output.write(dumps(result))
