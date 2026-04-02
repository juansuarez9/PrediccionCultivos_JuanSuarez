import os
import joblib
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, "models")

rf_path = os.path.join(MODELS_DIR, "ModeloRandomForestCosecha.pkl")
svm_path = os.path.join(MODELS_DIR, "ModeloSupportVectorMachineCosecha.pkl")

rf_model = joblib.load(rf_path)
svm_model = joblib.load(svm_path)

def _to_array(data):
    return np.array([[
        data.nitrogeno,
        data.fosforo,
        data.potasio,
        data.temperatura,
        data.humedad,
        data.ph,
        data.lluvia
    ]])

def predict_rf(data):
    prediction = rf_model.predict(_to_array(data))
    return str(prediction[0])

def predict_svm(data):
    prediction = svm_model.predict(_to_array(data))
    return str(prediction[0])
