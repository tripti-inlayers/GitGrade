"use client";

export default function Error({
  error,
  reset,
}) {

  return (

    <main className="page-container">

      <section className="content-column flex min-h-screen items-center justify-center">

        <div className="card card-pad max-w-lg text-center">

          <h2 className="text-2xl font-semibold text-ink">
            Analysis Failed
          </h2>

          <p className="mt-3 text-subtle">
            {error.message}
          </p>

          <button
            onClick={() => reset()}
            className="btn-primary mt-8"
          >
            Try Again
          </button>

        </div>

      </section>

    </main>

  );

}