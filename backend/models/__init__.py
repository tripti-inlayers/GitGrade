from dataclasses import dataclass

@dataclass
class RepositoryEvidence:
    documentation: dict
    organization: dict
    development: dict
    project_readiness: dict


@dataclass
class RepositoryScores:
    documentation: int
    organization: int
    development: int
    project_readiness: int
    overall: int


@dataclass
class RepositoryAnalysis:
    evidence: RepositoryEvidence
    scores: RepositoryScores