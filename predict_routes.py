from flask import Blueprint, request, jsonify
from ml_model import predict_allergy

predict_blueprint = Blueprint("predict", __name__)

@predict_blueprint.route('/predict', methods=['POST'])
def predict():
    symptoms = request.json['symptoms']
    prediction = predict_allergy(symptoms)
    return jsonify({"prediction": prediction})