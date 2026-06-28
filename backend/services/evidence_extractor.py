from datetime import datetime


def extract_documentation(snapshot):
    readme_exists = snapshot["readme"]["exists"]

    readme_size = 0
    meaningful_readme = False

    installation_present = False
    usage_present = False
    tech_stack_present = False
    screenshots_present = False
    demo_link_present = False

    if readme_exists:
        readme_data = snapshot["readme"]["data"]

        readme_size = readme_data["size"]

        if readme_size > 1000:
            meaningful_readme = True

        content = readme_data["content"].lower()

        installation_keywords = [
            "npm install",
            "pip install",
            "pnpm install",
            "yarn",
            "docker",
            "cargo",
            "brew install",
            "apt install"
        ]

        installation_present = any(
            keyword in content
            for keyword in installation_keywords
        )

        usage_keywords = [
            "## usage",
            "## getting started",
            "## example",
            "## examples"
        ]

        usage_present = any(
            keyword in content
            for keyword in usage_keywords
        )

        tech_keywords = [
            "react",
            "next.js",
            "nextjs",
            "python",
            "fastapi",
            "node.js",
            "mongodb",
            "postgresql"
        ]

        tech_stack_present = any(
            keyword in content
            for keyword in tech_keywords
        )

        screenshots_present = (
            "![" in content or
            "<img" in content
        )   

        demo_keywords = [
            "vercel.app",
            "netlify.app",
            "render.com",
            "railway.app",
            "live demo",
            "deployment"
        ]

        demo_link_present = any(
            keyword in content
            for keyword in demo_keywords
        )

    return {
        "readme_exists": readme_exists,
        "readme_size": readme_size,
        "meaningful_readme": meaningful_readme,
        "installation_present": installation_present,
        "usage_present": usage_present,
        "tech_stack_present": tech_stack_present,
        "screenshots_present": screenshots_present,
        "demo_link_present": demo_link_present
    }

def extract_organization(snapshot):
    paths = []

    if snapshot["file_tree"]["exists"]:
        paths = snapshot["file_tree"]["data"]

    gitignore_present = ".gitignore" in paths

    dependency_file_present = any(
        file in paths
        for file in [
            "package.json",
            "requirements.txt",
            "pyproject.toml",
            "Pipfile",
            "Cargo.toml",
            "pom.xml"
        ]
    )

    logical_structure_present = any(
    path.split("/")[0]
    in [
        "src",
        "lib",
        "app",
        "frontend",
        "backend",
        "client",
        "server",
        "packages"
    ]
    for path in paths
)
    
    BUILD_ARTIFACTS = [
        "node_modules/",
        "dist/",
        "build/",
        "__pycache__/",
        ".next/",
        ".parcel-cache/",
        ".turbo/",
    ]

    no_build_artifacts = not any(
        any(
            path.startswith(artifact)
            for artifact in BUILD_ARTIFACTS
        )
        for path in paths
    )


    return {
        "gitignore_present": gitignore_present,
        "dependency_file_present": dependency_file_present,
        "logical_structure_present": logical_structure_present,
        "no_build_artifacts": no_build_artifacts,
    }

def extract_development_practices(snapshot):
    commits = []

    if snapshot["commits"]["exists"]:
        commits = snapshot["commits"]["data"]

    non_merge_commits = []

    for commit in commits:
        message = commit["message"]

        if not message.startswith("Merge "):
            non_merge_commits.append(commit)

    commit_count = len(non_merge_commits)

    quality_commit_count = 0

    bad_words = [
        "fix",
        "test",
        "wip",
        "changes",
        "stuff"
    ]

    for commit in non_merge_commits:
        message = commit["message"].lower().strip()

        word_count = len(message.split())

        if (
            word_count >= 3
            and message not in bad_words
        ):
            quality_commit_count += 1

    quality_commit_ratio = (
        quality_commit_count / commit_count
        if commit_count > 0
        else 0
    )

    commit_activity_spread_days = 0

    if len(non_merge_commits) >= 2:
        dates = [
            datetime.fromisoformat(
                commit["date"].replace("Z", "+00:00")
            )
            for commit in non_merge_commits
        ]

        commit_activity_spread_days = (
            max(dates) - min(dates)
        ).days

    return {
        "commit_count": commit_count,
        "quality_commit_count": quality_commit_count,
        "quality_commit_ratio": round(
            quality_commit_ratio,
            2
        ),
        "commit_activity_spread_days":
            commit_activity_spread_days
    }

def extract_project_readiness(snapshot):
    paths = []

    if snapshot["file_tree"]["exists"]:
        paths = snapshot["file_tree"]["data"]

    env_example_present = any(
        path.lower() == ".env.example"
        for path in paths
    )

    environment_documented = env_example_present

    if snapshot["readme"]["exists"]:
        content = snapshot["readme"]["data"]["content"].lower()

        environment_documented = (
            environment_documented
            or ".env" in content
            or "environment" in content
            or "configuration" in content
        )

    project_documentation_present = any(
            path.lower() in [
                "contributing.md",
                "architecture.md",
                "api.md",
                "design.md"
            ]
            for path in paths
        )

    project_documentation_present = (
            project_documentation_present
            or any(
                path.startswith("docs/")
                for path in paths
            )
        )

    repo = snapshot["repo"]

    has_license = any(
        path.lower() in [
            "license",
            "license.md",
            "license.txt"
        ]
        for path in paths
    )

    DEPLOYMENT_FILES = [
        "dockerfile",
        "docker-compose.yml",
        "procfile",
        "vercel.json"
    ]

    has_deployment_evidence = any(
        path.lower() in DEPLOYMENT_FILES
        or path.startswith(".github/workflows/")
        for path in paths
    )

    if snapshot["readme"]["exists"]:
        content = snapshot["readme"]["data"]["content"].lower()

        deployment_keywords = [
            "vercel.app",
            "netlify.app",
            "onrender.com",
            "railway.app",
            "render.com",
            "live demo"
        ]

        has_deployment_evidence = (
            has_deployment_evidence
            or any(
                keyword in content
                for keyword in deployment_keywords
            )
        )

    created_date = datetime.fromisoformat(
        repo["created_at"].replace("Z", "+00:00")
    )

    repo_age_days = (
        datetime.now(created_date.tzinfo)
        - created_date
    ).days

    commits = []

    if snapshot["commits"]["exists"]:
        commits = snapshot["commits"]["data"]

    recent_activity_days = None

    if commits:
        latest_commit_date = datetime.fromisoformat(
            commits[0]["date"].replace("Z", "+00:00")
        )

        recent_activity_days = (
            datetime.now(latest_commit_date.tzinfo)
            - latest_commit_date
        ).days

    return {
        "has_license": has_license,
        "has_deployment_evidence": has_deployment_evidence,

        "environment_documented": environment_documented,
        "project_documentation_present": project_documentation_present,

        "repo_age_days": repo_age_days,
        "recent_activity_days": recent_activity_days,
    }