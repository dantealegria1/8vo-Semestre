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

Invariante: Cantidades que no cambian a pesar de que se le apliquen transformaciones afines
### Transformaciones afines
- Traslacion
- Cambio de escala
- rotacion
![[Imagen de WhatsApp 2025-03-11 a las 10.16.01_cabe1b9f.jpg]]

### **Transformaciones afines**

Las transformaciones afines son operaciones que modifican una figura en un espacio (como un plano o el espacio tridimensional) mediante combinaciones de **movimientos lineales** y **traslaciones**. Las más comunes son:
### 1. **Traslación**

Consiste en **desplazar** una figura en una dirección específica sin cambiar su forma ni orientación.

Si un punto $P(x, y)$ se traslada por un vector $(t_x, t_y)$, las nuevas coordenadas $P'$ serán:
$$P' = (x + t_x, y + t_y)$$
✅ **Ejemplo:** Si $P(2, 3)$ se traslada por el vector $(1, -2)$, el nuevo punto es:
$$P' = (2 + 1, 3 - 2) = (3, 1)$$
### 2. **Cambio de escala**

Consiste en **agrandar o reducir** una figura mediante un factor de escala en cada eje.

Si un punto $P(x, y)$ se escala por factores $s_x$ y $s_y$ en los ejes $x$ y $y$ respectivamente, las nuevas coordenadas serán:
$$P' = (s_x \cdot x, s_y \cdot y)$$

✅ **Ejemplo:** Si P(2,3)P(2, 3) se escala por un factor de 2 en $x$ y 0.5 en $y$, el nuevo punto es:
$$P' = (2 \cdot 2, 0.5 \cdot 3) = (4, 1.5)$$
### 3. **Rotación**

Consiste en **girar** una figura alrededor de un punto (usualmente el origen) por un ángulo $\theta$.

Si un punto $P(x, y)$ se rota por un ángulo $\theta$ en sentido antihorario, las nuevas coordenadas serán:
$$P' = (x' , y') = (x \cdot \cos \theta - y \cdot \sin \theta, x \cdot \sin \theta + y \cdot \cos \theta)$$

✅ **Ejemplo:** Si $P(1,0)$ se rota 90° ($180=π \ 90 = \frac{\pi}{2}$):
$$P' = (1 \cdot \cos \frac{\pi}{2} - 0 \cdot \sin \frac{\pi}{2}, 1 \cdot \sin \frac{\pi}{2} + 0 \cdot \cos \frac{\pi}{2}) \ P' = (0, 1)$$
#### Rotaciones en 3D

Sacar angulos de euler
En 2D: La rotación en 2D se expresa mediante una multiplicación de matrices:
$$\begin{bmatrix} x' \\ y' \end{bmatrix} = \begin{bmatrix} \cos{\theta} & -\sin{\theta} \\ \sin{\theta} & \cos{\theta} \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}$$
La matriz de rotación en 2D puede escribirse en términos de vectores unitarios:
$$\begin{bmatrix} \hat{i}' \cdot \hat{i} & \hat{i}' \cdot \hat{j} \\ \hat{j}' \cdot \hat{i} & \hat{j}' \cdot \hat{j} \end{bmatrix}$$
donde:
- $\hat{i}' y \ \hat{j}'$ son los vectores unitarios rotados.
- Los productos escalares entre estos vectores forman los elementos de la matriz de rotación.
## Chain Code y sus Variantes

### 1. Chain Code

El **Chain Code** es una técnica de codificación utilizada en el procesamiento de imágenes para representar la forma de un contorno mediante una secuencia de direcciones discretas. Se utiliza principalmente en el análisis de bordes y reconocimiento de patrones.

La idea principal es recorrer un contorno siguiendo una dirección específica y almacenando los cambios direccionales en una cadena de códigos numéricos.

---

### 2. Three Orthogonal Direction Chain Code (3OT)

Este método restringe los movimientos a **tres direcciones ortogonales**:

- **0** → Derecha
    
- **1** → Arriba
    
- **2** → Izquierda
    

Se usa en aplicaciones donde la reducción de datos es prioritaria y el contorno puede representarse con menos direcciones.

**Ejemplo:** Si un contorno se mueve de manera escalonada en una forma de "L", la secuencia podría ser:

```
0 → 0 → 1 → 1 → 2 → 2
```

---

### 3. Freeman Chain Code de Ocho ηpq​=M00γ​Mpq​​2Direcciones (8-direcciones)

El **Freeman Chain Code** es una variante más detallada que permite representar movimientos en **ocho direcciones**:

```
  3  2  1
  4  P  0
  5  6  7
```

Donde:

- **0** → Derecha
    
- **1** → Diagonal arriba-derecha
    
- **2** → Arriba
    
- **3** → Diagonal arriba-izquierda
    
- **4** → Izquierda
    
- **5** → Diagonal abajo-izquierda
    
- **6** → Abajo
    
- **7** → Diagonal abajo-derecha
    

Este método es más preciso que el de tres direcciones y es ampliamente utilizado en análisis de imágenes y reconocimiento de patrones.

**Ejemplo:** Si el contorno se mueve en diagonal y luego recto:

```
1 → 2 → 3 → 4 → 5 → 6
```

---

## Conclusión

Cada método de **Chain Code** tiene sus ventajas:

- **3OT** es más compacto y fácil de procesar.
    
- **Freeman de 8 direcciones** ofrece mayor precisión en la representación de contornos.
    

Su elección depende del nivel de detalle y eficiencia que se requiera en la aplicación específica.

## 1. Demostración Por Inducción: Relación entre Perímetro y Celdas

### Teorema a Demostrar

Para una figura compuesta por $m$ celdas cuadradas adyacentes, se cumple la relación:

$2P_c + L = 4m$

Donde:

- $P_c$ = Perímetro común (bordes compartidos entre celdas)
- $L$ = Perímetro libre (bordes que no son compartidos)
- $m$ = Número de celdas

### Caso Base

Para una celda individual ($m = 1$):

- $P_c = 0$ (no hay bordes compartidos)
- $L = 4$ (todos los bordes son libres)
- $m = 1$ (una sola celda)

Verificación: $2(0) + 4 = 4(1)$ ✓

### Hipótesis de Inducción

Asumimos que para $m$ celdas se cumple: $2P_c + L = 4m$

### Paso Inductivo

Para $m+1$ celdas:

- Al agregar una celda nueva, ocurre:
    - $P_c' = P_c + 1$ (aumenta el perímetro común)
    - $L' = L + 2$ (el perímetro libre aumenta en 2 unidades)
    - $m' = m + 1$ (una celda adicional)

Sustituyendo en la ecuación: $$2P_c' + L' = 2(P_c+1) + (L+2) = 2P_c + 2 + L + 2 = 2P_c + L + 4$$

Por hipótesis de inducción, sabemos que $2P_c + L = 4m$, por tanto: $$2P_c + L + 4 = 4m + 4 = 4(m+1)$$
Lo que demuestra que la relación se mantiene para $m+1$ celdas.
### Parámetros Adicionales

- $T = 3, 4, 6$ (posibles tipos de teselas o figuras)
- $l = 1$ (longitud unitaria de cada lado)

## 2. Codificación de Contornos

### Códigos de Cadena

Los códigos de cadena son representaciones numéricas del contorno de objetos en imágenes digitales.

#### Tipos de Códigos de Cadena:

1. **Código de Tres Direcciones Ortogonales (3OT)**
    - Utiliza tres direcciones para representar contornos
    - Más compacto que otros códigos pero con menor precisión
    - ![[Pasted image 20250408110030.png]]
    - ![[Pasted image 20250408110124.png]]
    - Cada dos se pone el numerito
2. F8
	- Recorre la cadena por el centro de los pixeles
	- Comienza con el pixel mas arriba a la izquierda
	- ![[Pasted image 20250408110507.png]]
	- ![[Pasted image 20250408110622.png]]
3. **Código de Cadena de Freeman de Ocho Direcciones (DFCCE → AF8)**
    - Utiliza 8 direcciones (0-7) para codificar el contorno
    - Mayor precisión en la representación
    - ![[Pasted image 20250408110708.png]]
    - Usa dos vectores para codificar
    - Recorre por el centro
    - ![[Pasted image 20250408110742.png]]
    - Ojo se comio el de la esquina inferior izquierda, el profe dice que esta mal, debio haber sido 0,0,4,2,2,0,0,4,2,2
4. F4
	- Comienza con el pixel que esta mas arriba a la izquierda
	- Recorre la cadena por las orillas de los pixeles
	- Usa un vector para codificar
	- ![[Pasted image 20250408105520.png]]
	- ![[Pasted image 20250408105627.png]]
5. VCC
	- Similar al F4 pero en lugar de usar un vector usa dos 
	- Si vemos la diferencia es que son menos numeros en la codificacion final
	- ![[Pasted image 20250408105752.png]]
	- ![[Pasted image 20250408105940.png]]
### Conjuntos Relevantes

- $F_4 = {0, 1, 2, 3}$ (Código de Freeman de 4 direcciones)
- $F_8 = {0, 1, 2, 3, 4, 5, 6, 7}$ (Código de Freeman de 8 direcciones)
- $PBT = {0, 1}$ (Posiblemente código binario)
- $VCC = {1, 2, 3}$ (Valores de conectividad)
## 3. Momentos en Imágenes

Los momentos son descriptores estadísticos utilizados para caracterizar la forma, tamaño y orientación de objetos en imágenes.

### Definiciones Básicas

- **Momento de orden $(p,q)$**: $M_{pq} = \iint x^p y^q \rho(x,y) \, dx \, dy$ Donde $\rho(x,y)$ es la función de densidad (intensidad de píxel)
- **Momento de orden cero $M_{00}$**: Representa el área del objeto

### Momentos Normalizados

Los momentos normalizados $\eta_{pq}$ son invariantes a la escala:

$$\eta_{pq} = \frac{M_{pq}}{M_{00}^{\gamma}}$$

Donde $\gamma = \frac{p+q+2}{2}$ para $p+q \geq 2$

### Valores Numéricos Observados

- $\eta_{01} = -15.42$
- $\eta_{01}' = -31.23$