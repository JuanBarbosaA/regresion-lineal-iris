import numpy as np
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# 1. Cargar dataset
iris = datasets.load_iris()
X = iris.data  # ancho sépalo, largo sépalo, ancho pétalo, largo pétalo
y = iris.target  # 0=setosa, 1=versicolor, 2=virginica

# 2. Dividir datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Entrenar modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Función para predecir flor
def predecir_flor(ancho_sepalo, largo_sepalo, ancho_petalo, largo_petalo):
    entrada = np.array([[ancho_sepalo, largo_sepalo, ancho_petalo, largo_petalo]])
    pred = np.rint(model.predict(entrada)).astype(int)
    pred = np.clip(pred, 0, 2)  # asegurar que quede entre 0 y 2
    return iris.target_names[pred[0]]

# Ejemplo: pedir datos al usuario
print("Clasificación de flores Iris 🌸")
ancho_sepalo = float(input("Ingrese el ancho del sépalo: "))
largo_sepalo = float(input("Ingrese el largo del sépalo: "))
ancho_petalo = float(input("Ingrese el ancho del pétalo: "))
largo_petalo = float(input("Ingrese el largo del pétalo: "))

resultado = predecir_flor(ancho_sepalo, largo_sepalo, ancho_petalo, largo_petalo)
print(f"La flor predicha es: {resultado}")