from git import Repo
import os
import shutil


def get_token(file_path='token.txt'):
    with open(file_path, "r") as f:
        token = f.read()
    return token


if __name__ == '__main__':
    git_url = 'https://{}:x-oauth-basic@github.com/nofacer/blog.articles'.format(get_token())
    dest_dir = './download'

    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.mkdir(dest_dir)

    Repo.clone_from(git_url, dest_dir)
