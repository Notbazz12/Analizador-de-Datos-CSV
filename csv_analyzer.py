import pandas as pd
import plotly.express as px

def leer_excel(ruta_archivo):
    """Leer el archivo Excel en un DataFrame."""
    df = pd.read_excel(ruta_archivo)
    return df

def manejar_valores_faltantes(df, metodo='eliminar', valor_relleno=None):
    """
    Manejar valores faltantes en el DataFrame.
    
    :param df: El DataFrame a procesar.
    :param metodo: El método para manejar valores faltantes ('eliminar' o 'rellenar').
    :param valor_relleno: El valor para rellenar valores faltantes (usado si el método es 'rellenar').
    :return: El DataFrame con valores faltantes manejados.
    """
    if metodo == 'eliminar':
        df = df.dropna()
    elif metodo == 'rellenar':
        df = df.fillna(valor_relleno)
    return df

def generar_estadisticas(df):
    """Generar estadísticas básicas."""
    return df.describe()

def graficar_datos(df, columna_x, columna_y):
    """Crear un gráfico de dispersión interactivo."""
    fig = px.scatter(df, x=columna_x, y=columna_y, title=f'Gráfico de {columna_y} vs {columna_x}')
    fig.write_image("grafico.png")  # Guarda el gráfico como PNG
    fig.show()

if __name__ == "__main__":
    ruta_archivo = r'd:\pruebas\CSV DATA ANALYZER\Lista-de-clientes-con-nombre-y-direccion.xls'
    df = leer_excel(ruta_archivo)

    print("Nombres de las columnas:", df.columns)

    df = manejar_valores_faltantes(df, metodo='rellenar', valor_relleno=0)

    print("Resumen de Datos:")
    print(generar_estadisticas(df))

    # Reemplaza 'columna1' y 'columna2' con los nombres reales de las columnas
    # graficar_datos(df, 'columna1', 'columna2')