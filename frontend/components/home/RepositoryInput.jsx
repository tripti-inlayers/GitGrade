"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { extractRepository } from "@/services/api";

export default function RepositoryInput() {
  const router = useRouter();

  const [url, setUrl] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  function handleAnalyze() {
    try {
      setError("");

      const { owner, repo } = extractRepository(url);

      setLoading(true);

      router.push(`/results/${owner}/${repo}`);

    } catch (err) {
      setError(err.message);
      setLoading(false);
    }
  }

  return (
    <div className="card card-pad mt-10 w-full max-w-3xl">

      <label className="label mb-3 block">
        Repository URL
      </label>

      <div className="flex gap-3">

        <input
          className="input-base flex-1"
          placeholder="https://github.com/owner/repository"
          value={url}
          disabled={loading}
          onChange={(e) => setUrl(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              handleAnalyze();
            }
          }}
        />

        <button
          className="btn-primary min-w-35"
          disabled={loading}
          onClick={handleAnalyze}
        >
          {loading ? "Analyzing..." : "Analyze"}
        </button>

      </div>

      {error && (
        <p className="mt-3 text-sm text-score-low">
          {error}
        </p>
      )}

    </div>
  );
}