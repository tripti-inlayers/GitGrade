import Link from "next/link";

export default function Navbar({ generatedAt }) {
  return (
    <header className="sticky top-0 z-50 border-b border-border bg-surface/90 backdrop-blur-md">

      <div className="mx-auto flex h-16 max-w-wide items-center justify-between px-8">

        <Link
          href="/"
          className="group"
        >
          <h1 className="text-2xl font-bold tracking-tight text-ink transition-colors group-hover:text-accent">
            GitGrade
          </h1>
        </Link>

        <div className="flex flex-col items-end">

          <p className="label">
            Report Generated
          </p>

          <p className="mt-1 text-sm text-subtle">
            {generatedAt}
          </p>

        </div>

      </div>

    </header>
  );
}