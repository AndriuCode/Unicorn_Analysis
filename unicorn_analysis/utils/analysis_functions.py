

def calculate_ROI(datos, ganado, invertido):
    ganancia_neta = datos[ganado] - datos[invertido]
    roi = (ganancia_neta / datos[invertido]) * 100

    return round(roi, 2) 