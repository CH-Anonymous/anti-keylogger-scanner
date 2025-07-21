import os
import git
import json
from github import Github

TOKEN_FILE = os.path.expanduser("~/.autogitpush_token.json")

def save_token(username, token):
    with open(TOKEN_FILE, 'w') as f:
        json.dump({"username": username, "token": token}, f)

def load_token():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'r') as f:
            data = json.load(f)
            return data.get('username'), data.get('token')
    return None, None

def reset_token():
    if os.path.exists(TOKEN_FILE):
        os.remove(TOKEN_FILE)

def push_to_github(folder_path, username, repo_name, token):
    try:
        os.chdir(folder_path)

        if not os.path.exists(os.path.join(folder_path, ".git")):
            repo = git.Repo.init(folder_path)
        else:
            repo = git.Repo(folder_path)

        remote_url = f"https://{username}:{token}@github.com/{username}/{repo_name}.git"

        # Reset remote origin
        if 'origin' in [remote.name for remote in repo.remotes]:
            repo.delete_remote('origin')
        repo.create_remote('origin', remote_url)

        # Checkout or create main
        if "main" not in repo.heads:
            repo.git.checkout('-b', 'main')
        else:
            repo.git.checkout('main')

        # Pull latest from GitHub before pushing
        try:
            repo.remotes.origin.fetch()
            repo.git.pull('--rebase', 'origin', 'main')
        except Exception as e:
            return False, f"Failed to pull remote changes. Resolve conflicts and try again.\nDetails: {str(e)}"

        # Stage and commit changes
        if repo.is_dirty(untracked_files=True):
            repo.git.add(A=True)
            repo.index.commit("AutoGitPush Commit")

        # Push to GitHub
        repo.git.push('--set-upstream', 'origin', 'main')
        return True, "Code pushed successfully to GitHub!"
    except Exception as e:
        return False, f"Push failed: {str(e)}"

def create_github_repo(repo_name, username, token):
    try:
        g = Github(token)
        user = g.get_user()
        if repo_name not in [repo.name for repo in user.get_repos()]:
            user.create_repo(repo_name)
            return True, f"Repository '{repo_name}' created successfully."
        return False, f"Repository '{repo_name}' already exists."
    except Exception as e:
        return False, f"Failed to create repo: {str(e)}"

def delete_github_repo(repo_name, token):
    try:
        g = Github(token)
        user = g.get_user()
        for repo in user.get_repos():
            if repo.name == repo_name:
                repo.delete()
                return True
        return False
    except:
        return False

def list_github_repos(token):
    try:
        g = Github(token)
        user = g.get_user()
        return [repo.name for repo in user.get_repos()]
    except:
        return []

def update_repo_remote(folder_path, username, repo_name, token):
    try:
        repo = git.Repo(folder_path)
        remote_url = f"https://{username}:{token}@github.com/{username}/{repo_name}.git"
        if 'origin' in [remote.name for remote in repo.remotes]:
            repo.delete_remote('origin')
        repo.create_remote('origin', remote_url)
        return True, "Remote updated successfully."
    except Exception as e:
        return False, str(e)
