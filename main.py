from SqliteIndexer import *
from Downloader import Downloader
from Parser import parse
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['get'])
def hello():
    return {'message': 'hello world'}, 200


@app.route('/index', methods=['POST'])
def index_articles():
    index()
    return {'message': 'index articles successfully'}, 200


def index():
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
