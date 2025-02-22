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
$$V_8(P){X}