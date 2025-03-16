import torch
import joblib
import pandas as pd

# Load trained model
model = torch.load("allergy_model.pth")
model.eval()

# Load label encoder
label_encoder = joblib.load("label_encoder.pkl")

# Load dataset
data = pd.read_csv("allergy_data.csv")
symptom_encoder = data['Symptoms'].str.get_dummies(sep=', ')

def predict_allergy(symptoms):
    input_data = torch.tensor([symptom_encoder.loc[:, symptoms].values[0]], dtype=torch.float32)
    output = model(input_data)
    predicted_label = torch.argmax(output).item()
    return label_encoder.inverse_transform([predicted_label])[0]