"use client";

import { useState } from "react";
import EvidenceItem from "./EvidenceItem";

function getBorder(score) {

  if (score >= 80)
    return "tier-high";

  if (score >= 60)
    return "tier-mid";

  return "tier-low";

}

export default function DimensionCard({
  title,
  weight,
  score,
  evidence,
}) {

  const [expanded, setExpanded] = useState(false);

  const LABELS = {
    readme_exists: "README Present",
    meaningful_readme: "Detailed README",
    installation_present: "Installation Guide",
    usage_present: "Usage Examples",
    tech_stack_present: "Technologies Used",
    screenshots_present: "Visual Preview",
    demo_link_present: "Live Demo",

    gitignore_present: "Git Ignore Configured",
    dependency_file_present: "Dependencies Declared",
    logical_structure_present: "Organised Folder Structure",
    no_build_artifacts: "Clean Repository",

    has_license: "License Included",
    has_deployment_evidence: "Deployment Configured",
    environment_documented: "Environment Setup Documented",
    project_documentation_present: "Additional Project Docs",
  };

  const items = Object.entries(evidence || {}).filter(
    ([key]) =>
      ![
        "readme_size",
        "repo_age_days",
        "recent_activity_days",
      ].includes(key)
  );

  return (

    <section
      className={`card card-hover ${getBorder(score)}`}
    >

      <div className="px-8 py-6">

        <button
            onClick={() => setExpanded(!expanded)}
            className="flex w-full items-center justify-between"
            >

            <div className="text-left">

                <p className="label">
                    {title}
                </p>

                <p className="mt-1 text-xs text-subtle">
                    {weight} of Overall Score
                </p>

            </div>

            <div className="flex items-center gap-3">

                <h3
                className={`text-3xl font-bold ${
                    score >= 80
                    ? "text-score-high"
                    : score >= 60
                    ? "text-score-mid"
                    : "text-score-low"
                }`}
                >
                {score}
                <span className="ml-1 text-xl font-medium text-subtle">
                    /100
                </span>
                </h3>

                <svg
                className={`chevron ${
                    expanded ? "chevron-open" : ""
                }`}
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                viewBox="0 0 24 24"
                >
                <path
                    d="M19 9l-7 7-7-7"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                />
                </svg>

            </div>

            </button>   

        {expanded && (

          <div className="mt-5 border-t border-border pt-4">

            {items.map(
              ([key, value]) => (

                <EvidenceItem
                  key={key}
                  label={LABELS[key] || key.replaceAll("_", " ")}
                  detected={
                    Boolean(value)
                  }
                />

              )
            )}

          </div>

        )}

      </div>

    </section>

  );

}