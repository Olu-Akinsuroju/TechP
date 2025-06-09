import React, { useState } from 'react';

function SurveyForm({ onSubmit }) {
  const [interestReason, setInterestReason] = useState('');
  const [tools, setTools] = useState([]);
  const [activity, setActivity] = useState('');

  const handleToolChange = (event) => {
    const { value, checked } = event.target;
    if (checked) {
      setTools((prevTools) => [...prevTools, value]);
    } else {
      setTools((prevTools) => prevTools.filter((tool) => tool !== value));
    }
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!interestReason.trim() || tools.length === 0 || !activity) {
      alert("Please fill out all fields and select at least one tool and activity.");
      return;
    }
    try {
      // Adjusted API endpoint to be relative, Django will serve it from the same domain
      const response = await fetch('/api/suggest-path/', { // Note the trailing slash, common in Django
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          // Django CSRF token might be needed if not using @csrf_exempt or if SessionAuthentication is active
          // For simple API views with DRF and token/no auth, it's often not an immediate issue
          // For now, assuming basic setup without CSRF on this specific POST from external SPA-like frontend
        },
        body: JSON.stringify({ interestReason, tools, activity }),
      });
      if (!response.ok) {
        const errorData = await response.text(); // Read error response for more details
        throw new Error(`HTTP error! status: ${response.status}, details: ${errorData}`);
      }
      const data = await response.json();
      onSubmit(data);
    } catch (error) {
      console.error("Failed to submit survey:", error);
      alert(`Failed to submit survey: ${error.message}. Make sure the backend is running and accessible.`);
    }
  };

  const toolOptions = ["Terminal", "Figma", "Excel", "Python", "Unity"];
  const activityOptions = [
    { value: "building websites", label: "Building websites" },
    { value: "analyzing data", label: "Analyzing data" },
    { value: "securing systems", label: "Securing systems" },
    { value: "designing UIs", label: "Designing UIs" },
    { value: "building games", label: "Building games" },
  ];

  return (
    <div className="card shadow rounded p-4" style={{ backgroundColor: 'white' }}>
      <h2 className="mb-4 text-center">Tech Path Suggester</h2>
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label htmlFor="interestReason" className="form-label">
            Why are you interested in tech?
          </label>
          <input
            type="text"
            className="form-control"
            id="interestReason"
            value={interestReason}
            onChange={(e) => setInterestReason(e.target.value)}
            required
          />
        </div>
        <div className="mb-3">
          <label className="form-label">Which of these tools are you comfortable with?</label>
          {toolOptions.map((tool) => (
            <div className="form-check" key={tool}>
              <input
                className="form-check-input"
                type="checkbox"
                value={tool}
                id={`tool-${tool}`}
                onChange={handleToolChange}
                checked={tools.includes(tool)}
              />
              <label className="form-check-label" htmlFor={`tool-${tool}`}>
                {tool}
              </label>
            </div>
          ))}
        </div>
        <div className="mb-3">
          <label className="form-label">Which of these activities excites you most?</label>
          {activityOptions.map((act) => (
            <div className="form-check" key={act.value}>
              <input
                className="form-check-input"
                type="radio"
                name="activity"
                id={`activity-${act.value}`}
                value={act.value}
                checked={activity === act.value}
                onChange={(e) => setActivity(e.target.value)}
                required
              />
              <label className="form-check-label" htmlFor={`activity-${act.value}`}>
                {act.label}
              </label>
            </div>
          ))}
        </div>
        <button type="submit" className="btn btn-primary w-100">
          Suggest My Path
        </button>
      </form>
    </div>
  );
}
export default SurveyForm;
