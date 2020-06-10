from git import Repo
from utils import recreate_folder


class Downloader:
    def __init__(self):
        self.token = None

    def get_token(self, file_path='token.txt', token_str=None) -> None:
        if token_str is not None:
            self.token = token_str
        else:
            with open(file_path, "r") as f:
                self.token = f.read()

    def clone_repo(self, git_user_name: str, git_repo_name: str, target_dir: str, is_public=True) -> None:
        recreate_folder(target_dir)
        if is_public:
            Repo.clone_from('https://github.com/{}/{}'.format(git_user_name, git_repo_name), target_dir)
        else:
            if self.token is None:
                self.get_token()
            Repo.clone_from(
                'https://{}:x-oauth-basic@github.com/{}/{}'.format(self.token, git_user_name, git_repo_name),
                target_dir)
