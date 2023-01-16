from InactiveRepositoriesScanner.InactiveRepositoriesScanner import InactiveRepositoriesScanner
from Logger.Logger import Logger
from RepositoriesRetriever.RepositoriesRetriever import RepositoriesRetriever


def main():
    repository_retriever = RepositoriesRetriever()
    inactive_repository_scanner = InactiveRepositoriesScanner()
    logger = Logger()

    repositories = repository_retriever.retrieve()
    inactive_repos = inactive_repository_scanner.scan(repositories)
    logger.log(inactive_repos)


if __name__ == '__main__':
    main()
