import requests
from Constants import ApiConstants
from RepositoriesRetriever.IRepositoriesRetriever import IRepositoriesRetriever


class RepositoriesRetriever(IRepositoriesRetriever):
    @staticmethod
    def retrieve():
        response = requests.get(url=ApiConstants.WORKSPACE_URL,
                                headers={'Authorization': f'Bearer {ApiConstants.ACCESS_TOKEN}'})

        return response  # todo parse result
