## 1. ¿Qué es la Optimización Multiobjetivo?

La optimización multiobjetivo (MOO) busca optimizar dos o más objetivos simultáneamente que suelen estar en conflicto. En lugar de una solución única, se obtiene un conjunto de soluciones de compromiso.

## 2. Fundamentos

###  Formulación

$$\min f(x) = [f_1(x), f_2(x), ..., f_k(x)]$$

- ( x ): vector de decisión
- ( X ): espacio de soluciones factibles
- ( f_i(x) ): funciones objetivo

## 3. Dominancia y Frente de Pareto

###  Dominancia de Pareto

Una solución **A** domina a **B** si:

- ( f_i(A) \leq f_i(B) ) para todo ( i )
- ( f_j(A) < f_j(B) ) para al menos un ( j )

###  Frente de Pareto

El conjunto de soluciones **no dominadas**. Representa los mejores compromisos entre los objetivos.

## 4. Tipos de Enfoques

### 4.1. Basados en Agregación

Convierte los objetivos en uno solo: $$F(x) = w_1 f_1(x) + w_2 f_2(x) + ... + w_k f_k(x)$$

- Simple pero no captura bien frentes no convexos
- Difícil de elegir los pesos adecuados

### 4.2. Basados en Pareto

Evalúan soluciones basadas en su dominancia, manteniendo una población de soluciones no dominadas.

### 4.3. Evolutivos (MOEAs)

Basados en algoritmos genéticos para la exploración global:

- **NSGA-II**
- **SPEA2**
- **MOEA/D**
- **MOPSO**

## 5. Enfoques Híbridos

### ¿Qué son?

Combinan diferentes estrategias (evolutivas, heurísticas, exactas, etc.) para mejorar los resultados.

### Tipos de Híbridos:

- **MOEA + Búsqueda Local**
- **Algoritmos clásicos + Metaheurísticas**
- **Multiobjetivo + Machine Learning**
- **Híbridos Determinístico-Evolutivos**

###  Ventajas:

- Mejor calidad de soluciones
- Más diversidad
- Mayor velocidad de convergencia

## 6. Algoritmos Multiobjetivo Populares

| Algoritmo    | Características                         |
| ------------ | --------------------------------------- |
| **NSGA-II**  | Dominancia, crowding distance, elitismo |
| **SPEA2**    | Archivo externo, densidad               |
| **MOEA/D**   | Divide el problema en subproblemas      |
| **MOPSO**    | Enjambre de partículas multiobjetivo    |
| **NSGA-III** | Especializado en más de 3 objetivos     |

## 7. Métricas de Evaluación

- **Hypervolume (HV)**: Volumen bajo el frente
- **Spread (Δ)**: Diversidad entre soluciones
- **Generational Distance (GD)**: Cercanía al frente ideal
- **IGD**: Inverted GD
- **Número de soluciones no dominadas**

## 8. Aplicaciones Reales

- Ingeniería (estructuras, mecánica)
- Finanzas (riesgo vs rendimiento)
- Machine Learning (precisión vs complejidad)
- Diseño de hardware/software
- Logística (costo vs tiempo)

## 9. Ejemplo Simple

| Solución | Tiempo (ms) | Energía (J) |
| -------- | ----------- | ----------- |
| A        | 10          | 80          |
| B        | 12          | 60          |
| C        | 11          | 70          |

- A **domina** a C
- A y B no se dominan ⇒ **Frente de Pareto** = {A, B}

## 10. NSGA-II en Detalle

NSGA-II (Non-dominated Sorting Genetic Algorithm II) es uno de los algoritmos evolutivos multiobjetivo más utilizados, desarrollado por Deb et al. en 2002.

### Características principales:

- **Fast Non-dominated Sorting**: Clasifica la población en diferentes frentes de no dominancia.
- **Crowding Distance**: Mantiene la diversidad dentro del mismo frente.
- **Elitismo**: Conserva las mejores soluciones encontradas.
- **Operador de Comparación**: Utiliza ranking + crowding distance.

### Funcionamiento del algoritmo:

1. **Inicialización**: Generar población inicial aleatoria P₀ de tamaño N.
2. **Crear población de descendientes**: Aplicar selección, cruce y mutación para generar Q₀.
3. **Proceso principal** (para cada generación t):
    - Combinar poblaciones: Rt = Pt ∪ Qt
    - Clasificar Rt en frentes de no dominancia: F = (F₁, F₂, ...)
    - Crear nueva población Pt+1 = ∅
    - Mientras |Pt+1| + |Fi| ≤ N:
        - Añadir Fi a Pt+1
    - Para el último frente a incluir (Fi):
        - Calcular crowding distance
        - Ordenar por crowding distance (descendente)
        - Añadir las mejores soluciones hasta completar N en Pt+1
    - Generar nueva población Qt+1 mediante selección, cruce y mutación
4. **Repetir** hasta alcanzar criterio de parada.

### Cálculo de Crowding Distance:

1. Inicializar distancia = 0 para todas las soluciones
2. Para cada objetivo m:
    - Ordenar soluciones según objetivo m
    - Asignar distancia infinita a soluciones extremas
    - Para soluciones intermedias:
        - Incrementar distancia basada en la diferencia normalizada entre vecinos

### Ventajas de NSGA-II:

- Complejidad computacional O(MN²) donde M=objetivos, N=tamaño población
- Preserva elitismo sin parámetros adicionales
- No requiere especificación de parámetros de sharing
- Equilibra convergencia y diversidad

### Limitaciones:

- Rendimiento degradado en problemas con muchos objetivos (>3)
- Puede tener dificultades con frentes discontinuos
- La crowding distance puede no ser óptima para mantener diversidad en todos los casos