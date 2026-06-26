from services.evidence_extractor import *
from services.scorer import *
from services.ai_analyzer import generate_report
from datetime import datetime

def analyze_repository(snapshot):

    repo = snapshot["repo"]

    documentation_evidence = extract_documentation(snapshot)
    documentation_score = score_documentation(
        documentation_evidence
    )

    organization_evidence = extract_organization(snapshot)
    organization_score = score_organization(
        organization_evidence
    )

    development_evidence = (
        extract_development_practices(snapshot)
    )
    development_score = (
        score_development_practices(
            development_evidence
        )
    )

    readiness_evidence = (
        extract_project_readiness(snapshot)
    )
    readiness_score = (
        score_project_readiness(
            readiness_evidence
        )
    )

    overall_score = calculate_overall_score(
        documentation_score,
        organization_score,
        development_score,
        readiness_score
    )

    print("OVERALL:", overall_score)
    print("DOC:", documentation_score)
    print("ORG:", organization_score)
    print("DEV:", development_score)
    print("READY:", readiness_score)

    generated_at = datetime.now().strftime(
        "%d %b %Y • %I:%M %p"
    )

    analysis = {

        "generated_at": generated_at,

        "repository": {
            "owner": repo["owner"],
            "name": repo["name"],
            "description": repo["description"],
            "language": repo["language"],
            "stars": repo["stars"],
            "forks": repo["forks"],
            "avatar_url": repo["avatar_url"],
            "github_url": repo["html_url"],
            "updated_at": repo["updated_at"]
        },

        "scores": {
            "overall": overall_score,
            "documentation": documentation_score,
            "organization": organization_score,
            "development": development_score,
            "project_readiness": readiness_score
        },

        "evidence": {
            "documentation": documentation_evidence,
            "organization": organization_evidence,
            "development": development_evidence,
            "project_readiness": readiness_evidence
        },

        "assessment": None,

        "generated_at": generated_at
    }

    analysis["assessment"] = generate_report(analysis)
    return analysis