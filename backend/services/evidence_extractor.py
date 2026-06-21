def extract_documentation(snapshot):
    readme_exists = snapshot["readme"]["exists"]

    readme_size = 0
    meaningful_readme = False

    if readme_exists:
        readme_size = snapshot["readme"]["data"]["size"]

        if readme_size > 1000:
            meaningful_readme = True

    return {
        "readme_exists": readme_exists,
        "readme_size": readme_size,
        "meaningful_readme": meaningful_readme
    }