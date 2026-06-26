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
  score,
  evidence,
}) {

  const [expanded, setExpanded] =
    useState(false);

  const items = Object.entries(
    evidence || {}
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

            <p className="label">
                {title}
            </p>

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
                  label={key
                    .replaceAll("_", " ")}
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