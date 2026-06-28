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

    if evidence["no_build_artifacts"]:
        score += 40

    return score


def score_project_readiness(evidence):
    score = 0

    if evidence["has_deployment_evidence"]:
        score += 45

    if evidence["environment_documented"]:
        score += 30

    if evidence["project_documentation_present"]:
        score += 25

    return score


def calculate_overall_score(
    documentation,
    organization,
    project_readiness,
):
    return round(
        documentation * 0.30 +
        organization * 0.35 +
        project_readiness * 0.35
    )