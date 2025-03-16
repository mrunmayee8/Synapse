from flask import Flask, request, jsonify
import torch
import torchvision.transforms as transforms
from PIL import Image
import os
import pickle  # To load the label encoder

app = Flask(__name__)

# Load the model
MODEL_PATH = "path/to/allergy_model.pth"  # Update this path
model = torch.load(MODEL_PATH, map_location=torch.device("cpu"))
model.eval()  # Set model to evaluation mode

# Load the label encoder
LABEL_ENCODER_PATH = "path/to/label_encoder.pkl"  # Update this path
with open(LABEL_ENCODER_PATH, "rb") as f:
    label_encoder = pickle.load(f)

# Define transformations for image preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

def predict_allergen(image_path):
    """Predicts the allergen class from an image."""
    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0)

    with torch.no_grad():
        output = model(image)
        prediction_idx = torch.argmax(output, dim=1).item()
        prediction_label = label_encoder.inverse_transform([prediction_idx])[0]  # Convert index to label
    
    return prediction_label

# API endpoint for image upload and prediction
@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    file_path = os.path.join("uploads", file.filename)
    file.save(file_path)

    result = predict_allergen(file_path)
    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)