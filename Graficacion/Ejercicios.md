Pruebe que la distancia entre el punto $(x_1, y_1)$ y la recta $ax+by=c$ esta dada por $$d= \frac{ax_1+by_1-c}{\sqrt{a²+b^2}}$$
$$PQ = y_1-y_2$$
El punto $Q(x_1,y_2)$ se ubica en la recta $ax+by-c=0$ esta directamente debajo de P se satisface que $ax_1+by_1 -c=0$ 
Despejando $y_2$ :
$$y_2=\frac{c-ax}{b}=-\frac{ax_1-c}{b} \rightarrow PQ=y_1+\frac{ax_1-c}{b}$$
$$Como \ \cos\theta=\frac{d}{PQ} \rightarrow d=PQcos\theta$$
$$d=(y_1+\frac{ax_1+c}{b})\cos\theta$$
![[Drawing 2025-02-04 10.47.44.excalidraw]]

Tenemos $tan\theta=tan\alpha=m$ Como $ax+by-c=0 \rightarrow y=-\frac{a}{b}x+\frac{c}{b}$ 

### Ejercicio 1.2 apartado 3

¿Cuál de las aseveraciones que siguen es cierta para el siguiente sistema de ecuaciones?
3x - 2y = 8
4x + y = 7 
a) El sistema es inconsistente.
b) La solución es (-1, 2).
*c) La solución se encuentra sobre la recta x=2.*
d) Las ecuaciones son equivalentes 

![[Pasted image 20250204211617.png]]

En un zoológico hay aves de dos patas y bestias de cuatro patas. SI el zoológico contiene 60 cabezas y 200 patas ¿Cuantas aves y bestias viven en el?
$$x=\ aves$$
$$y=\ bestias$$
$$x+y=60$$
$$2x+4y=200$$
$$\left\lceil\begin{matrix}  1 & 1\\   2 & 4   \end{matrix}\right\rvert \left\rvert\begin{matrix}   60 \\ 200 \end{matrix}\right\rceil  $$
La solución seria $x=20 \ y \ y=40$  
### Ejercicio 
Este es el modelo de nuestro problema:
$$1x_1+3x_2+2x_3=25,000$$
$$1x_1+4x_2+1x_3=20,000$$
$$2x_1+5x_2+5x_3=55,000$$
Y nuestro sistema de operaciones queda así:
$$\left\lceil\begin{matrix}  1 & 3 & 2\\   1 & 4 & 1 \\ 2 &5 & 5  \end{matrix}\right\rvert \left\rvert\begin{matrix}   25,000 \\ 20,000 \\ 55,000 \end{matrix}\right\rceil  $$
Resolviéndolo:
$$\left\lceil\begin{matrix}  1 & 0 & 0\\   0 & 1 & -1 \\ 0 &0 & 0  \end{matrix}\right\rvert \left\rvert\begin{matrix}   40,000 \\ -5,000 \\ 0 \end{matrix}\right\rceil  $$
Se puede ver que no tiene solución
Se pudo determinar que $5,000 <= x_3 <=8,000$

Si los valores solo nos da 0 se le llama solución trivial
# Vectores y matrices

> Un *vector* de $N$ componentes es un conjunto ordenado de $N$ números escritos como $\begin{bmatrix} x_1 & x_2 & ... \end{bmatrix}$

> Una *matriz* $A$ de $mxn$ es un arreglo de números dispuestos en $m$ renglones y $n$ columnas $$A=\begin{bmatrix} a_{11} & a_{12} & ... & a_{1n} \\ a_{21} & a_{22} & ...& a_{2n} \\ a_{m1} & a_{m2} & ...& a_{mn}\end{bmatrix}$$

## Igualdad de matrices

Dos matrices son iguales si:
- Son del mismo tamaño
- Las componentes correspondientes son iguales

### Ejercicio
Sea $A$ y $B$ dos matrices de $m*n$ y sea $\alpha$ un escalar demostrar que $\alpha (A+B)$ = $\alpha A + \alpha B$ 

Una matriz $A$ de $mxn$ es un arreglo compuestos en $m$ renglones y $n$ columnas

Para demostrar la propiedad de la distributividad del producto escalar sobre la suma de matrices, es decir, demostrar que:
$$α(A+B)=αA+αB\alpha (A + B) = \alpha A + \alpha B$$

para cualesquiera matrices $A$,$BA$, $B$ de tamaño $m×nm \times n$ y cualquier escalar $α\alpha$, procedemos de la siguiente manera:

#### **Paso 1: Definir las matrices y la operación suma**

Sean $A = [a_{ij}]$ y $B = [b_{ij}]$ matrices de tamaño $m×nm \times n$. La suma de matrices $A+BA + B$ se define como:
$$(A+B)ij=aij+bij,para 1≤i≤m,1≤j≤n.(A + B)_{ij} = a_{ij} + b_{ij}, \quad \text{para } 1 \leq i \leq m, 1 \leq j \leq n$$

#### **Paso 2: Aplicar la multiplicación escalar**

Multiplicamos la matriz suma $A+BA + B$ por el escalar $α\alpha$ La definición de la multiplicación escalar en matrices establece que:
$$α(A+B)=[α(aij+bij)].\alpha (A + B) = \left[ \alpha (a_{ij} + b_{ij}) \right]$$
Por la distributividad del producto escalar sobre la suma de números reales:

$$α(aij+bij)=αaij+αbij.\alpha (a_{ij} + b_{ij}) = \alpha a_{ij} + \alpha b_{ij}$$
Por lo tanto,
$$α(A+B)=[αaij+αbij].\alpha (A + B) = \left[ \alpha a_{ij} + \alpha b_{ij} \right]$$

#### Teorema
Sean $A,B,C$ tres matrices de $mxn$ y sean $\alpha$ y $\beta$ dos escalares, entonces:
1. $A+0=A$ 
2. $0A=0$
3. $A+B=B+A$
4. $(A+B)+C = A+(B+C)$
5. $\alpha (A+B) ) \alpha A + \alpha B$
6. $1A = A$
7. $(\alpha + \beta) A = \alpha A + \beta A$

## Ejercicios
Calcule $a * b$  $$a = (2,-3,4,-36)\ y \ b = \begin{bmatrix} 1 \\2\\9\\3\end{bmatrix}$$ $2*1+(-3)(2)+0+(-6)(3) = 2-6+(-18) = 22$
Notación $\Sigma$ 
$$\sum_{i=M}^N a_i$$
Escriba la suma $S_8 = 1-2+3-4+5-6+7-8$
$$\sum_{i=1}^8 (-1)^{i+1} i$$
Sea $a=(a_1,a_2,...,a_n) \ b=(b_1,b_2,...,b_n)$
$ab =a_1b_1+a_2b_2+...a_nb_n$ = $$\sum_{i=1}^n a_ib_i$$  
Si tuvieramos una constante es$$C\sum_{i=1}^n a_ib_i$$
Sean ${a_n},{a_n}$ dos sucesiones reales y c un numero real entonces $$\sum_{k=m}^n ca_k = c\sum_{k=m}^n a_k$$ 
$$\sum_{k=m}^n (a_k+b_k) = \sum_{k=m}^n a_k + \sum_{k=m}^n n_k$$

Matrices y sistemas de ecuaciones lineales

Calcule $BA$ y $AB$ $$A = \begin{bmatrix} 1 & 2 \\-1& 4\end{bmatrix} \ y \ B=\begin{bmatrix} 3 & -2 \\3& 6\end{bmatrix}$$
Sea $A=[A_{ij}]$ una matriz de $m*n$ y sea $B = [B_{ij}]$ una matriz de $n*p$ producto de $A \ y \ B$ en una matriz $m*p$ $C=[C_{ij}]$ $$C_{ij} = (rengon \ i \ de \ A)+(columna \ j \ de \ B)$$   
Calculamos cada elemento:
$(AB)11=(1)(3)+(2)(3)=3+6=9$
$(AB)12=(1)(−2)+(2)(6)=−2+12=10$
$(AB)21=(−1)(3)+(4)(3)=−3+12=9$
$(AB)22=(−1)(−2)+(4)(6)=2+24=26$

Por lo tanto
$$AB = \begin{bmatrix} 9 & 10 \\ 9 & 26 \end{bmatrix}$$
Ahora calculamos BA:

$$BA = \begin{bmatrix} 3 & -2 \\ 3 & 6 \end{bmatrix} \times \begin{bmatrix} 1 & 2 \\ -1 & 4 \end{bmatrix}$$

Calculamos cada elemento:

- $(BA)11=(3)(1)+(−2)(−1)=3+2=5$
- $(BA)12=(3)(2)+(−2)(4)=6−8=−2$
- $(BA)21=(3)(1)+(6)(−1)=3−6=−3$
- $(BA)22=(3)(2)+(6)(4)=6+24=30$

Por lo tanto,

$$BA = \begin{bmatrix} 5 & -2 \\ -3 & 30 \end{bmatrix}$$
El producto de dos matrices $A \ y \ B$ se define de la siguiente manera:

Si $A$ es una matriz de tamaño $m×n$ y $B$ es una matriz de tamaño $n×p$ el resultado $C=AB$ será una matriz de tamaño $m×p$.

Cada entrada de la matriz resultante $C$ se calcula como el **producto escalar** entre una fila de $A$ y una columna de $B$:

$C_{ij} = A_{i1} B_{1j} + A_{i2} B_{2j} + \dots + A_{in} B_{nj}$

Es decir, el elemento en la fila $i$ y columna $j$ de $C$ se obtiene sumando los productos de los elementos correspondientes de la **fila $i$ de $A$** y la **columna $j$ de $B$$**

### **Matriz Inversa usando el Método de Gauss-Jordan**

Para encontrar la **matriz inversa** de una matriz AA usando **el método de Gauss-Jordan**, seguimos estos pasos:

1. **Construir la matriz aumentada** $[A∣I][A | I]$, donde I es la matriz identidad.
2. **Aplicar transformaciones elementales** para convertir A en la identidad I.
3. **El resultado** será $[I∣A−1][I | A^{-1}]$, donde el lado derecho será la matriz inversa $A−1A^{-1}$.
### **Ejemplo: Calcular la inversa de**
$$A = \begin{bmatrix} 2 & 3 \\ 1 & 4 \end{bmatrix}$$
#### **Paso 1: Formar la matriz aumentada**
$$\left[ \begin{array}{cc|cc} 2 & 3 & 1 & 0 \\ 1 & 4 & 0 & 1 \end{array} \right]$$
#### **Paso 2: Convertir la primera columna en una columna de pivotes**
Hacemos que el primer pivote (posición 1,1) sea **1** dividiendo la primera fila entre 2:
$$\left[ \begin{array}{cc|cc} 1 & \frac{3}{2} & \frac{1}{2} & 0 \\ 1 & 4 & 0 & 1 \end{array} \right]$$
Restamos la primera fila de la segunda para hacer **cero** el elemento (2,1):
$$\left[ \begin{array}{cc|cc} 1 & \frac{3}{2} & \frac{1}{2} & 0 \\ 0 & \frac{5}{2} & -\frac{1}{2} & 1 \end{array} \right]$$
#### **Paso 3: Convertir la segunda columna en una columna de pivotes**
Dividimos la segunda fila entre 52\frac{5}{2} para hacer que el pivote (2,2) sea **1**:
$$\left[ \begin{array}{cc|cc} 1 & \frac{3}{2} & \frac{1}{2} & 0 \\ 0 & 1 & -\frac{1}{5} & \frac{2}{5} \end{array} \right]$$
Sustituimos en la primera fila para hacer **cero** el elemento (1,2):
$$\left[ \begin{array}{cc|cc} 1 & 0 & \frac{4}{5} & -\frac{3}{5} \\ 0 & 1 & -\frac{1}{5} & \frac{2}{5} \end{array} \right]$$
#### **Paso 4: La parte derecha es la inversa**
$$A−1=A^{-1} = \begin{bmatrix} \frac{4}{5} & -\frac{3}{5} \\ -\frac{1}{5} & \frac{2}{5} \end{bmatrix}$$
## Magnitud y vectores
$$ |V| = \sqrt{a²+b²}$$
### Calcule las magnitudes y direcciones de los vectores

>La dirección se da respecto al eje x

$V=(2,2), V=(2,2\sqrt{3}), V=(-2\sqrt{3},2)$

1) $|V| = \sqrt{2²+2²} = \sqrt{8} = \sqrt{4*2} = \sqrt 4 \sqrt 2 = 2\sqrt 2$ Para sacar la dirección $\theta = tan^{-1}( \frac {y}{x}) = tan^{-1}( \frac {2}{2}) = 45$
2) $|V| = \sqrt{2²+(2\sqrt 3)²}=4$ Para sacar la dirección $\theta = tan^{-1}( \frac {y}{x}) = tan^{-1}( \frac {2\sqrt 3}{2}) = \sqrt 3$

### Suma de vectores
$U+V = (a_2+a_1,b_2+b_1)$
La suma de vectores forma un paralelogramo

```vega-lite 
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "width": 400,
  "height": 400,
  "layer": [
    {
      "mark": "line",
      "encoding": {
        "x": {"field": "x", "type": "quantitative"},
        "y": {"field": "y", "type": "quantitative"},
        "color": {"field": "vector", "type": "nominal"}
      },
      "data": {
        "values": [
          {"vector": "V1", "x": 0, "y": 0},
          {"vector": "V1", "x": 2, "y": 2},

          {"vector": "V2", "x": 0, "y": 0},
          {"vector": "V2", "x": -1, "y": 3},

          {"vector": "V1 (translated)", "x": -1, "y": 3},
          {"vector": "V1 (translated)", "x": 1, "y": 5},

          {"vector": "V2 (translated)", "x": 2, "y": 2},
          {"vector": "V2 (translated)", "x": 1, "y": 5},

          {"vector": "Sum V1 + V2", "x": 0, "y": 0},
          {"vector": "Sum V1 + V2", "x": 1, "y": 5}
        ]
      }
    }
  ]
}
```
### Desigualdad del triangulo
Establece que, para cualquier par de vectores u y v, se cumple la siguiente relación:
$$|U+V| \leq |U|+|V|$$
En términos geométricos, esta desigualdad refleja el hecho de que la longitud de un lado de un triángulo (en este caso, ∥u+v∥\| u + v \|∥u+v∥) **nunca es mayor que la suma de las longitudes de los otros dos lados** (∥u∥+∥v∥\| u \| + \| v \|∥u∥+∥v∥).

Si tienes dos vectores u y v, la suma u+v forma un tercer lado de un triángulo en el espacio. La desigualdad del triángulo nos dice que la distancia entre el inicio y el final del recorrido de los dos vectores no puede ser mayor que recorrer ambos por separado.

Para conseguir que un vector sea unitario se divide entre su magnitud

### Producto escalar y Angulo entre vectores
$$u*v=a_1a_2+b_1b_2$$
$$cos\theta = \frac{u*v}{|u||v|} \ siendo \ |v| \ la \ magnitud \ del \ vector \rightarrow \theta = cos^{-1}(\frac{u*v}{|u||v|})$$

Si $u=(a,b)$ demuestra que $|u| =1$ 
$$V = \frac{V}{|V|} = \frac{(a,b)}{|V|} \rightarrow |V| = \sqrt{a²+b2} \rightarrow \frac{V}{|V|} = \frac{(a,b)}{\sqrt{a²+b²}} = ( \frac{(a)}{\sqrt{a²+b²}} + \frac{(b)}{\sqrt{a²+b²}}) $$
$$|V|=\sqrt{(\frac{(a)}{\sqrt{a²+b²}})² + (\frac{(b)}{\sqrt{a²+b²}})²} = \sqrt{\frac{a²}{a²+b²} + \frac{b²}{a²+b²}} = \sqrt{\frac{a²+b²}{a²+b²}} = \sqrt 1 = 1$$
Dibuja el vector a) v-u b) u-v
```vega-lite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "data": {
    "values": [
      {"x": 0, "y": 0, "x2": 3, "y2": 4, "label": "u(3,4)", "color": "blue"},
      {"x": 0, "y": 0, "x2": 1, "y2": 2, "label": "v(1,2)", "color": "green"},
      {"x": 0, "y": 0, "x2": 2, "y2": 2, "label": "u - v(2,2)", "color": "red"}
    ]
  },
  "layer": [
    {
      "mark": {"type": "rule", "strokeWidth": 3},
      "encoding": {
        "x": {"field": "x", "type": "quantitative"},
        "y": {"field": "y", "type": "quantitative"},
        "x2": {"field": "x2"},
        "y2": {"field": "y2"},
        "color": {"field": "color", "type": "nominal"}
      }
    },
    {
      "mark": {"type": "text", "align": "left", "baseline": "middle", "dx": 5},
      "encoding": {
        "x": {"field": "x2", "type": "quantitative"},
        "y": {"field": "y2", "type": "quantitative"},
        "text": {"field": "label"},
        "color": {"field": "color", "type": "nominal"}
      }
    }
  ],
  "width": 400,
  "height": 400,
  "config": {
    "axis": {"grid": true, "domain": true, "ticks": true}
  }
}

```


> **Teorema** sean u y v dos vectores diferentes de 0 si $\rho$ es el angulo entre ellos entonces $$ cos \varphi = \frac{u*v}{|u||v|} $$ 
```vega-lite
 {
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "layer": [
    {
      "mark": {"type": "line", "strokeWidth": 2, "color": "red"},
      "encoding": {
        "x": {"field": "x", "type": "quantitative"},
        "y": {"field": "y", "type": "quantitative"}
      },
      "data": {
        "values": [
          {"x": 0, "y": 0},
          {"x": 3, "y": 1}
        ]
      }
    },
    {
      "mark": {"type": "line", "strokeWidth": 2, "color": "red"},
      "encoding": {
        "x": {"field": "x", "type": "quantitative"},
        "y": {"field": "y", "type": "quantitative"}
      },
      "data": {
        "values": [
          {"x": 0, "y": 0},
          {"x": 1, "y": 2}
        ]
      }
    },
    {
      "mark": {"type": "line", "strokeWidth": 2, "color": "red", "strokeDash": [5,5]},
      "encoding": {
        "x": {"field": "x", "type": "quantitative"},
        "y": {"field": "y", "type": "quantitative"}
      },
      "data": {
        "values": [
          {"x": 3, "y": 1},
          {"x": 1, "y": 2}
        ]
      }
    },
    {
      "mark": {"type": "text", "dx": -15, "dy": 15, "fontSize": 14},
      "encoding": {
        "x": {"value": 1},
        "y": {"value": 2},
        "text": {"value": "(a₂, b₂)"}
      }
    },
    {
      "mark": {"type": "text", "dx": 15, "dy": -15, "fontSize": 14},
      "encoding": {
        "x": {"value": 3},
        "y": {"value": 1},
        "text": {"value": "(a₁, b₁)"}
      }
    },
    {
      "mark": {"type": "text", "dx": 0, "dy": -15, "fontSize": 14},
      "encoding": {
        "x": {"value": 2},
        "y": {"value": 1.5},
        "text": {"value": "v - u"}
      }
    },
    {
      "mark": {"type": "text", "dx": 20, "dy": 0, "fontSize": 14},
      "encoding": {
        "x": {"value": 2},
        "y": {"value": 0.5},
        "text": {"value": "u"}
      }
    },
    {
      "mark": {"type": "text", "dx": -20, "dy": 0, "fontSize": 14},
      "encoding": {
        "x": {"value": 0.5},
        "y": {"value": 1},
        "text": {"value": "v"}
      }
    },
    {
      "mark": {"type": "text", "dx": -10, "dy": -10, "fontSize": 14},
      "encoding": {
        "x": {"value": 0},
        "y": {"value": 0},
        "text": {"value": "0"}
      }
    }
  ]
}

```
 $$|v-u|² = (v-u)*(v-u)=v*v-2u*v+u*u = |v|² - 2u*v+|u|²$$
Usando ley de cosenos

Encuentre el angulo entre los vectores
$$
\vec{u} = 2\hat{i} + 3\hat{j} = (2,3)
$$
$$
\vec{v} = -7\hat{i} - \hat{j} = (-7,-1)
$$
$$
\vec{u} \cdot \vec{v} = 2(-7) + 3(1) = -14 + 3 = -11
$$
$$
|\vec{u}| = \sqrt{2^2 + 3^2} = \sqrt{4 + 9} = \sqrt{13}
$$
$$
|\vec{v}| = \sqrt{(-7)^2 + 1^2} = \sqrt{49 + 1} = \sqrt{50} = 5\sqrt{2}
$$
$$
\therefore \cos \varphi = \frac{-11}{(\sqrt{13})(5\sqrt{2})} = \frac{-11}{5\sqrt{26}}
$$
 ### Producto escalar
 $$u*v=|u||v|cos \varphi$$

### Vectores ortogonales y paralelos 
 Ortogonales:
 Son aquellos cuyo producto escalar es igual a 0. osea que el angulo entre ellos es de 90 grados
 Paralelos:
 Uno es un escalar o muliplo de otro y el angulo entre ellos es de 0 o 180

## Ejercicio
Demuestre que si $\vec{v}=a\hat{i}+b\hat{j}\neq\vec{0}$, entonces": $\vec{u}=\left(\frac{a}{\sqrt{a^2+b^2}}\right)\hat{i}+\left(\frac{b}{\sqrt{a^2+b^2}}\right)\hat{j}$ es un vector unitario que tiene la misma dirección que $\vec{v}$
Para la demostración del módulo:
$$|\vec{v}|=\sqrt{a^2+b^2}$$
$$|\vec{u}|=\sqrt{\left(\frac{a}{\sqrt{a^2+b^2}}\right)^2+\left(\frac{b}{\sqrt{a^2+b^2}}\right)^2}=\sqrt{\frac{a^2}{a^2+b^2}+\frac{b^2}{a^2+b^2}}=\sqrt{\frac{a^2+b^2}{a^2+b^2}}=\sqrt{1}=1$$

Para demostrar que tienen la misma direccion recordemos que el vector unitario se saca $$\hat{\mathbf{v}} = \frac{\mathbf{v}}{\|\mathbf{v}\|} = \left( \frac{v_1}{\|\mathbf{v}\|}, \frac{v_2}{\|\mathbf{v}\|}, \dots, \frac{v_n}{\|\mathbf{v}\|} \right)
$$
Entonces: $$\hat{\mathbf{v}} = \frac{\mathbf{v}}{\|\mathbf{v}\|} = \frac{(a,b)}{\sqrt{a²+b²}} = \left( \frac{a}{\sqrt{a²+b²}}, \frac{b}{\sqrt{a²+b²}} \right)
$$
Aqui ya podemos ver que los vectores unitarios $v$ = al vector unitrio $u$ por lo tanto tienen la misma direccion

#### **Regla de la Mano Derecha en Producto Cruz (⃗A × ⃗B)**

Se usa para encontrar la dirección del **producto cruz** de dos vectores.
### **Pasos**:

1. Extiende la mano derecha con los **dedos apuntando en la dirección del primer vector** (**A**).
2. Gira los dedos hacia la dirección del segundo vector (**B**), como si hicieras un barrido desde **A** hasta **B**.
3. El **pulgar extendido** indica la dirección del vector resultante (**A × B**).


```vega-lite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "width": 400,
  "height": 400,
  "data": {
    "values": [
      {"x": 0, "y": 0, "z": 0, "u": 1, "v": 0, "w": 0, "name": "î (1,0,0)"},
      {"x": 0, "y": 0, "z": 0, "u": 0, "v": 1, "w": 0, "name": "ĵ (0,1,0)"},
      {"x": 0, "y": 0, "z": 0, "u": 0, "v": 0, "w": 1, "name": "k̂ (0,0,1)"}
    ]
  },
  "mark": {"type": "rule", "tooltip": true},
  "encoding": {
    "x": {"field": "x", "type": "quantitative", "scale": {"domain": [-1, 1]}},
    "y": {"field": "y", "type": "quantitative", "scale": {"domain": [-1, 1]}},
    "color": {"field": "name", "type": "nominal"},
    "tooltip": [
      {"field": "name", "type": "nominal"},
      {"field": "u", "type": "quantitative"},
      {"field": "v", "type": "quantitative"},
      {"field": "w", "type": "quantitative"}
    ]
  }
}

```

Saca el producto cruz de dos vetores sea $u=a_1+b_1+c_1$ y $v=a_2+b_2+c_2$
$$\vec{u}\times\vec{v}=\left|\begin{matrix} \hat{\imath} & \hat{\jmath} & \hat{k} \\ a_1 & b_1 & c_1 \\ a_2 & b_2 & c_2 \end{matrix}\right|=\hat{i}\begin{vmatrix} b_1 & c_1 \\ b_2 & c_2 \end{vmatrix}-\hat{j}\begin{vmatrix} a_1 & c_1 \\ a_2 & c_2 \end{vmatrix}+\hat{k}\begin{vmatrix} a_1 & b_1 \\ a_2 & b_2 \end{vmatrix}$$ $$=-\hat{i}(b_1c_2-b_2c_1)-\hat{j}(a_1c_2-a_2c_1)+\hat{k}(a_1b_2-a_2b_1)$$ $$=\hat{i}(b_1c_2-b_2c_1)+\hat{j}(a_2c_1-a_1c_2)+\hat{k}(a_1b_2-a_2b_1)$$ $$=(b_1c_2-b_2c_1)\hat{i}+(a_2c_1-a_1c_2)\hat{j}+(a_1b_2-a_2b_1)\hat{k}$$
Muestra que
$$ |\vec{u} \times\vec{v} |²=(u_1²+u_2²+u_3²)(v_1²+v_2²+v_3²)-(u_1v_1+u_2v_2+u_3v_3)²$$
$$\vec{u}\times\vec{v}=\left|\begin{matrix} \hat{\imath} & \hat{\jmath} & \hat{k} \\ u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \end{matrix}\right|=\hat{i}\begin{vmatrix} u_2 & u_3 \\ v_2 & v_3 \end{vmatrix}-\hat{j}\begin{vmatrix} u_1 & u_3 \\ v_1 & v_3 \end{vmatrix}+\hat{k}\begin{vmatrix} u_1 & u_2 \\ v_1 & v_2 \end{vmatrix}$$
$$=\vec{i}(u_2v_3 -v_2u_3)-j(u_1v_3-v_1u_3)+k(u_1v_2-v_1u_2)$$$$ |\vec{u} \times\vec{v} |²=(u_1²+u_2²+u_3²)(v_1²+v_2²+v_3²)-(u_1v_1+u_2v_2+u_3v_3)² = |\vec{u}|^2 |\vec{v}|² -(\vec{u}*\vec{v})$$
### Ecuaciones Valiosas
$$ |\vec{u} \times\vec{v} | =  |\vec{u}||\vec{v} |sen\theta $$$$\vec{u}*\vec{v} = |\vec{u} ||\vec{v} |cos\theta$$ 
# Vectores Dependientes vs Paralelos

### Vectores Dependientes

Dos o más vectores son **linealmente dependientes** si **uno de ellos se puede escribir como combinación lineal** de los otros.

📌 **Ejemplo:**  
Si v2=c⋅v1v2​=c⋅v1​ (con c≠0c=0), entonces v1v1​ y v2v2​ son dependientes.

- En un espacio de **dimensión 2 (ℝ²)**, dos vectores son dependientes si son **paralelos o colineales**.
    
- En **dimensión 3 (ℝ³)** o mayor, pueden ser dependientes sin ser paralelos si hay más vectores de los necesarios para generar el espacio.
    
### Vectores Paralelos

Dos vectores son **paralelos** si **uno es un múltiplo escalar del otro**.

- **Siempre son linealmente dependientes.**
    
- **Tienen la misma dirección o exactamente opuesta.**
    

📌 **Ejemplo en ℝ²:**  
Si v1=(2,3)v1​=(2,3) y v2=(4,6)v2​=(4,6), entonces:

v2=2⋅v1v2​=2⋅v1​  

✅ **Son paralelos** y también **dependientes**.

📌 **Ejemplo en ℝ³:**  
Si v1=(1,2,3)v1​=(1,2,3) y v2=(2,4,6)v2​=(2,4,6), también son **paralelos** y **dependientes**.

---

### Resumen

|Concepto|Definición|Ejemplo|
|---|---|---|
|**Dependientes**|Uno se puede escribir como combinación lineal de los otros.|En ℝ³, (1,0,0),(2,0,0),(3,0,0)(1,0,0),(2,0,0),(3,0,0) son dependientes pero no paralelos.|
|**Paralelos**|Uno es un múltiplo escalar del otro.|(1,2)(1,2) y (2,4)(2,4) son paralelos y dependientes.|

📌 **Todos los vectores paralelos son dependientes, pero no todos los dependientes son paralelos.** 🚀