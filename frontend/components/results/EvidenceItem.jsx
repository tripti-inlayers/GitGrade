export default function EvidenceItem({
  label,
  detected,
}) {

  return (

    <div className="flex items-center justify-between py-2">

      <span className="font-mono text-sm text-subtle">
        {label}
      </span>

      {detected ? (

        <span className="badge badge-detected">
          ✓ detected
        </span>

      ) : (

        <span className="badge badge-missing">
          not detected
        </span>

      )}

    </div>

  );

}