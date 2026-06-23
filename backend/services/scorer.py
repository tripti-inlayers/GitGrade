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

    if evidence["logical_structure_present"]:
        score += 20

    if evidence["tests_folder_present"]:
        score += 20

    if evidence["github_actions_present"]:
        score += 20

    return score

def score_development_practices(evidence):
    score = 0

    if evidence["commit_count"] >= 20:
        score += 30
    elif evidence["commit_count"] >= 10:
        score += 20
    elif evidence["commit_count"] >= 5:
        score += 10

    score += int(
        evidence["quality_commit_ratio"] * 40
    )

    spread = evidence["commit_activity_spread_days"]

    if spread >= 30:
        score += 30
    elif spread >= 14:
        score += 20
    elif spread >= 7:
        score += 10

    return min(score, 100)