export default function RepositoryMetadata({
  metadata,
}) {
  return (
    <section className="card card-hover">

      <div className="px-8 py-6">

        <p className="label">
            Repository Metadata
            </p>

            <p className="mt-2 mb-6 text-sm text-subtle">
            Additional repository context. These metrics are displayed for transparency and do not affect the overall score.
            </p>

            <hr className="my-5 border-border" />

        <div className="space-y-3">

          <MetadataRow
            label="Primary Language"
            value={metadata.primary_language}
          />

          <MetadataRow
            label="Repository Age"
            value={`${metadata.repository_age_days} days`}
          />

          <MetadataRow
            label="Last Updated"
            value={`${metadata.last_updated_days} days ago`}
          />

          <MetadataRow
            label="Commit Count"
            value={metadata.commit_count}
          />

          <MetadataRow
            label="Meaningful Commit Ratio"
            value={`${Math.round(
              metadata.meaningful_commit_ratio * 100
            )}%`}
          />

          <MetadataRow
            label="Contributors"
            value={metadata.contributors}
          />

        </div>

      </div>

    </section>
  );
}

function MetadataRow({
  label,
  value,
}) {
  return (
    <div className="flex justify-between">

      <span className="text-subtle">
        {label}
      </span>

      <span className="font-medium">
        {value}
      </span>

    </div>
  );
}