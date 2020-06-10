from git import Repo
import os
import shutil


def get_token(file_path='token.txt'):
    with open(file_path, "r") as f:
        token = f.read()
    return token


def recreate_folder(dest_dir):
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.mkdir(dest_dir)


def clone_repo(git_url: str, dest_dir: str):
    recreate_folder(dest_dir)
    Repo.clone_from(git_url, dest_dir)


if __name__ == '__main__':
    clone_repo('https://{}:x-oauth-basic@github.com/nofacer/blog.articles'.format(get_token()), './download')