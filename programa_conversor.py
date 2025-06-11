import pandas as pd


def cm_a_pulgadas(cm):
    #Convierte centímetros a pulgadas.
    return cm / 2.54


# leer el archivo Excel
df = pd.read_excel("muebles_medidas.xlsx")

# Añadir una nueva columna al DataFrame que sea de pulgadas y se rellene con el calculo de cm / 2.54

df["Pulgadas"] = df["Centimetros"].apply(cm_a_pulgadas)

df.to_excel("muebles_medidas_convertidas.xlsx", index=False)# Guardamos el DataFrame en un archivo Excel llamado "muebles_medidas_convertidas.xlsx"

print("Conversión completada. El archivo 'muebles_medidas_convertidas.xlsx' ha sido creado.")


