import datetime

def guardar_en_historial(bruto, neto, inversion, educacion, estilo):
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("historial_presupuestos.txt", "a" encoding="utf-8") as archivo:
        archivo.write(f"--- Registro: {fecha_actual} ---\n")
        archivo.write(f"Ingreso Bruto: ${bruto:.2f} | Neto: {neto:,.2f}\n")
        archivo.write(f"Colchón Milán (70%): ${inversion:,.2f}\n")
        archivo.write(f"Educación/Idiomas (15%): ${educacion:,.2f}\n")
        archivo.write(f"Estilo de Vida (15%): ${estilo:,.2f}\n")
        archivo.write("-"*40+"\n\n")

def calcular_presupuesto_tilbury():
    print ("--- CALCULADORA DE PRESUPUESTO ESTILO TILBURY ---")
    print ("Optimizado para el arbitraje de financiero desde Ecuador/n")

    try:
        # 1. User data entry
        ingreso_bruto = float(input("Introduce tus ingresos de este mes : $"))
        
        # 2. Taxes Ecuador
        # Si ganas menos de $20,000 al año el RIMPE cobra aprox. 1% de tasa efectiva
        impuestos_ecuador = ingreso_bruto * 0.01
        ingreso_neto = ingreso_bruto - impuestos_ecuador

        # 3. Aplicacion de porcentajes optimizados
        inversion_colchon = ingreso_neto * 0.70 
        educacion_herramientas = ingreso_neto * 0.15
        estilo_de_vida = ingreso_neto * 0.15

        # 4. Mostrar resultados en pantalla
        print ("\n==================================")
        print (f"Ingreso Bruto: ${ingreso_bruto:.2f}")
        print (f"Reserva para impuestos (RIMPE): ${impuestos_ecuador:.2f}")
        print (f"Ingreso Neto Real: ${ingreso_neto:,.2f}")
        print ("\n==================================")
        print (f"[70%] Colchón Milan / Fondos indexados: ${inversion_colchon:,.2f}")
        print (f"[15%] Educación, idiomas y Herramientas: ${educacion_herramientas:,.2f}")
        print (f"[15%] Estilo de vida y gastos personales: ${estilo_de_vida:,.2f}")
        print ("\n==================================")
        print ("Recuerda la frase de Tilbury: 'No muestres tu riqueza, construyela'.")

    except ValueError:
        print("Error: Por favor, introduce un número válido.")
if __name__ == "__main__":
    calcular_presupuesto_tilbury()