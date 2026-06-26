import RepositoryInput from "@/components/home/RepositoryInput";

export default function Home() {
  return (
    <main className="page-container">
      <section className="content-column min-h-screen flex flex-col items-center justify-center">

        <div className="text-center max-w-2xl">

          <span className="label">
            AI • GitHub Repository Analysis
          </span>

          <h1 className="mt-4 text-5xl font-bold tracking-tight text-ink">
            GitGrade
          </h1>

          <p className="mt-6 text-lg leading-8 text-subtle">
            Turn any public GitHub repository into an evidence-based quality
            report with AI-powered insights and actionable recommendations.
          </p>

        </div>

        <div className="card card-pad card-hover mt-12 w-full max-w-2xl">
          <RepositoryInput />
        </div>

        <div className="mt-20 grid w-full max-w-wide grid-cols-1 gap-6 md:grid-cols-3">

          <div className="card card-pad card-hover">
            <p className="label">Evidence Based</p>
            <h3 className="mt-3 text-lg font-semibold text-ink">
              Deterministic Scoring
            </h3>
            <p className="mt-2 text-sm text-subtle">
              Every score is backed by measurable repository signals instead of
              arbitrary AI judgments.
            </p>
          </div>

          <div className="card card-pad card-hover">
            <p className="label">AI Review</p>
            <h3 className="mt-3 text-lg font-semibold text-ink">
              Human-readable Insights
            </h3>
            <p className="mt-2 text-sm text-subtle">
              Gemini converts repository evidence into recruiter-friendly
              strengths, weaknesses and recommendations.
            </p>
          </div>

          <div className="card card-pad card-hover">
            <p className="label">Roadmap</p>
            <h3 className="mt-3 text-lg font-semibold text-ink">
              Improve Faster
            </h3>
            <p className="mt-2 text-sm text-subtle">
              Know exactly which documentation, testing or project structure
              improvements will have the biggest impact.
            </p>
          </div>

        </div>

      </section>
    </main>
  );
}