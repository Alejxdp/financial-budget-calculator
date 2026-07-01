from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 1. Esta lista de Python simulará nuestra Base de Datos física
BASE_DE_DATOS_ESTUDIANTES = [
    {"id": 1, "nombre": "Alejandro", "universidad": "ESPE"},
    {"id": 2, "nombre": "Ragnar", "universidad": "Valhalla University"}
]

# 2. Creamos el "molde" o esquema de cómo deben lucir los datos que viajan por internet
class EsquemaEstudiante(BaseModel):
    nombre: str
    universidad: str

# RUTA GET: Para LEER los datos (Equivalente a consultar la base de datos)
@app.get("/estudiantes")
def obtener_todos_los_estudiantes():
    return BASE_DE_DATOS_ESTUDIANTES

# RUTA POST: Para CREAR/GUARDAR datos (Equivalente a insertar en la base de datos)
@app.post("/estudiantes")
def registrar_estudiante(datos_recibidos: EsquemaEstudiante):
    # Simulamos la creación de un ID único sumando 1 al tamaño de la lista
    nuevo_id = len(BASE_DE_DATOS_ESTUDIANTES) + 1
    
    # Construimos el objeto final combinando el ID con los datos que llegaron de internet
    nuevo_estudiante = {
        "id": nuevo_id,
        "nombre": datos_recibidos.nombre,
        "universidad": datos_recibidos.universidad
    }
    
    # ¡Lo guardamos en nuestra base de datos simulada!
    BASE_DE_DATOS_ESTUDIANTES.append(nuevo_estudiante)
    
    # Respondemos al cliente con un mensaje de éxito
    return {"mensaje": "¡Estudiante guardado con éxito!", "datos": nuevo_estudiante}