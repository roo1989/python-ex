import feedparser


def get_url():
    url = str(input('RSS URL: '))

    while not len(url) > 0:
        print('Invalid URL: Length has to be greater than 0')
        url = str(input('RSS URL: '))

    return url


def read(url):
    rss = feedparser.parse(url)

    return rss


def read_feed(url):
    rss = read(url)

    print(f'Feed Description: {rss.feed.description}')
    print(f'Feed Link: {rss.feed.link}')

    return


def read_feed_entries(url):
    rss = read(url)

    for entry in rss['entries']:
        print(f'Entry title: {entry.title}')
        print(f'Entry description: {entry.description}')
        print(f'Entry title: {entry.link}')

        return


if __name__ == '__main__':
    url = get_url()
    read_feed(url)
    read_feed_entries(url)
