from fastapi import APIRouter
from schemas.datos_suelo_schema import DatosSuelo
from services.SistemaPrediccion import predict_rf, predict_svm

router = APIRouter(tags=["Prediccion"])

@router.post("/predict/rf")
async def predict_random_forest(data: DatosSuelo):
    result = predict_rf(data)
    return {
        "model": "RandomForest",
        "prediction": result
    }

@router.post("/predict/svm")
async def predict_svm_model(data: DatosSuelo):
    result = predict_svm(data)
    return {
        "model": "SVM",
        "prediction": result
    }
