export default function RepositoryHeader({ repository }) {
  if (!repository) return null;

  return (
    <section className="card card-pad">

      <div className="flex flex-col gap-6 md:flex-row md:items-start md:justify-between">

        <div className="flex items-start gap-4">

          <img
            src={repository.avatar_url}
            alt={repository.owner}
            className="h-14 w-14 rounded-full border border-border"
          />

          <div>

            <h1 className="text-2xl font-bold tracking-tight text-ink">
              {repository.owner} / {repository.name}
            </h1>

            {repository.description && (
              <p className="mt-2 max-w-2xl text-subtle">
                {repository.description}
              </p>
            )}

            <div className="mt-4 flex flex-wrap items-center gap-4 text-sm text-ghost">

              {repository.language && (
                <span>{repository.language}</span>
              )}

              <span>⭐ {repository.stars}</span>

              <span>🍴 {repository.forks}</span>

              <span>
                Updated {new Date(repository.updated_at).toLocaleDateString()}
              </span>

            </div>

          </div>

        </div>

        <a
          href={repository.github_url}
          target="_blank"
          rel="noopener noreferrer"
          className="btn-primary shrink-0"
        >
          View Repository ↗
        </a>

      </div>

    </section>
  );
}