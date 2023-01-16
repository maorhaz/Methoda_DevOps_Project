import datetime
import json

from Constants import ApiConstants
from InactiveRepositoriesScanner.IInactiveRepositoriesScanner import IInactiveRepositoriesScanner


class InactiveRepositoriesScanner(IInactiveRepositoriesScanner):
    inactive_repositories = []

    def scan(self, retrieved_repositories):
        for repository in retrieved_repositories:
            repository_url = ApiConstants.WORKSPACE_URL + repository['name']  # fixme ??
            repository_response = requests.get(
                repository_url.format(workspace_name=repository['workspace']['name'],
                                      repository_name=repository['name']),
                auth=('username', ApiConstants.ACCESS_TOKEN))
            repository_json = json.loads(repository_response.text)

            is_valid = self.validate_date(repository_json)
            if is_valid:
                self.inactive_repositories.append(repository_json)

    @staticmethod
    def validate_date(repository_json):
        last_updated = datetime.datetime.strptime(repository_json['updated_on'], '%Y-%m-%dT%H:%M:%S.%f%z')
        if datetime.datetime.now() - last_updated > datetime.timedelta(days=365):
            return True
        return False
