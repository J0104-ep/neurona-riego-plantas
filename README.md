# Análisis de resultados

## 1. ¿Por qué es necesario normalizar las entradas antes de entrenar?

Es necesario normalizar las entradas porque la humedad y la temperatura tienen diferentes escalas de valores. Al normalizarlas, los datos quedan en valores más pequeños y similares, lo que facilita el entrenamiento de la neurona y permite que los pesos se actualicen de una mejor manera.

## 2. ¿En qué parte del código se usa `X_normalizado` y por qué se conserva también `X`?

`X_normalizado` se utiliza durante el entrenamiento de la neurona, especialmente para calcular la suma ponderada y actualizar los pesos.

También se conserva `X` porque contiene los valores originales de humedad y temperatura, los cuales son más fáciles de mostrar y entender en los resultados.

## 3. ¿Qué ocurrió al entrenar solo 100 épocas?

Al utilizar solamente 100 épocas, la neurona tiene menos oportunidades para ajustar sus pesos y aprender de los datos. Por esta razón, el aprendizaje puede ser insuficiente y el error puede ser mayor que cuando se utilizan más épocas.

## 4. ¿Entrenar durante más épocas siempre mejora significativamente el resultado?

No necesariamente. Aumentar el número de épocas permite realizar más actualizaciones de los pesos, pero después de cierto punto la mejora puede ser pequeña. Por esto, entrenar durante muchas más épocas no siempre significa obtener una mejora significativa en el resultado.

## 5. ¿Qué efecto tuvo usar una tasa de aprendizaje muy pequeña?

Una tasa de aprendizaje muy pequeña hace que los pesos cambien lentamente durante el entrenamiento. Por esta razón, la neurona necesita muchas más épocas para aprender y el proceso de entrenamiento se vuelve más lento.

## 6. ¿Qué efecto tuvo usar una tasa de aprendizaje alta o muy alta?

Una tasa de aprendizaje alta hace que los pesos cambien de una manera más rápida. Si la tasa es demasiado alta, los cambios pueden ser muy grandes y provocar un aprendizaje inestable, haciendo que el error no disminuya correctamente.

## 7. ¿Qué representa el signo del peso asociado a la humedad?

El peso de la humedad es negativo. Esto significa que, según los datos utilizados en este ejercicio, cuando aumenta la humedad, disminuye la probabilidad de que la neurona indique que se debe regar la planta.

## 8. ¿Qué representa el signo del peso asociado a la temperatura?

El peso de la temperatura es positivo. Esto significa que, según los datos del ejercicio, cuando aumenta la temperatura, aumenta la probabilidad de que la neurona indique que se debe regar la planta.

## 9. ¿Por qué se convierte la probabilidad en 0 o 1 usando un umbral?

La función sigmoide produce un valor entre 0 y 1 que representa una probabilidad. Para obtener una decisión sencilla, se utiliza un umbral. En este caso, si la probabilidad es mayor o igual a 0.5, la respuesta es 1 (REGAR); de lo contrario, la respuesta es 0 (NO REGAR).

## 10. ¿Qué limitaciones tendría este modelo para controlar el riego de una planta real?

El modelo tiene varias limitaciones porque solamente utiliza la humedad y la temperatura como entradas. Además, los datos utilizados en la actividad son didácticos y no representan recomendaciones reales para el riego de plantas.

Para utilizar un sistema de este tipo en una situación real sería necesario considerar más factores y utilizar datos reales de diferentes tipos de plantas y condiciones ambientales.