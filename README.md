# TrabajoFinal_Suarez

Proyecto final de recomendacion de cultivo con FastAPI, Random Forest, SVM, Pydantic, Postman y cliente web.

## Estructura
- `principal.py`: punto de entrada de FastAPI
- `routers/`: endpoints
- `schemas/`: modelos Pydantic
- `services/`: carga de modelos y prediccion
- `models/`: modelos serializados `.pkl`
- `web/index.html`: cliente web con estilo tipo liquid glass
- `postman/`: coleccion de Postman

## Crear entorno en Anaconda
```bash
conda env create -f environment.yml
conda activate cultivo_ai
```

## Ejecutar la API
```bash
uvicorn principal:app --reload
```

## Probar
- Swagger: `http://127.0.0.1:8000/docs`
- Cliente web: abrir `web/index.html`

## Endpoints
- `POST /predict/rf`
- `POST /predict/svm`

## JSON de entrada
```json
{
  "nitrogeno": 90,
  "fosforo": 42,
  "potasio": 43,
  "temperatura": 20.87,
  "humedad": 82.0,
  "ph": 6.5,
  "lluvia": 202.93
}
```
