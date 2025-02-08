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
