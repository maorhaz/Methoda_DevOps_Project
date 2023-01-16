from abc import ABC, abstractmethod


class IInactiveRepositoriesScanner(ABC):
    @abstractmethod
    def scan(self, retrieved_repositories):
        pass
