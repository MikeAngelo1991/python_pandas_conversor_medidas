import pandas as pd


# Dataframe es la información básica con el nombre de las piezas y centimetros para poder armar el Excel.

data = {
    "Piezas": ["Pata", "Tablero", "Puerta", "Estante", "Panel Lateral"],
    "Centimetros": [40, 120, 60, 30, 180],
}

df = pd.DataFrame(data)
# Guardamos el DataFrame en un archivo Excel llamado "muebles_medidas.xlsx"

df.to_excel("muebles_medidas.xlsx", index=False)
print("Archivo muebles_medidas.xlsx ha sido creado con las medidas de las piezas.")



