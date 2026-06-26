"use client";

import { useEffect, useState } from "react";

const STEPS = [
  "Repository detected",
  "Collecting repository data",
  "Evaluating documentation",
  "Measuring project organization",
  "Analyzing development practices",
  "Evaluating project readiness",
  "Preparing report",
];

export default function AnalysisProgress() {
  const [activeStep, setActiveStep] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
        setActiveStep((current) => {
        if (current >= STEPS.length - 1) {
            clearInterval(timer);
            return current;
        }

        return current + 1;
        });
    }, 300);

    return () => clearInterval(timer);
    }, []);

  return (
    <main className="page-container">

      <section className="content-column flex min-h-screen items-center justify-center">

        <div className="card card-pad w-full max-w-2xl">

          <p className="label">
            GitGrade Analysis
          </p>

          <h1 className="mt-2 text-4xl font-bold text-ink">
            Analyzing Repository
          </h1>

          <p className="mt-3 text-subtle">
            We're collecting repository evidence and
            preparing your quality report.
          </p>

          <div className="mt-10 space-y-5">

            {STEPS.map((step, index) => {

              const completed = index < activeStep;
              const active = index === activeStep;

              return (

                <div
                    key={step}
                    className="flex items-center gap-4"
                >

                    <div
                    className={`
                        flex h-8 w-8 items-center justify-center rounded-full
                        transition-all duration-500
                        ${
                        completed
                            ? "bg-green-500 text-white"
                            : active
                            ? "border-2 border-blue-600 text-blue-600"
                            : "border border-gray-300 text-gray-300"
                        }
                    `}
                    >

                    {completed ? (
                        "✓"
                    ) : active ? (
                        <svg
                        className="h-5 w-5 animate-spin"
                        viewBox="0 0 24 24"
                        fill="none"
                        >
                        <circle
                            cx="12"
                            cy="12"
                            r="9"
                            stroke="currentColor"
                            strokeWidth="3"
                            strokeLinecap="round"
                            strokeDasharray="40 20"
                        />
                        </svg>
                    ) : null}

                    </div>

                    <div className="flex flex-col">

                    <span
                        className={
                        completed
                            ? "font-medium text-black"
                            : active
                            ? "font-semibold text-blue-600"
                            : "text-gray-400"
                        }
                    >
                        {step}
                    </span>

                    </div>

                </div>

                );

            })}

          </div>

          <div className="mt-10 h-2 overflow-hidden rounded-full bg-canvas">

            <div
              className="h-full rounded-full bg-accent transition-all duration-300"
              style={{
                width: `${
                  ((activeStep + 1) / STEPS.length) * 100
                }%`,
              }}
            />

          </div>

          <p className="mt-4 text-center text-sm text-subtle">
            This usually takes a few seconds.
          </p>

        </div>

      </section>

    </main>
  );
}