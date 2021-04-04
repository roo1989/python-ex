import sys

import requests
from bs4 import BeautifulSoup


class Article:
    def __init__(self, url):
        self.url = url

    @property
    def response(self):
        response = requests.get(self.url).text

        if not response.status_code.startswith(int(2)):
            print(f'Response returned with status code {response.status_code}')
            raise

    @property
    def title(self):
        soup = BeautifulSoup(self.response, 'lxml')
        title = soup.find('title')
        if not title:
            return 'Title not a valid element: Not found'
            raise

        return title.text


if __name__ == '__main__':
    url_article = sys.argv[0]

    print('Title': Article.title)