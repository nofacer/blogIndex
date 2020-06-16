from SqliteIndexer import *
from Downloader import Downloader
from Parser import parse

if __name__ == '__main__':
    DEST_DIR = 'download'
    GIT_USER = 'nofacer'
    REPO_NAME = 'blog.articles'
    IS_PUBLIC = False

    downloader = Downloader()
    downloader.clone_repo(GIT_USER, REPO_NAME, DEST_DIR, IS_PUBLIC)

    article_info_tuples = parse(DEST_DIR)

    create_new_database()
    for article_info_tuple in article_info_tuples:
        article_metadata = article_info_tuple[0]
        article_string = article_info_tuple[1]
        insert_data(article_metadata, article_string)
