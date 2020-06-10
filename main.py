from Downloader import Downloader

if __name__ == '__main__':
    downloader = Downloader()
    downloader.clone_repo('nofacer', 'blog.articles', 'download', False)
