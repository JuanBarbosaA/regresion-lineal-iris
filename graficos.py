import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
from sklearn.linear_model import LinearRegression

# 1. Cargar dataset Iris
iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = [iris.target_names[i] for i in iris.target]

#Gráficos
# 1. Dispersión pétalo (petal length vs petal width)
plt.figure(figsize=(8,6))
for species in df["species"].unique():
    subset = df[df["species"] == species]
    plt.scatter(subset["petal length (cm)"], subset["petal width (cm)"], label=species)
plt.title("Clasificación de Iris según pétalos")
plt.xlabel("Largo del pétalo (cm)")
plt.ylabel("Ancho del pétalo (cm)")
plt.legend()
plt.show()

# 2. Dispersión sépalo (sepal length vs sepal width)
plt.figure(figsize=(8,6))
for species in df["species"].unique():
    subset = df[df["species"] == species]
    plt.scatter(subset["sepal length (cm)"], subset["sepal width (cm)"], label=species)
plt.title("Clasificación de Iris según sépalos")
plt.xlabel("Largo del sépalo (cm)")
plt.ylabel("Ancho del sépalo (cm)")
plt.legend()
plt.show()

# 3. Mapa de calor de correlación
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", center=0)
plt.title("Matriz de correlación entre características")
plt.show()

# 4. Regresión lineal simple (petal length vs petal width con línea)
sns.lmplot(x="petal length (cm)", y="petal width (cm)", data=df, hue="species", height=6, aspect=1.2)
plt.title("Regresión lineal entre largo y ancho de pétalo")
plt.show()

# ------------------------------------------------------
# REGRESIÓN LINEAL SOBRE IRIS
# ------------------------------------------------------

# 5. Coeficientes del modelo
X = iris.data
y = iris.target
model = LinearRegression().fit(X, y)

plt.figure(figsize=(8,6))
coef = pd.Series(model.coef_, index=iris.feature_names)
coef.plot(kind="bar")
plt.title("Coeficientes de regresión lineal")
plt.ylabel("Peso del coeficiente")
plt.show()

# 6. Predicciones vs valores reales
y_pred = model.predict(X)
plt.figure(figsize=(8,6))
plt.scatter(y, y_pred, c="blue", alpha=0.6)
plt.plot([0,2],[0,2], "r--")  # línea ideal
plt.xlabel("Valores reales (clases)")
plt.ylabel("Predicciones (regresión lineal)")
plt.title("Predicciones vs valores reales")
plt.show()

