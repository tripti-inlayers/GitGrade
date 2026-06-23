import requests
import base64


def get_repo_details(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"

    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "Repository not found"}

    data = response.json()

    return {
        "name": data["name"],
        "owner": data["owner"]["login"],
        "description": data["description"],
        "stars": data["stargazers_count"],
        "forks": data["forks_count"],
        "default_branch": data["default_branch"]
    }

def get_readme(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/readme"

    response = requests.get(url)

    if response.status_code != 200:
        return {
            "exists": False,
            "data": None
        }

    data = response.json()

    content = base64.b64decode(
        data["content"]
    ).decode("utf-8")

    return {
        "exists": True,
        "data": {
            "name": data["name"],
            "size": data["size"],
            "content": content
        }
    }


    

def get_commits(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits?per_page=50"

    response = requests.get(url)

    if response.status_code != 200:
        return {
            "exists": False,
            "data": None
        }

    commits = response.json()

    commit_data = []

    for commit in commits:
        commit_data.append({
            "sha": commit["sha"],
            "message": commit["commit"]["message"].split("\n")[0],
            "date": commit["commit"]["author"]["date"],
            "author": commit["commit"]["author"]["name"]
        })

    return {
        "exists": True,
        "data": commit_data
    }

def get_contributors(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/contributors?per_page=20"

    response = requests.get(url)

    if response.status_code != 200:
        return {
            "exists": False,
            "data": None
        }

    contributors = response.json()

    contributor_data = []

    for contributor in contributors:
        contributor_data.append({
            "username": contributor["login"],
            "commit_count": contributor["contributions"]
        })

    return {
        "exists": True,
        "data": contributor_data
    }

def get_file_tree(owner, repo):
    repo_data = get_repo_details(owner, repo)
    print(repo_data)

    default_branch = repo_data["default_branch"]

    url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{default_branch}?recursive=1"

    response = requests.get(url)

    if response.status_code != 200:
        return {
            "exists": False,
            "data": None
        }

    data = response.json()

    file_paths = []

    for item in data["tree"]:
        file_paths.append(item["path"])

    return {
        "exists": True,
        "data": file_paths
    }

def fetch_snapshot(owner, repo):
    return {
        "repo": get_repo_details(owner, repo),
        "readme": get_readme(owner, repo),
        "commits": get_commits(owner, repo),
        "contributors": get_contributors(owner, repo),
        "file_tree": get_file_tree(owner, repo)
    }