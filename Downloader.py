from git import Repo
import os
import shutil


def recreate_folder(target_dir: str) -> None:
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
    os.mkdir(target_dir)


def clone_repo(git_user_name: str, git_repo_name: str, target_dir: str, is_public=True) -> None:
    recreate_folder(target_dir)
    if is_public:
        git_url = 'https://github.com/{}/{}'.format(git_user_name, git_repo_name)
        Repo.clone_from(git_url, target_dir)
    else:
        git_token = os.environ.get('git_token')
        git_url = 'https://{}:x-oauth-basic@github.com/{}/{}'.format(git_token, git_user_name, git_repo_name)
        Repo.clone_from(git_url, target_dir)
