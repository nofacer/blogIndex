import os

DEST_DIR = os.environ.get('dest_dir')
GIT_USER = os.environ.get('git_user')
REPO_NAME = os.environ.get('repo_name')
IS_PUBLIC = (os.environ.get('is_public') == str(True))
OUTPUT_PATH = os.environ.get('output_path', './')
