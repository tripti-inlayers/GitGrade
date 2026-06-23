def score_documentation(evidence):
    score = 0

    if evidence["readme_exists"]:
        score += 15

    if evidence["meaningful_readme"]:
        score += 20

    if evidence["installation_present"]:
        score += 15

    if evidence["usage_present"]:
        score += 15

    if evidence["tech_stack_present"]:
        score += 15

    if evidence["screenshots_present"]:
        score += 10

    if evidence["demo_link_present"]:
        score += 10

    return score

def score_organization(evidence):
    score = 0

    if evidence["gitignore_present"]:
        score += 20

    if evidence["dependency_file_present"]:
        score += 20

    if evidence["src_folder_present"]:
        score += 20

    if evidence["tests_folder_present"]:
        score += 20

    if evidence["github_actions_present"]:
        score += 20

    return score