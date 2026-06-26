import RepositoryHeader from "@/components/results/RepositoryHeader";
import OverallScore from "@/components/results/OverallScore";
import RepositoryAssessment from "@/components/results/RepositoryAssessment";
import DimensionCard from "@/components/results/DimensionCard";
import Highlights from "@/components/results/Highlights";
import ImprovementAreas from "@/components/results/ImprovementAreas";
import Recommendations from "@/components/results/Recommendations";
import Navbar from "@/components/common/Navbar";

const API_URL = process.env.NEXT_PUBLIC_API_URL;

async function getReport(owner, repo) {

  const response = await fetch(
    `${API_URL}/analyze/${owner}/${repo}`,
    {
      cache: "no-store",
    }
  );

  if (!response.ok) {
    throw new Error("Repository analysis failed.");
  }

  return response.json();

}

export default async function ResultsPage({
  params,
}) {

  const { owner, repo } = await params;

  const report = await getReport(
    owner,
    repo
  );

  return (
    <>

        <Navbar 
            generatedAt={report.generated_at} 
        />

        <main className="page-container">

        <section className="content-column py-12 space-y-8">

            <RepositoryHeader
            repository={report.repository}
            />

            <OverallScore
            score={report.scores.overall}
            />

            <RepositoryAssessment
            assessment={report.assessment}
            />

            <div className="space-y-4">

            <DimensionCard
                title="Documentation"
                score={report.scores.documentation}
                evidence={report.evidence.documentation}
            />

            <DimensionCard
                title="Project Organization"
                score={report.scores.organization}
                evidence={report.evidence.organization}
            />

            <DimensionCard
                title="Development Practices"
                score={report.scores.development}
                evidence={report.evidence.development}
            />

            <DimensionCard
                title="Project Readiness"
                score={report.scores.project_readiness}
                evidence={report.evidence.project_readiness}
            />

            </div>

            <div className="grid gap-4 md:grid-cols-3">

            <Highlights
                items={
                report.assessment?.highlights
                }
            />

            <ImprovementAreas
                items={
                report.assessment?.improvement_areas
                }
            />

            <Recommendations
                items={
                report.assessment?.recommendations
                }
            />
            </div>

        </section>

        </main>

    </>

  );

}