import React from 'react';

function ResultPage({ result, onTryAgain }) {
  if (!result) {
    return <p>Loading results...</p>;
  }
  const { techPath, reason } = result;
  const pathColors = {
    "Data Science": "info",
    "Web Development": "success",
    "Web Development (Frontend Focus)": "primary",
    "Game Development": "warning",
    "Game Development or AR/VR Development": "warning",
    "Cybersecurity": "danger",
    "UI/UX Design": "secondary",
    "General Tech": "dark"
  };
  const headingColorClass = `text-${pathColors[techPath] || 'dark'}`;

  return (
    <div className="card shadow rounded p-4" style={{ backgroundColor: 'white' }}>
      <h2 className={`text-center mb-3 ${headingColorClass}`} style={{ fontSize: '2rem', fontWeight: 'bold' }}>
        Your Suggested Tech Path:
      </h2>
      <h3 className={`text-center mb-4 ${headingColorClass}`} style={{ fontSize: '2.5rem', fontWeight: 'bold' }}>
        {techPath}
      </h3>
      <div className="card-body text-center">
        <p className="card-text fs-5 mb-4">{reason}</p>
        <button onClick={onTryAgain} className="btn btn-outline-primary w-50">
          Try Again
        </button>
      </div>
    </div>
  );
}
export default ResultPage;
