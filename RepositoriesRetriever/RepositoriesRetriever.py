import requests
from Constants import ApiConstants
from RepositoriesRetriever.IRepositoriesRetriever import IRepositoriesRetriever


class RepositoriesRetriever(IRepositoriesRetriever):

    def retrieve(self):
        response = requests.get(url=ApiConstants.WORKSPACE_URL)
        return response.json()['values']
