from ml_model import predict_allergy

# Test with example symptoms
test_symptoms = ["Sneezing", "Itchy Eyes"]
prediction = predict_allergy(test_symptoms)

print(f"Predicted Allergy: {prediction}")