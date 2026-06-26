export default function RepositoryAssessment({ assessment }) {
  if (!assessment) {
    return (
      <section className="card card-pad">

        <div className="flex items-center gap-2">

          <span className="ai-tag">
            AI Assessment
          </span>

        </div>

        <p className="mt-4 text-subtle leading-relaxed">
          AI assessment is currently unavailable.
          Repository scores above are computed
          deterministically and remain valid.
        </p>

      </section>
    );
  }

  return (
    <section className="card card-pad">

      <div className="flex items-center gap-2">

        <span className="ai-tag">
          AI Assessment
        </span>

      </div>

      <p className="mt-4 leading-relaxed text-ink">
        {assessment.summary}
      </p>

    </section>
  );
}