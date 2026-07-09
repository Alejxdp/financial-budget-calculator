import datetime
from fastapi import FastAPI
from pydantic import BaseModel

# 1. Inicializamos la aplicación FastAPI
app = FastAPI(
    title="API de Presupuesto Estilo Mark Tilbury",
    description="API para optimizar el arbitraje financiero y calcular la distribución de ingresos.",
    version="1.0.0"
)

# 2. Definimos el "Modelo de Datos" (Qué datos espera recibir la API)
class IngresoRequest(BaseModel):
    ingreso_bruto: float

# Función auxiliar para guardar el historial en el archivo de texto
def guardar_en_historial(bruto, neto, inversion, educacion, estilo):
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("historial_presupuestos.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"--- Registro API: {fecha_actual} ---\n")
        archivo.write(f"Ingreso Bruto: ${bruto:,.2f} | Neto: ${neto:,.2f}\n")
        archivo.write(f"💰 Colchón Milán (70%): ${inversion:,.2f}\n")
        archivo.write(f"📚 Educación/Idiomas (15%): ${educacion:,.2f}\n")
        archivo.write(f"🍕 Estilo de vida (15%): ${estilo:,.2f}\n")
        archivo.write("-" * 40 + "\n\n")

# 3. Creamos la Ruta de la API (El "Endpoint")
@app.post("/calcular-presupuesto")
def calcular_presupuesto(datos: IngresoRequest):
    #Sistema de impuestos locales
    impuestos_ecuador = datos.ingreso_bruto * 0.01 
    ingreso_neto = datos.ingreso_bruto - impuestos_ecuador
    
    # Lógica de distribución de Mark Tilbury (70 / 15 / 15)
    inversion_colchon = ingreso_neto * 0.70
    educacion_herramientas = ingreso_neto * 0.15
    estilo_vida_novia = ingreso_neto * 0.15
    
    # Guardamos en el archivo de texto local
    guardar_en_historial(datos.ingreso_bruto, ingreso_neto, inversion_colchon, educacion_herramientas, estilo_vida_novia)
    
    # 4. La API responde con un objeto JSON (Formato universal de datos)
    return {
        "status": "success",
        "meta": "No muestres tu riqueza, constrúyela. - Mark Tilbury",
        "resumen_financiero": {
            "ingreso_bruto": round(datos.ingreso_bruto, 2),
            "impuestos_rimpe_ecuador": round(impuestos_ecuador, 2),
            "ingreso_neto_real": round(ingreso_neto, 2)
        },
        "distribucion_inteligente": {
            "colchon_milan_70_porciento": round(inversion_colchon, 2),
            "educacion_e_idiomas_15_porciento": round(educacion_herramientas, 2),
            "estilo_vida_y_novia_15_porciento": round(estilo_vida_novia, 2)
        }
    }
