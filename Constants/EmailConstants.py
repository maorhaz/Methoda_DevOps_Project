DOMAIN_SERVER = 'smtp.example.com'
PORT = 587
USERNAME = 'username'
PASSWORD = 'password'
TEMPLATE = '''From: {from_email}
    To: {to_email}
    Subject: Inactivity on repository {repository_name}

    Hello,

    We have noticed that your repository {repository_name} in the {workspace_name} workspace has not been updated in more than a year.
    We just wanted to check if you are still maintaining this repository or if it can be archived.

    Please let us know.

    Best,
    The team
    '''