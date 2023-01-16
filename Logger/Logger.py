import smtplib

from Constants import EmailConstants
from Logger.ILogger import ILogger


class Logger(ILogger):
    @staticmethod
    def log(inactive_repositories):
        for repository in inactive_repositories:
            repo_last_updated = repository['last_updated']
            print(f'{repository["name"]} was last updated on {repo_last_updated}')

            last_commit_author = repository['last_updated']['user']['email']
            message = EmailConstants.TEMPLATE.format(from_email='noreply@example.com', to_email=last_commit_author,
                                                     repository_name=repository['name'],
                                                     workspace_name=repository['workspace']['name'])
            with smtplib.SMTP(EmailConstants.DOMAIN_SERVER, EmailConstants.PORT) as server:
                server.starttls()
                server.login(EmailConstants.USERNAME, EmailConstants.PASSWORD)
                server.sendmail('noreply@example.com', last_commit_author, message)
