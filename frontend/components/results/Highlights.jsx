export default function Highlights({ items = [] }) {
  if (!items.length) return null;

  return (
    <section className="card card-pad h-130 overflow-y-auto">

      <p className="label">
        Highlights
      </p>

      <ul className="mt-4 space-y-3">

        {items.map((item, index) => (

          <li
            key={index}
            className="flex items-start gap-3"
          >

            <span className="mt-1 text-score-high">
              ✓
            </span>

            <span className="text-sm leading-relaxed text-ink">
              {item}
            </span>

          </li>

        ))}

      </ul>

    </section>
  );
}