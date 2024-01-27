Algoritmos Genéticos Simples

Raúl Daniel García Ramón

Instituto de Investigaciones en Inteligencia Artificial. Universidad Veracruzana.

rauld.garcia95@gmail.com

Abstract. Los algoritmos genéticos son una línea de investigación de la inteligencia artificial, la cual se inspira en la evolución biológica, para a partir de una población de individuos evolucionarlos mediante una se- rie de acciones aleatorias, así como a un proceso de selección que de acuerdo a un criterio se decide que individuos son más aptos y sobre- viven, repitiéndose cierto número de generaciones o hasta alcanzar algún objetivo. En este trabajo la meta es minimizar dos funciones utilizando para cada una la representación mediante cadenas binarias y la repre- sentación real. Para finalmente realizar una comparativa de las diferentes representaciones para analizar sus ventajas y desventajas.

Keywords: Algoritmos Genéticos · Inteligencia Artificial · Computo Evolutivo

1  Introducción

Un algoritmo genético es una técnica para la resolución de problemas medi- ante una estrategia inspirada en la evolución biológica, la cual está basada en poblaciones, con una métrica llamada función de aptitud que permite evaluar a la población y ver cuál tiene características más adecuadas para el problema a resolver.

En este trabajo se busca minimizar las siguientes dos funciones, mediante el uso de la representación con cadenas binarias y con número reales para ambas funciones:

$f(\overrightarrow{x})= \sum_{i=1}^{D} x_{i}^{2} $

donde $D=10$, $-10\leq x_{i}\leq10$ con una precisión de 3 dígitos.

$f(\overrightarrow{x})= 10D+ \sum_{i=1}^{D} (x_{i}^{2} -10 cos(2\pi x_{i}))$

donde $D=10$, $-5.12 \leq x_{i}\leq 5.12$ con una precisión de 3 dígitos.

2  Implementación

Para la representación con cadenas binarias para números reales se utilizó la cruza uniforme, mutación por reordenamiento y selección universal estocástica, además el tamaño de la cadena para cada solución se calcula con la siguiente fórmula: $L=int[log_{2}[(l_{sup}-l_{inf})*10^{precision}]+0.9]$, mientras que el valor real de la cadena se calcula con esta fórmula: $x_{real}=l_{inf}+[\frac{x_{decodificada} *(l_{sup}-l_{inf})}{2^{L}-1}]$.
Para la representación real se utilizó la cruza SBX, con mutación uniforme y selección por torneo binario determinístico. En las dos representaciones se utilizó el elitismo, sustituyendo al peor hijo generado, por el mejor individuo de la población. Los parámetros utilizados para ambas representaciones es el siguiente: Tamaño de población de 100, 1500 generaciones, probabilidad de cruza de 50\%, probabilidad de mutación de 1\%, además de $\eta=2$ para la cruza SBX.

3  Resultados

Al realizar la parte experimental de este trabajo se pudo notar que para el primer problema era más sencillo para los algoritmos encontrar la solución, ya que no requerían un número muy grande de generaciones para converger a una buena solución, lo cual se puede notar en su gráfica de convergencia como en menos de 40000 evaluaciones ya está encontrando soluciones muy cercanas, esto se debe principalmente a que, como se ve en su gráfica 3D, la función no tiene mínimos locales que puedan hacer que la búsqueda se quede estancada. Por el contrario, para el segundo problema, como se puede ver en su gráfica 3D, esta función tiene varios mínimos locales, los cuales complican la búsqueda del mínimo global, esto a su vez se ve reflejado en las gráficas de convergencia donde a ambos algoritmos les toma mayor cantidad de generaciones encontrar soluciones aceptables.

En la parte de los algoritmos, se observó que la calibración de parámetros es un proceso laborioso, sobre todo con la representación binaria para el segundo problema, lo cual se puede ver reflejado en la tabla de estadísticas, ya que a pesar de que para los cuatro casos se logró encontrar el mínimo global en al menos una corrida, el algoritmo 1 con el problema 2 fue el que mayor desviación estándar obtuvo, lo cual a su vez se ve reflejado con las medias y medianas, donde para los otros 3 casos estos valores están cercanos al mínimo global.

Por otro lado, se realizó la prueba Wilcoxon rank-sum  con un 95\% de confianza, en busca de una diferencia significativa en los resultados obtenidos mediante ambas representaciones para cada problema, obteniendo un valor de $p=3.654x10^{-6}$ para la primera función, y $p=1.991x10^{-6}$ para la segunda función; con lo cual se concluye que hay una diferencia estadística significativa entre los resultados de ambas representaciones.

Finalmente, se puede concluir que de los 4 casos el que mejor resultados dio fue el binario para el problema 1, ya que siempre encontró el mínimo global, sin embargo, al comparar las dos representaciones, el algoritmo con número reales en general llego a resultados más cercanos al mínimo global para ambos problemas, además su calibración de parámetros fue más sencilla y su tiempo de ejecución es menor al binario.





<table><tr><th colspan="1">Población:</th><th colspan="1">100</th><th colspan="1">Generaciones:</th><th colspan="1">1500</th></tr>
<tr><td colspan="1">P. Cruza:</td><td colspan="1">0.7</td><td colspan="1">P. Muta</td><td colspan="1">0.01</td></tr>
<tr><td colspan="4"></td></tr>
<tr><td colspan="1" rowspan="2">Problema</td><td colspan="1" rowspan="2">Estadísticas</td><td colspan="2">Técnicas comparadas</td></tr>
<tr><td colspan="1">Algoritmo 1</td><td colspan="1">Algoritmo 2</td></tr>
<tr><td colspan="1" rowspan="5">Problema 1</td><td colspan="1">Mejor</td><td colspan="1">0</td><td colspan="1">0</td></tr>
<tr><td colspan="1">Media</td><td colspan="1">0</td><td colspan="1">0.0094</td></tr>
<tr><td colspan="1">Mediana</td><td colspan="1">0</td><td colspan="1">0.004</td></tr>
<tr><td colspan="1">Peor</td><td colspan="1">0</td><td colspan="1">0.059</td></tr>
<tr><td colspan="1">Desv. Est.</td><td colspan="1">0</td><td colspan="1">0.0112</td></tr>
<tr><td colspan="1" rowspan="5">Problema 2</td><td colspan="1">Mejor</td><td colspan="1">0</td><td colspan="1">0</td></tr>
<tr><td colspan="1">Media</td><td colspan="1">3.407</td><td colspan="1">0.931</td></tr>
<tr><td colspan="1">Mediana</td><td colspan="1">3.718</td><td colspan="1">0.599</td></tr>
<tr><td colspan="1">Peor</td><td colspan="1">7.707</td><td colspan="1">5.014</td></tr>
<tr><td colspan="1">Desv. Est.</td><td colspan="1">2.0291</td><td colspan="1">1.0578</td></tr>
</table>

![](Aspose.Words.e3f89892-6717-4f36-9507-8f077850d3dd.001.png) ![](Aspose.Words.e3f89892-6717-4f36-9507-8f077850d3dd.002.png)

![](Aspose.Words.e3f89892-6717-4f36-9507-8f077850d3dd.003.png) ![](Aspose.Words.e3f89892-6717-4f36-9507-8f077850d3dd.004.png)

![](Aspose.Words.e3f89892-6717-4f36-9507-8f077850d3dd.005.png) ![](Aspose.Words.e3f89892-6717-4f36-9507-8f077850d3dd.006.png)

![](Aspose.Words.e3f89892-6717-4f36-9507-8f077850d3dd.007.png) ![](Aspose.Words.e3f89892-6717-4f36-9507-8f077850d3dd.008.png)

Fig.1. Estadísticas y gráficas de convergencia de los algoritmos
