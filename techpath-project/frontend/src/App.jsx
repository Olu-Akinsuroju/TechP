import React, { useState } from 'react';
import SurveyForm from './components/SurveyForm';
import ResultPage from './components/ResultPage';
// import './App.css'; // Assuming App.css is empty or not strictly needed

function App() {
  const [surveyResult, setSurveyResult] = useState(null);

  const handleSurveySubmit = (result) => {
    setSurveyResult(result);
  };

  const handleTryAgain = () => {
    setSurveyResult(null);
  };

  return (
    <div className="container d-flex flex-column align-items-center justify-content-center min-vh-100">
      {!surveyResult ? (
        <SurveyForm onSubmit={handleSurveySubmit} />
      ) : (
        <ResultPage result={surveyResult} onTryAgain={handleTryAgain} />
      )}
    </div>
  );
}
export default App;
