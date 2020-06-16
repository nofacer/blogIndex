from Downloader import Downloader
from Parser import parse

if __name__ == '__main__':
    DEST_DIR = 'download'
    GIT_USER = 'nofacer'
    REPO_NAME = 'blog.articles'
    IS_PUBLIC = False

    downloader = Downloader()

    downloader.clone_repo(GIT_USER, REPO_NAME, DEST_DIR, IS_PUBLIC)
    result = parse(DEST_DIR)
    print(result)
