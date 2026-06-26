function getScoreColor(score) {
  if (score >= 80) {
    return {
      text: "text-score-high",
      bg: "bg-score-high-bg",
      border: "border-score-high",
      label: "Excellent",
    };
  }

  if (score >= 60) {
    return {
      text: "text-score-mid",
      bg: "bg-score-mid-bg",
      border: "border-score-mid",
      label: "Good",
    };
  }

  return {
    text: "text-score-low",
    bg: "bg-score-low-bg",
    border: "border-score-low",
    label: "Needs Improvement",
  };
}

export default function OverallScore({ score }) {
  const style = getScoreColor(score);

  return (
    <section className="card card-pad">

      <div className="flex flex-col items-center justify-center gap-6 md:flex-row md:justify-between">

        <div>

          <p className="label">
            Overall Repository Score
          </p>

          <h2 className="mt-2 text-3xl font-bold text-ink">
            GitGrade Assessment
          </h2>

          <p className="mt-3 max-w-lg text-subtle">
            Overall quality based on documentation,
            organization, development practices and
            project readiness.
          </p>

        </div>

        <div
          className={`flex h-44 w-44 flex-col items-center justify-center rounded-full border-4 ${style.bg} ${style.border}`}
        >

          <span
            className={`text-score-lg font-bold ${style.text}`}
          >
            {score}
          </span>

          <span className="text-sm font-medium text-subtle">
            /100
          </span>

          <span
            className={`mt-2 rounded-full px-3 py-1 text-xs font-semibold ${style.bg} ${style.text}`}
          >
            {style.label}
          </span>

        </div>

      </div>

    </section>
  );
}