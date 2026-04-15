export const calculateFinalScore = (analysis) => {
  const trust = analysis.trust_score || 50;
  const fraud = analysis.fraud_risk || 0.5;

  const score =
    (trust * 0.7) -
    (fraud * 100 * 0.3);

  return Math.round(score);
};