from abc import ABC, abstractmethod


class IRepositoriesRetriever(ABC):
    @abstractmethod
    def retrieve(self):
        pass
