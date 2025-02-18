### Conceptos biológicos
- Cromosomas
- Alelos
- Locus
- Genoma
- Genotipo
- Fenotipo
------------------------------------------------------------------------
## Algoritmos genéticos

Fueron desatollados por John Holland a principios de los 1960 motivado
por el aprendizaje de maquina

El *cromosoma* es una representación de una solución usualmente una cadena de bits binaria. A cada posición de la cadena se le denomina *gen* y al valor dentro de esa posición se le llama *alelo*

Genotipo -> cadena de cromosoma
Fenotipo -> Solución de problema
Adaptabilidad -> Valor de la solución
#### Características
- Son los mas utilizados
- Son robustos
- Utilizan dos espacios separados
	- De búsqueda (Genotipo)
	- De solución (Fenotipo)
- Los genotipos deben ser convertidos en fenotipos antes de evaluar la adaptación de cada solución
### Tipos de selección
- Ruleta
- Elitista
- Estado Estable
- Escalafón
### Operadores de cruce
- Cruce de un solo punto
- Cruce de dos puntos
### Mutación
Se escoge un pequeño numero de cromosomas al azar. En cada de estos se escoge un gen al azar y sobre este se cambia aleatoria mente un bit
- De un punto
- De varios puntos
- Mutación global
### Fitness
A cada solución (Cromosoma) se le asigna un valor dependiente que tan bueno es el cromosoma solucionando un problema
### Para aplicar el algoritmo genético se requieren 5 componentes
- Una representación de soluciones potenciales
- Una forma de crear una población inicial de soluciones
- Una función de evaluación que juegue el papel de ambiente clasificando soluciones en termino de aptitud
# EDAs (Estimation of Distribution Algorithms)

En los EDAs, primero generamos una población aleatoria. Para el problema **OneMax**, la siguiente generación se construye manteniendo, en cada alelo (_columna_), al menos el mismo porcentaje de **1s** que en la población anterior.

En este enfoque, no se aplican operadores tradicionales como mutación o cruce. En su lugar, la evolución se basa únicamente en la distribución de los valores dentro de la población