import pandas as pd


class CSV_lector:
    def __init__(self, file_path):
        self.file_path = file_path
        self.datos = pd.read_csv(file_path)

    def primeras_lineas(self, n):
        return self.datos.head(n)

    def ultimas_lineas(self, n):
        return self.datos.tail(n)

    def aleatorio_lineas(self, n):
        return self.datos.sample(n)

    @property
    def nombres_columnas(self):
        return self.datos.columns.tolist()

    @property
    def tipos_datos_columnas(self):
        return self.datos.dtypes.tolist()

    @property
    def dimensiones(self):
        return self.datos.shape


csv_reader = CSV_lector('archivo.csv')

primeras_filas = csv_reader.primeras_lineas(5)
print("Primeras 5 filas:")
print(primeras_filas)

ultimas_filas = csv_reader.ultimas_lineas(5)
print("Últimas 5 filas:")
print(ultimas_filas)

aleatorias = csv_reader.aleatorio_lineas(3)
print("3 filas aleatorias:")
print(aleatorias)

column_names = csv_reader.nombres_columnas
print("Nombres de columnas:")
print(column_names)

data_types = csv_reader.tipos_datos_columnas
print("Tipos de datos de las columnas:")
print(data_types)

dimensions = csv_reader.dimensiones
print("Dimensiones del DataFrame:")
print(dimensions)








