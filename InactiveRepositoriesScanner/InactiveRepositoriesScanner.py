import datetime
from itertools import repeat

import pytz
from Constants import ApiConstants
from InactiveRepositoriesScanner.IInactiveRepositoriesScanner import IInactiveRepositoriesScanner


class InactiveRepositoriesScanner(IInactiveRepositoriesScanner):
    inactive_repositories = []

    def scan(self, retrieved_repositories):
        for repository in retrieved_repositories:
            is_valid = self.validate_date(repository)
            if is_valid:
                self.inactive_repositories.append(repository)
                return self.inactive_repositories

    @staticmethod
    def validate_date(repository_json):
        delta_time = (datetime.datetime.now() - datetime.timedelta(days=365))
        delta_time = delta_time.replace(tzinfo=pytz.utc)
        last_updated = datetime.datetime.strptime(repository_json['updated_on'], '%Y-%m-%dT%H:%M:%S.%f%z')
        last_updated = last_updated.replace(tzinfo=pytz.utc)
        if last_updated < delta_time:
            return True
        return False
