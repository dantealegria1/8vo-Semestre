# Metacaracteres y Comodines en UNIX

Los **comodines** permiten hacer referencia a múltiples nombres de archivos y simplificar operaciones al trabajar con archivos en UNIX. Los nombres de archivos solo permiten **caracteres** específicos y pueden manipularse mediante estos metacaracteres:

### 🛠️ **Comodines Comunes**

|Comodín|Descripción|Ejemplo|
|---|---|---|
|`?`|Sustituye un único carácter en la posición donde se encuentra.|`ls a?c.txt` → Coincide con `abc.txt`, `adc.txt`, etc.|
|`*`|Sustituye cualquier combinación de caracteres (incluyendo vacío) desde esa posición.|`ls *.txt` → Coincide con `abc.txt`, `test.txt`, etc.|
|`[abcd...z]`|Sustituye un solo carácter tomando como referencia el conjunto de caracteres especificado.|`ls a[bc]d.txt` → Coincide con `abd.txt`, `acd.txt` pero no `aad.txt`|

---

## 🔄 **Manejo de Procesos y Órdenes Asociadas**

### ➡️ **Conexiones**

- **Pipe (`|`)** – Permite redirigir la salida de un comando como entrada para otro.

**Ejemplo**

```bash
cat /etc/passwd | wc
```

- `cat` → Muestra el contenido del archivo.
- `|` → Redirige la salida al siguiente comando.
- `wc` → Cuenta el número de líneas, palabras y caracteres.

### 📤 **Redirecciones**

Permiten redirigir la entrada y salida de comandos hacia archivos o dispositivos específicos:

|Tipo|Descripción|Ejemplo|
|---|---|---|
|**De dispositivo**|Redirige la salida a un dispositivo físico.|`echo "Hola" > /dev/tty`|
|**De archivo**|Guarda la salida en un archivo.|`echo "Hola" > archivo.txt`|
|**De terminal**|Redirige la entrada desde o hacia una terminal.|`cat < archivo.txt`|

---

## 🔐 **Seguridad en UNIX**

### 🗂️ **Permisos de Archivos**

Los permisos de archivo en UNIX están divididos en tres categorías:

|Tipo de Usuario|Permisos|Descripción|
|---|---|---|
|**Usuario (dueño)**|`r` `w` `x`|Lectura, escritura y ejecución.|
|**Grupo (dueño)**|`r` `w` `x`|Permisos aplicados a los miembros del grupo.|
|**Otros (resto del mundo)**|`r` `w` `x`|Permisos para todos los demás usuarios.|

### 🏷️ **Tipos de Archivos**

|Símbolo|Tipo|Descripción|
|---|---|---|
|`-`|Archivo normal|Archivo regular.|
|`d`|Directorio|Carpeta que contiene archivos o subdirectorios.|
|`c`|Dispositivo de caracteres|Entrada/salida de dispositivos basada en caracteres (ejemplo: teclado).|
|`b`|Dispositivo de bloques|Entrada/salida de dispositivos basada en bloques (ejemplo: disco duro).|
|`s`|Socket|Punto de comunicación para procesos.|
|`l`|Enlace simbólico (soft link)|Referencia a otro archivo o directorio.|

### 🔗 **Tipos de Enlaces**

- **Enlace duro (hard link)** → Apunta directamente al i-nodo del archivo.
- **Enlace simbólico (soft link)** → Apunta al nombre de otro archivo (como un acceso directo).

---

✅ **Ejemplo de permisos:**

```bash
ls -l archivo.txt
```

Salida:

```
-rw-r--r--  1 usuario grupo 1048 mar 20 10:34 archivo.txt
```

**Significado**:

- `-rw-r--r--` → Permisos para usuario, grupo y otros.
    - `r` → Lectura
    - `w` → Escritura
    - `x` → Ejecución
- `1` → Número de enlaces al archivo.
- `usuario` → Propietario del archivo.
- `grupo` → Grupo asociado al archivo.
- `1048` → Tamaño en bytes.
- `mar 20 10:34` → Fecha y hora de modificación.

---

🔎 **Consejo:** Usa `chmod`, `chown` y `chgrp` para gestionar permisos y propietarios.

Aquí tienes un apunte más completo y estructurado sobre **scripts en Shell** con explicaciones claras y ejemplos:  

---

# **Introducción a los Scripts en Shell**  

Un **script en Shell** es un archivo de texto que contiene una serie de comandos que se ejecutan en un intérprete de comandos, como **Bash**. Se utilizan para automatizar tareas en sistemas Linux y Unix.

## **1. Creación y Edición de un Script**  

Para crear y editar un script en Bash, podemos usar editores de texto como:  
- `nano` (simple y fácil de usar)  
- `vim` / `nvim` (más avanzado)  
- `emacs` (potente y configurable)  

Ejemplo usando `nvim`:  

```sh
nvim suma.sh
```

## **2. Estructura Básica de un Script**  

### **Encabezado: Shebang (`#!`)**
El **shebang** indica qué intérprete se usará para ejecutar el script. Para Bash:  

```sh
#!/bin/bash
```

### **Metadatos del Script**  
Añadir comentarios ayuda a documentar el código:  

```sh
# Nombre: suma.sh
# Autor: [Tu Nombre]
# Descripción: Script en Bash que solicita dos números y muestra su suma.
# Fecha: [DD/MM/AAAA]
# Uso: ./suma.sh
```

---

## **3. Código del Script: Sumar Dos Números**
Ejemplo de un script interactivo que solicita dos números al usuario y los suma:

```sh
#!/bin/bash

# Script que suma dos números ingresados por el usuario

# Pedir al usuario que ingrese dos números
read -p "Ingrese el primer número: " num1
read -p "Ingrese el segundo número: " num2

# Calcular la suma
suma=$((num1 + num2))

# Mostrar el resultado
echo "La suma de $num1 y $num2 es: $suma"
```

---

## **4. Hacer el Script Ejecutable**
Antes de ejecutar el script, es necesario darle permisos de ejecución:  

```sh
chmod +x suma.sh
```

## **5. Ejecutar el Script**  
Para ejecutarlo, usamos:  

```sh
./suma.sh
```

---

## **6. Mejoras y Funcionalidades Extras**
Para hacer el script más robusto, agregamos validación de entrada y mensajes de error:

```sh
#!/bin/bash

# Script mejorado que suma dos números con validación

# Función para validar si la entrada es un número
es_numero() {
  [[ $1 =~ ^-?[0-9]+$ ]]
}

# Solicitar números al usuario con validación
while true; do
  read -p "Ingrese el primer número: " num1
  es_numero "$num1" && break
  echo "❌ Error: Ingrese un número válido."
done

while true; do
  read -p "Ingrese el segundo número: " num2
  es_numero "$num2" && break
  echo "❌ Error: Ingrese un número válido."
done

# Calcular la suma y mostrar el resultado
suma=$((num1 + num2))
echo "✅ La suma de $num1 y $num2 es: $suma"
```

---

# Unidad II: Consolidación y Virtualización  

## 1. Infraestructura  

La infraestructura tecnológica se compone de varios elementos esenciales que permiten la consolidación y virtualización de recursos.  

### 🖥️ **Servicios**  
Los servicios de infraestructura se dividen en tres categorías principales:  

- **Poder de Cómputo**: Capacidad de procesamiento disponible.  
- **Almacenamiento**: Espacios y sistemas para guardar información (**NAS/DAS, block storage**).  
- **Redes de Comunicaciones**: Sistemas que permiten la interconectividad entre servidores y clientes.  

### 🏗️ **Hardware**  
- **Servidores**: Máquinas físicas o virtualizadas que ejecutan procesos y servicios.  

### 🔍 **¿Cómo se adquiere?**  
La administración de infraestructura es responsabilidad de roles especializados como:  

- **SysAdmin** (Administrador de Sistemas)  
- **SysOp** (Operador de Sistemas)  

## 2. Poder de Cómputo  

El poder de cómputo define la capacidad de procesamiento de una infraestructura.  

### ⚙️ **Componentes Claves**  
- **Procesadores** – *Arquitectura ISC (Instruction Set Computing)*  
- **Núcleos** – Cantidad de núcleos físicos y lógicos por procesador.  
- **Velocidad** – Medida en GHz, indica la rapidez del procesamiento.  

### 📊 **Métricas de Desempeño**  
Las siguientes métricas evalúan la eficiencia y potencia de procesamiento:  
- **MIPS** – *Millones de Instrucciones por Segundo*.  
- **FLOPS** – *Operaciones de Punto Flotante por Segundo*, clave en cálculos científicos.  
- **TOPS** – *Tera Operaciones por Segundo*, relevante en IA y ML.  

### 🎮 **Aceleradores de Procesamiento**  
- **GPUs** – Procesamiento paralelo optimizado para gráficos y cálculos masivos.  
- **NPUs** – *Neural Processing Units*, especializadas en tareas de inteligencia artificial.  

## 3. Almacenamiento  

El almacenamiento puede clasificarse en función de su localización y redundancia.  

### 🏠 **Almacenamiento Local**  
- **No Seguro** – Sin redundancia, vulnerable a fallos.  
- **Seguro (con réplicas)** – Uso de **RAID** (*Redundant Array of Independent Disks*).  

### ☁️ **Almacenamiento Remoto**  
- **Discos – SAN (Storage Area Network)** – Almacenamiento en red de alta velocidad.  
- **Directorios – NAS (Network Attached Storage)** – Servidores de almacenamiento accesibles por red.  

### 🔗 **Almacenamiento Distribuido**  
- Repartición de datos en múltiples nodos para alta disponibilidad y tolerancia a fallos.  

## Infraestructura  

La infraestructura tecnológica se compone de varios elementos esenciales que permiten la consolidación y virtualización de recursos.  

### Como se adquiere

Tengo varias operaciones
- Lo rento (fisicamente o virtualmente en la nube)
- Lo compro (fisicamente)

### 🖥️ **Servicios**  
Los servicios de infraestructura se dividen en tres categorías principales:  

- **Poder de Cómputo**: Capacidad de procesamiento disponible.  
- **Almacenamiento**: Espacios y sistemas para guardar información (**NAS/DAS, block storage**).  
- **Redes de Comunicaciones**: Sistemas que permiten la interconectividad entre servidores y clientes.  

### 🏗️ **Hardware**  
- **Servidores**: Máquinas físicas o virtualizadas que ejecutan procesos y servicios.  

### 🔍 **¿Cómo se adquiere?**  
La administración de infraestructura es responsabilidad de roles especializados como:  

- **SysAdmin** (Administrador de Sistemas)  
- **SysOp** (Operador de Sistemas)  

## Poder de Cómputo  

El poder de cómputo define la capacidad de procesamiento de una infraestructura.  

### ⚙️ **Componentes Claves**  
- **Procesadores** – *Arquitectura ISC (Instruction Set Computing)*  
- **Núcleos** – Cantidad de núcleos físicos y lógicos por procesador.  
- **Velocidad** – Medida en GHz, indica la rapidez del procesamiento.  

### 📊 **Métricas de Desempeño**  
Las siguientes métricas evalúan la eficiencia y potencia de procesamiento:  
- **MIPS** – *Millones de Instrucciones por Segundo*.  
- **FLOPS** – *Operaciones de Punto Flotante por Segundo*, clave en cálculos científicos.  
- **TOPS** – *Tera Operaciones por Segundo*, relevante en IA y ML.  

### 🎮 **Aceleradores de Procesamiento**  
- **GPUs** – Procesamiento paralelo optimizado para gráficos y cálculos masivos.  
- **NPUs** – *Neural Processing Units*, especializadas en tareas de inteligencia artificial.  

## 3. Almacenamiento  

El almacenamiento puede clasificarse en función de su localización y redundancia.  

### 🏠 **Almacenamiento Local**  
- **No Seguro** – Sin redundancia, vulnerable a fallos.  
- **Seguro (con réplicas)** – Uso de **RAID** (*Redundant Array of Independent Disks*).  

### ☁️ **Almacenamiento Remoto**  
- **Discos – SAN (Storage Area Network)** – Almacenamiento en red de alta velocidad.  
- **Directorios – NAS (Network Attached Storage)** – Servidores de almacenamiento accesibles por red.  

### 🔗 **Almacenamiento Distribuido**  
- Repartición de datos en múltiples nodos para alta disponibilidad y tolerancia a fallos.  

