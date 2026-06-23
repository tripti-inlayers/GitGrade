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

    src_folder_present = any(
        path.startswith("src/")
        for path in paths
    )

    tests_folder_present = any(
        path.startswith("tests/")
        or path.startswith("test/")
        for path in paths
    )

    github_actions_present = any(
        path.startswith(".github/")
        for path in paths
    )

    return {
        "gitignore_present": gitignore_present,
        "dependency_file_present": dependency_file_present,
        "src_folder_present": src_folder_present,
        "tests_folder_present": tests_folder_present,
        "github_actions_present": github_actions_present
    }