from services.evidence_extractor import *
from services.scorer import *
from models import (
    RepositoryEvidence,
    RepositoryScores,
    RepositoryAnalysis
)

def analyze_repository(snapshot):

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

    evidence = RepositoryEvidence(
    documentation=documentation_evidence,
    organization=organization_evidence,
    development=development_evidence,
    project_readiness=readiness_evidence
)

    scores = RepositoryScores(
        documentation=documentation_score,
        organization=organization_score,
        development=development_score,
        project_readiness=readiness_score,
        overall=overall_score
    )

    analysis = RepositoryAnalysis(
        evidence=evidence,
        scores=scores
    )

    return {
        "overall_score": overall_score,

        "documentation": {
            "score": documentation_score,
            "evidence": documentation_evidence
        },

        "organization": {
            "score": organization_score,
            "evidence": organization_evidence
        },

        "development": {
            "score": development_score,
            "evidence": development_evidence
        },

        "project_readiness": {
            "score": readiness_score,
            "evidence": readiness_evidence
        }
    }