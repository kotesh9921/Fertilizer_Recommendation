
function recommendFertilizer() {
    // Retrieve input values
    const soilColor = document.getElementById('soilColor').value;
    const nitrogen = parseFloat(document.getElementById('nitrogen').value);
    const phosphorus = parseFloat(document.getElementById('phosphorus').value);
    const potassium = parseFloat(document.getElementById('potassium').value);
    const phValue = parseFloat(document.getElementById('phValue').value);
    const rainfall = parseFloat(document.getElementById('rainfall').value);
    const temperature = parseFloat(document.getElementById('temperature').value);
    const cropType = document.getElementById('cropType').value;

    // Your fertilizer recommendation logic goes here
    // For now, a simple example recommendation is provided
    let recommendation = "Use a balanced fertilizer for optimal growth.";

    // Display recommendation result
    const resultElement = document.getElementById('recommendationResult');
    resultElement.textContent = `Recommendation for ${cropType} on ${soilColor} soil: ${recommendation}`;
}