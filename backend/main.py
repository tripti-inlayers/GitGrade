from fastapi import FastAPI
from services.github_fetcher import get_repo_details,get_readme,get_commits,get_contributors,get_file_tree,fetch_snapshot
from services.evidence_extractor import extract_documentation, extract_organization, extract_development_practices, extract_project_readiness
from services.scorer import score_documentation, score_organization, score_development_practices, score_project_readiness, calculate_overall_score
from services.analyzer import analyze_repository

app = FastAPI()


@app.get("/")
def home():
    return {"message": "GitGrade Backend Running"}


@app.get("/repo/{owner}/{repo}")
def repo_details(owner: str, repo: str):
    return get_repo_details(owner, repo)

@app.get("/readme/{owner}/{repo}")
def readme(owner: str, repo: str):
    return get_readme(owner, repo)

@app.get("/commits/{owner}/{repo}")
def commits(owner: str, repo: str):
    return get_commits(owner, repo)

@app.get("/contributors/{owner}/{repo}")
def contributors(owner: str, repo: str):
    return get_contributors(owner, repo)

@app.get("/tree/{owner}/{repo}")
def tree(owner: str, repo: str):
    return get_file_tree(owner, repo)

@app.get("/documentation/{owner}/{repo}")
def documentation(owner: str, repo: str):
    snapshot = fetch_snapshot(owner, repo)
    return extract_documentation(snapshot)

@app.get("/doc-score/{owner}/{repo}")
def doc_score(owner: str, repo: str):
    snapshot = fetch_snapshot(owner, repo)

    evidence = extract_documentation(snapshot)

    return {
        "documentation_score": score_documentation(evidence),
        "evidence": evidence
    }

@app.get("/organization/{owner}/{repo}")
def organization(owner: str, repo: str):
    snapshot = fetch_snapshot(owner, repo)

    return extract_organization(snapshot)

@app.get("/organization-score/{owner}/{repo}")
def organization_score(owner: str, repo: str):
    snapshot = fetch_snapshot(owner, repo)

    evidence = extract_organization(snapshot)

    return {
        "organization_score": score_organization(evidence),
        "evidence": evidence
    }

@app.get("/dev-practices/{owner}/{repo}")
def dev_practices(owner: str, repo: str):
    snapshot = fetch_snapshot(owner, repo)

    return extract_development_practices(snapshot)

@app.get("/dev-practices-score/{owner}/{repo}")
def dev_practices_score(owner: str, repo: str):
    snapshot = fetch_snapshot(owner, repo)

    evidence = extract_development_practices(snapshot)

    score = score_development_practices(evidence)

    return {
        "score": score,
        "evidence": evidence
    }

@app.get("/project-readiness/{owner}/{repo}")
def project_readiness(owner: str, repo: str):
    snapshot = fetch_snapshot(owner, repo)

    evidence = extract_project_readiness(snapshot)

    return evidence

@app.get("/project-readiness-score/{owner}/{repo}")
def project_readiness_score(owner: str, repo: str):
    snapshot = fetch_snapshot(owner, repo)

    evidence = extract_project_readiness(snapshot)

    score = score_project_readiness(evidence)

    return {
        "project_readiness_score": score,
        "evidence": evidence
    }

@app.get("/analyze/{owner}/{repo}")
def analyze_repo(owner: str, repo: str):

    snapshot = fetch_snapshot(owner, repo)

    return analyze_repository(snapshot)