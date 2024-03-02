from sklearn.linear_model import LinearRegression
from os import system as system

#Datos de entrenamiento:
X_train = [[1], [2], [3], [4], [5], [6], [7], [8]] #Kilometros

#Etiquetas
y_train = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000] #Metros

#Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

#Limpiar la consola
system("cls")
#Pedir el valor en kilómetros
km = int(input("Ingrese el valor en kilómetros: "))

#Realizar predicciones
km_to_convert = [[km]]
predicted_m = model.predict(km_to_convert)

#Imprimir el resultado
print(f"{km} kilómetros equivalen aproximadamente a {predicted_m[0]} metros")