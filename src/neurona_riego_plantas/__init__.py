import numpy as np

X = np.array([[80,18],[70,22],[65,28],[55,25],[50,32],[40,30],[35,25],[30,32],[20,35],[10,38]], dtype=float)
y = np.array([[0],[0],[0],[0],[0],[1],[1],[1],[1],[1]], dtype=float)

# Normalización de las entradas

escala = np.array([100,50])
X_normalizado = X / escala

print("\nDatos normalizados: ")
print(X_normalizado)

# definir función de activación:

def sigmoide(z):
    return 1 / (1+np.exp(-z))

rng = np.random.default_rng(7)
pesos = rng.normal(size=(2,1))
sesgo = 0.0
tasa_aprendizaje = 0.5
epocas = 10000

for epoca in range(epocas):
    z= X_normalizado @ pesos + sesgo
    predicciones = sigmoide(z)

    #Calculo del error
    error = predicciones -y
    gradiente_z = 2 * error * predicciones * (1-predicciones) / len(X)
    gradiente_pesos = X_normalizado.T @ gradiente_z
    gradiente_sesgo = np.sum(gradiente_z)

    pesos -= tasa_aprendizaje * gradiente_pesos
    sesgo -= tasa_aprendizaje * gradiente_sesgo


    if epoca % 2000 == 0:
        perdida = np.mean(error**2)
        print(f"Epoca{epoca:5d} | error: {perdida:.6f}")
        
print("\n Pesos aprendidos: ", pesos.ravel())
print("\n Sesgo aprendido", sesgo )

probabilidad = sigmoide (X_normalizado @ pesos + sesgo)
respuesta = (probabilidad >= 0.5).astype(int)

print ("\n Resultados de los datos entrenados: ")
for entrada, probabilidad, respuesta in zip (X, probabilidad.ravel(), respuesta.ravel()):
    print(f"Humedad: {entrada[0]:.0f}% |"f"Temperatura:{entrada[1]:.0f}°C |"f"Probabilidad: {probabilidad:.3f}|"f"Respuesta: {respuesta}")

error_final = np.mean((probabilidad - y )**2)
print ("\n Error final: ")
print (f"{error_final :.6f}")

correctas = np.sum(respuesta == y)
print (f"\n Respuestas correctas:"f"{correctas}/10")


print("\n")
print("Pruebas con condiciones nuevas")

nuevos_datos = np.array([[75,30],[45,34],[25,22],[50,25],[30,40]], dtype=float)

nuevos_normalizados = nuevos_datos / escala

probabilidades_nuevas = sigmoide(nuevos_normalizados @ pesos + sesgo)

respuestas_nuevas = (probabilidades_nuevas >= 0.5 ).astype(int)

for entrada, probabilidad, respuesta in zip (nuevos_datos, probabilidades_nuevas.ravel(),respuestas_nuevas.ravel()):
    if respuesta ==1:
        decision = "REGAR"
    else: decision = "NO REGAR"

    print(f"Humedad:{entrada[0]:.0f}%|" f"Temperatura: {entrada[1]:.0f}°C |" f"Probabilidad:{probabilidad :.3f} | " f"Decision{decision}")
    
