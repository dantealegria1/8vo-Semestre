## Imágenes Vectoriales vs Imágenes Reales

### **Imágenes Vectoriales**
Las imágenes vectoriales están basadas en **primitivas geométricas** que se definen mediante ecuaciones matemáticas.
#### **Primitivas**
- Puntos  
- Segmentos  
- Círculos  
- Polígonos  
- Estructuras geométricas  
### **Imágenes de Píxeles**
Las imágenes reales están compuestas por **píxeles**, que son pequeñas unidades de color organizadas en una cuadrícula.
#### **Mallado**
Un **mallado** es un conjunto de píxeles o una matriz de píxeles de tamaño $M \times N$.  
- Un **mallado en 3 dimensiones** es un **paralelepípedo**.  
- Un **boxcell** tiene **tres coordenadas** para su identificación y, además, requiere información sobre la **intensidad del píxel o el color**.
### **CAD (Computer-Aided Design)**
El diseño asistido por computadora (CAD) permite trabajar con imágenes vectoriales y realizar transformaciones como:
- **Escalamiento**  
- **Rotación**  
- **Traslación**
### Ejercicio

#### Vecindad de un pixel

¿Cuales son las coordenadas de los vecinos en las coordenadas (x,y)
$$\begin{vmatrix} (x-1,y-1) & (x-1,y) & (x-1,y+1)\\ (x,y-1) & (x,y) & (x,y+1) \\ (x+1,y-1)& (x+1,y) & (x+1,y+1) \end{vmatrix}$$
Cuales son los vectores asociados?
$$V_8(P){X}$$
----
# Espacio Métrico y Métrica

Un **espacio métrico** es un conjunto $X$ junto con una función $d: X \times X \to \mathbb{R}$ llamada **métrica**, que asigna a cada par de puntos $x, y \in X$ una distancia $d(x,y)$. Para que $d$ sea una métrica válida, debe cumplir:

1. **No negatividad**:  
    $d(x, y) \geq 0, \quad \forall x, y \in X$
2. **Identidad del indiscernible**:  
    $d(x, y) = 0 \iff x = y$
3. **Simetría**:  
    $d(x, y) = d(y, x), \quad \forall x, y \in X$
4. **Desigualdad triangular**:  
    $d(x, z) \leq d(x, y) + d(y, z), \quad \forall x, y, z \in X$
## Ejemplos de métricas comunes

- **Métrica euclidiana** en $\mathbb{R}^n$ (Distancia común en el espacio):  
    $d(x, y) = \sqrt{\sum_{i=1}^{n} (x_i - y_i)^2}$
- **Métrica del máximo** o **métrica infinito** (Solo importa la mayor diferencia entre coordenadas):  
    $d(x, y) = \max_{i} |x_i - y_i|$
- **Métrica Manhattan** o **métrica $L_1$** (Suma de las diferencias en cada coordenada):  
    $d(x, y) = \sum_{i=1}^{n} |x_i - y_i|$
- **Métrica discreta** (Solo distingue si los puntos son iguales o no):
    $d(x, y) = \begin{cases} 0, & \text{si } x = y \\ 1, & \text{si } x \neq y \end{cases}$

Cada métrica define una **topología** diferente en el espacio, afectando conceptos como continuidad, convergencia y compacidad.

### Para un ejercicio de vecindad de 8

Donde $d_e \leq \sqrt 2$
$$V_8(P) = {P | d_e(P_o,P) \leq \sqrt2}$$
$$V_8 (P_0) = P|d_{\inf}(P_0,P)\leq 1$$
## Distancia Manhattan
No puedo ir en diagonal, sino solo son movimientos horizontales y verticales

Ejercicio: Vecindad de tamaño 8 en $( \mathbb{R}^2 )$

Dado un punto $( P = (2,3) )$ en el plano, encuentra los 8 puntos más cercanos según diferentes métricas.
### 1. Usando la métrica euclidiana  

Es la distancia recta entre dos puntos $( (x_1, y_1) ) y ( (x_2, y_2) )$ es:  

$$d(P, Q) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$
Los 8 vecinos más cercanos son los puntos a una distancia de $( \sqrt{1} ) o ( \sqrt{2} )$:

$$[
(1,3), (3,3), (2,2), (2,4), (1,2), (1,4), (3,2), (3,4)
]$$
### 2. Usando la métrica Manhattan $(( L_1 ))$  

La distancia se define como:  

$$d(P, Q) = |x_2 - x_1| + |y_2 - y_1|$$

Los vecinos más cercanos son los puntos con distancia 1 (suma de diferencias en coordenadas igual a 1):

$$(1,3), (3,3), (2,2), (2,4)$$

Para completar 8 vecinos, tomamos los que están a distancia 2:

$$(1,2), (1,4), (3,2), (3,4)$$
### 3. Usando la métrica del máximo $(( L_\infty ))$  

La distancia es:

$$d(P, Q) = \max (|x_2 - x_1|, |y_2 - y_1|)$$

Aquí, los puntos con $( d(P, Q) \leq 1 )$ forman un cuadrado de lado 2:

$$(1,2), (1,3), (1,4), (2,2), (2,4), (3,2), (3,3), (3,4)$$
---
### Conclusión  

Cada métrica define una vecindad diferente:

- **Métrica euclidiana** genera vecinos en forma de círculo.
- **Métrica Manhattan** genera vecinos en forma de cruz.
- **Métrica del máximo** genera vecinos en forma de cuadrado.
---
## Conectividad

Si hablamos de **conectividad en una matriz de píxeles cuadrados**, nos referimos a cómo se define la vecindad de cada píxel y cómo determinamos si dos píxeles están conectados dentro de una imagen.

---
## **Tipos de Conectividad en una Matriz de Píxeles**

Dado un píxel en la posición (i,j)(i, j) dentro de una matriz, podemos definir su conectividad de distintas maneras:

### **1. Conectividad 4 (Vecindad de Von Neumann)**

Un píxel está conectado con sus 4 vecinos más cercanos en **direcciones ortogonales** (arriba, abajo, izquierda, derecha).

$\begin{array}{ccc} & (i-1, j) & \\ (i, j-1) & (i, j) & (i, j+1) \\ & (i+1, j) & \end{array}$

Ejemplo en una matriz:

```
  0  
0 X 0  
  0  
```

Aquí, el píxel XX está conectado solo con los 4 píxeles que lo rodean horizontal y verticalmente.

---
### **2. Conectividad 8 (Vecindad de Moore)**

Un píxel está conectado con sus 4 vecinos ortogonales **y también con los 4 en diagonal**.

$$\begin{array}{ccc} (i-1, j-1) & (i-1, j) & (i-1, j+1) \\ (i, j-1) & (i, j) & (i, j+1) \\ (i+1, j-1) & (i+1, j) & (i+1, j+1) \end{array}$$

Ejemplo en una matriz:

```
0 0 0  
0 X 0  
0 0 0  
```

Aquí, XX está conectado con los 8 píxeles que lo rodean.

---

### **3. Conectividad 6 (En hexágonos, solo como referencia)**

Si la matriz tuviera una estructura hexagonal en lugar de cuadrada, cada píxel tendría **6 vecinos** en una disposición tipo panal de abeja.

---
## **Ejemplo Práctico**

Supón que tenemos la siguiente matriz binaria donde `1` representa píxeles activados y `0` representa fondo:
```
0 0 0 0 0  
0 1 1 0 0  
0 1 0 1 0  
0 0 1 1 0  
0 0 0 0 0  
```
Si usamos **conectividad 4**, los grupos de `1`s forman dos regiones separadas.

Si usamos **conectividad 8**, todos los `1`s están conectados en una sola región.

---
## **Aplicaciones**

- **Visión por computadora**: Identificación de regiones en imágenes.
- **Segmentación de imágenes**: Separación de objetos en imágenes digitales.
- **Algoritmos de crecimiento de regiones**: Como el **flood fill** en editores de imágenes.

---

### **Conclusión**

La elección entre **conectividad 4** y **conectividad 8** afecta cómo se detectan objetos en una matriz de píxeles. Conectividad 4 es más estricta (solo vecinos ortogonales), mientras que conectividad 8 permite conexiones en diagonal. 🚀

Un **símplice** (o **simplejo**, aunque este último término es menos común) es una de las estructuras geométricas más básicas en la geometría y la topología. Es la generalización de un triángulo a dimensiones superiores

## Espacio metrico
$d: M \times M \rightarrow R$ son $x,y,z,M$. Se satisfacen las siguientes axiomas
1. $d(x,x) = 0$
2. Si $x\neq y \rightarrow d(x,y) > 0$
3. $d(x,y) = d(y,x)$ (Simetria)
4. $d(x,z) \leq d(x,y) + d(y,z)$ (desigualdad de triangulo)

### Camino
Bajo cierta vecindad que conecta Po con Pm un componente conectado bajo cierta vecidndad es aquel en el que hay al menos un camino que conecta cualquier par de pixeles en ese componente.

