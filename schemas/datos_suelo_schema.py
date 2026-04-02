from pydantic import BaseModel, Field

class DatosSuelo(BaseModel):
    nitrogeno: float = Field(..., example=90, description="Cantidad de nitrogeno en el suelo")
    fosforo: float = Field(..., example=42, description="Cantidad de fosforo en el suelo")
    potasio: float = Field(..., example=43, description="Cantidad de potasio en el suelo")
    temperatura: float = Field(..., example=20.87, description="Temperatura del suelo o ambiente")
    humedad: float = Field(..., example=82.0, description="Porcentaje de humedad")
    ph: float = Field(..., example=6.5, description="Nivel de pH del suelo")
    lluvia: float = Field(..., example=202.93, description="Nivel de precipitacion o lluvia")
