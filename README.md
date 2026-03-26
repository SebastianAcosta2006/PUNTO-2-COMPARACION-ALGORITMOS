# PUNTO-2-COMPARACION-ALGORITMOS
En este ejercicio se implementó y comparó el rendimiento de dos algoritmos de análisis sintáctico:
<img width="1280" height="800" alt="COMPARACIONES DE ALGORITMOS DEFINITIVO" src="https://github.com/user-attachments/assets/0e698500-9908-47c9-bd50-8b0732e95bb2" />

El algoritmo CYK con complejidad O(n³)
Un parser predictivo LL(1) con complejidad O(n)![Uploading COMPARACIONES DE ALGORITMOS DEFINITIVO.png…]()


El objetivo principal es analizar experimentalmente la diferencia de rendimiento entre ambos algoritmos al procesar cadenas de diferentes tamaños y los 
demas objetivos eran 
Implementar el algoritmo CYK
Implementar un parser LL(1) basado en pila
Medir el tiempo de ejecución de ambos algoritmos
Comparar su comportamiento según el tamaño de la entrada

Tecnologías utilizadas
Lenguaje: Python 3
Sistema operativo: Ubuntu
Librerías:
time para medición de tiempos
random para la generacion de cadenas de prueba

Algoritmo CYK
El algoritmo CYK es un método de parsing basado en programación dinámica que permite determinar si una cadena pertenece a un lenguaje definido por una gramática libre de contexto

El parser LL es un analizador sintáctico predictivo que utiliza una pila y una tabla de parsing.
Funcionamiento general:
Inicializa una pila con el símbolo inicial
Compara entrada con el tope de la pila
Aplica reglas según una tabla
Acepta o rechaza la cadena
Metodología de comparación

Para comparar ambos algoritmos se realizó lo siguiente:

Se generaron cadenas aleatorias de distintos tamaños
Se ejecutó cada algoritmo con las mismas cadenas y despues con diferentes cadenas para hacer dos comparaciones 
Se midió el tiempo de ejecución usando time.time()
Se registraron los resultados en forma de tabla
<img width="1280" height="800" alt="COMPARACIONES DE ALGORITMOS" src="https://github.com/user-attachments/assets/1760cf3b-185e-43d1-96d2-f4e59a4ad8d6" />

