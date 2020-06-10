from git import Repo
import os
import shutil


def get_token(file_path='token.txt') -> str:
    with open(file_path, "r") as f:
        token = f.read()
    return token


def recreate_folder(target_dir: str) -> None:
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
    os.mkdir(target_dir)


def clone_repo(git_url: str, target_dir: str) -> None:
    recreate_folder(target_dir)
    Repo.clone_from(git_url, target_dir)


if __name__ == '__main__':
    clone_repo('https://{}:x-oauth-basic@github.com/nofacer/blog.articles'.format(get_token()), './download')
