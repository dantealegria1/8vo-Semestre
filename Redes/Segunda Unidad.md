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

Aquí tienes un apunte más estructurado, con un diseño más claro y organizado para mejorar su comprensión.

---
# Hipervisores
Los **hipervisores** son la base de la virtualización, ya que permiten ejecutar múltiples sistemas operativos sobre un mismo hardware físico. Existen tres tipos principales:

---

## 🏗️ **1. Hipervisores Tipo 1 (Bare-metal)**

También llamados **hipervisores nativos** o **de tipo bare-metal**, se instalan **directamente sobre el hardware** sin necesidad de un sistema operativo intermedio.

### ✅ **Ventajas:**

✔️ Mayor rendimiento y eficiencia (sin capa intermedia)  
✔️ Mejor seguridad y aislamiento de VMs  
✔️ Adecuado para entornos empresariales y servidores

### ❌ **Desventajas:**

❌ Requiere hardware compatible  
❌ Más complejo de administrar

### 🔧 **Ejemplos:**

- **VMware ESXi**
    
- **Microsoft Hyper-V**
    
- **Xen**
    
- **KVM** (Kernel-based Virtual Machine)
    

📌 **Usos comunes:** Centros de datos, servidores de alto rendimiento, cloud computing (AWS, Azure, Google Cloud).

---

## 🖥️ **2. Hipervisores Tipo 2 (Hosted)**

Se instalan **sobre un sistema operativo** (Windows, Linux, macOS) y actúan como una aplicación que administra las máquinas virtuales.

### ✅ **Ventajas:**

✔️ Más fácil de instalar y usar  
✔️ No requiere hardware especial  
✔️ Adecuado para entornos de desarrollo y pruebas

### ❌ **Desventajas:**

❌ Menor rendimiento (depende del SO anfitrión)  
❌ Menos seguro que los hipervisores Tipo 1

### 🔧 **Ejemplos:**

- **VMware Workstation / Fusion**
    
- **Oracle VirtualBox**
    
- **Parallels Desktop**
    

📌 **Usos comunes:** Desarrollo, pruebas de software, máquinas virtuales personales.

---

## 🌐 **3. Hipervisores Basados en Contenedores**

No virtualizan hardware completo, sino que comparten el mismo kernel del sistema operativo y **usan espacios aislados** para ejecutar aplicaciones como si fueran máquinas virtuales ligeras.

### ✅ **Ventajas:**

✔️ Arranque rápido y menor uso de recursos  
✔️ Escalabilidad ideal para microservicios  
✔️ Mejor integración con entornos de CI/CD y DevOps

### ❌ **Desventajas:**

❌ Menos aislamiento que una VM tradicional  
❌ Dependen del sistema operativo base

### 🔧 **Ejemplos:**

- **Docker**
    
- **LXC (Linux Containers)**
    
- **Podman**
    
- **Kubernetes** (orquestación de contenedores)
    

📌 **Usos comunes:** Cloud computing, microservicios, despliegues escalables en entornos DevOps.

---

## 📌 **¿Cuál elegir?**

✅ **Tipo 1** → Servidores, entornos empresariales, cloud computing  
✅ **Tipo 2** → Uso personal, pruebas de software, desarrollo  
✅ **Contenedores** → Aplicaciones escalables, DevOps, microservicios

## 🌐 **Virtualización con Hipervisores de Categoría 1**

### 🖥️ **¿Por qué usar virtualización?**

#### 🔹 **1. Consolidación**

- Aprovechamiento eficiente del hardware
    
- Reducción del consumo energético
    
#### 🔹 **2. Tolerancia a fallos**

- **Alta Disponibilidad (H.A.)**: Minimiza el tiempo de inactividad
    
- Migración en caliente para evitar interrupciones
    
#### 🔹 **3. Escalabilidad**

- Ajuste dinámico de recursos según la demanda
    
#### 🔹 **4. Clusters**

- Agrupación de servidores para mayor eficiencia
    
- **Emulación** de múltiples tipos de dispositivos

#### 🔹 **5. Seguridad**

- Aislamiento de máquinas virtuales
    
- Reducción del impacto de vulnerabilidades  

---

### 📂 **Almacenamiento y Repositorios**

#### 🗄️ **Tipos de repositorios**

✅ **Local**: Almacenamiento en un solo servidor  
✅ **Remoto**: Servidores centralizados en la red  
✅ **Distribuido**: Repartido en múltiples nodos

#### 🔐 **Seguridad del almacenamiento**

⚠️ **Líneas inseguras** → Riesgo de interceptación  
☁️ **Cloud (inseguro)** → Riesgo de ataques y pérdida de control  
🛡️ **Almacenamiento seguro (lento pero fiable)**

---

### 🌍 **Infraestructura y Redes**

🔹 **Internet**  
🔹 **Red de almacenamiento (SAN, NAS)**  
🔹 **Discos locales**  
🔹 **Red de datos**

---

✨ **Notas adicionales:**

- La virtualización con hipervisores tipo 1 (bare-metal) ofrece mejor rendimiento y estabilidad.
    
- Es clave en entornos empresariales para optimizar costos y mejorar la resiliencia de la infraestructura TI.
    


# 📡 **Unidad 3: Capa de Servicios de Internet**

## 🔹 **1. Conceptos Básicos**

### 🏛 **Familia de protocolos de Internet (TCP/IP)**

El modelo TCP/IP permite la comunicación en Internet mediante una estructura organizada en capas.

📌 **Capas del Modelo TCP/IP:**

|Capa|Número|Función|
|---|---|---|
|**Aplicación**|7,6|Interacción con el usuario y servicios de red.|
|**Transporte**|4|Gestión de la comunicación entre dispositivos.|
|**Red**|3|Enrutamiento de paquetes entre redes.|
|**Enlace de Datos**|1,2|Manejo de frames y conexión física.|

🔹 **Principios clave:**  
✅ Una máquina **puede comunicarse siempre que se pueda enrutar** su tráfico.  
✅ Cada mensaje en la red se encapsula en **paquetes**.  
✅ La información viaja a través de un modelo llamado **datagrama**.

---

## 🔹 **2. Capa de Enlace de Datos**

📌 **Funciones:**

- Maneja los **frames o marcos de datos**.
    
- Controla la conexión entre dispositivos en la misma red.
    

📌 **Protocolos importantes:**

- **LLC (Logical Link Control)** → Control de flujo y direccionamiento lógico.
    
- **MAC (Media Access Control)** → Direccionamiento físico (direcciones MAC).
    

---

## 🔹 **3. Capa de Red**

📌 **Objetivo:**

- Crear "carreteras" para el tráfico de datos y definir la mejor ruta de los paquetes.
    

📌 **Protocolos clave:**

- **IP (Internet Protocol)** → Identificación y entrega de paquetes.
    
- **ICMP (Internet Control Message Protocol)** → "El chismoso", notifica errores en la red.
    
- **Protocolos de enrutamiento** → Encuentran la mejor ruta para enviar paquetes.
    
- **AIP (Addressing and Internetworking Protocols)** → Manejo de direcciones y redes.
    

---

## 🔹 **4. Capa de Transporte**

📌 **Función principal:**

- Facilitar la comunicación entre dispositivos gestionando la entrega de datos.
    

📌 **Protocolos más usados:**

|Protocolo|Características|
|---|---|
|**UDP (User Datagram Protocol)**|Rápido pero inseguro, no garantiza la entrega.|
|**TCP (Transmission Control Protocol)**|Más lento pero seguro, garantiza la entrega.|
|**RTP (Real-time Transport Protocol)**|Se usaba para multimedia, pero ha perdido relevancia.|
|**RSVP (Resource Reservation Protocol)**|Protocolo de reserva de recursos en la red.|

🔹 **UDP y TCP usan sockets para comunicarse.**

- **UDP** tiene **65,536 sockets**, cada aplicación usa los suyos.

# Servicios en la Capa de Usuarios

## Categorías de Servicios

### 1. Servicios Básicos

- **DNS (Domain Name Services)**
    
    - Sistema que traduce nombres de dominio a direcciones IP
    - Componente fundamental para la navegación web
    - Estructura jerárquica de resolución de nombres
    - Ejemplo: `https://www.google.com` → el DNS traduce "www.google.com" a una dirección IP
- **DHCP (Dynamic Host Configuration Protocol)**
    
    - Asigna automáticamente direcciones IP a dispositivos en una red
    - Administra también máscaras de subred, puerta de enlace y servidores DNS
    - Facilita la integración de nuevos dispositivos a la red
- **Proxys**
    
    - Intermediarios entre cliente y servidor
    - Tipos:
        - Socks: actúa como intermediario para conexiones TCP/UDP
        - NAT (Network Address Translation): permite compartir una dirección IP pública
- **VPNs (Virtual Private Networks)**
    
    - Crean conexiones seguras a través de redes públicas
    - Cifran el tráfico entre dispositivos
    - Permiten acceso remoto seguro a redes privadas

### 2. Servicios de Almacenamiento

- **No Transparentes**
    
    - El usuario debe conocer la ubicación y método de acceso
    - Mayor control pero requiere más conocimiento técnico
- **Transparentes**
    
    - El usuario accede sin necesidad de conocer detalles técnicos
    - Abstracción de la complejidad del sistema
- **Bases de Datos**
    
    - Almacenamiento estructurado de información
    - Sistemas de gestión para consulta y manipulación de datos

### 3. Sesiones Remotas

- **Texto [CLI - Command Line Interface]**
    
    - Interfaces de línea de comandos (SSH, Telnet)
    - Control remoto basado en texto
    - Eficientes para tareas administrativas
- **Gráficos [Remote Desktops]**
    
    - Interfaces gráficas remotas (RDP, VNC, TeamViewer)
    - Permiten visualizar y controlar escritorios remotos
    - Mayor facilidad de uso para usuarios no técnicos

### 4. Servicios de Información

- **Asíncronos**
    
    - No requieren conexión simultánea (correo electrónico, foros)
    - La comunicación ocurre en diferentes momentos temporales
    - Permiten flexibilidad temporal
- **Síncronos**
    
    - Requieren conexión simultánea (chat, videoconferencias)
    - Comunicación en tiempo real
    - Mayor inmediatez en la interacción

## Gobernanza de Internet

### NIC (Network Information Center)

- Centro de Información de la Red
- Funciones:
    - Gestión de direcciones IP
    - Administración de DNS
    - Coordinación de recursos de red a nivel regional/nacional

### IETF (Internet Engineering Task Force)

- Organismo encargado de la tecnología de internet
- Desarrolla y promueve estándares de internet
- Establece protocolos mediante documentos RFC (Request for Comments)
- Proceso de desarrollo:
    1. Identificación de una necesidad
    2. Propuesta de solución
    3. Desarrollo de protocolos/estándares
    4. Publicación como RFC
    5. Implementación y mejora continua

### Cronología Relevante

- **1995**: Comercialización de Internet (ISPs)
    - Surgimiento de proveedores de servicios de internet
    - Expansión de protocolos estándares y privados
    - Desarrollo de aplicaciones públicas y privadas

## Estructura Funcional

### Componentes del Ecosistema

- **Personas** → **Organizaciones**
    - Desarrollan y codifican aplicaciones
    - Establecen estándares y protocolos
    - Implementan servicios y servidores

### Estructura de URLs

- **Ejemplo**: `https://www.google.com`
    - Protocolo: `https://`
    - FQDN (Fully Qualified Domain Name): `www.google.com`
    - El DNS traduce el FQDN a direcciones IP
    - Las direcciones IP permiten la conectividad en internet

### Relación FQDN-DNS-IP

- FQDN ⟺ DNS ⟺ Direcciones IP
- El sistema DNS actúa como intermediario para traducir nombres legibles para humanos a direcciones numéricas que las máquinas pueden procesar

## Consideraciones Adicionales

### Capas de Red

- El modelo de capas facilita la comprensión de los servicios de red
- La capa de usuario representa la interfaz más cercana al usuario final
- Los servicios mencionados operan principalmente en las capas superiores del modelo OSI

### Seguridad en Servicios

- Cada servicio tiene consideraciones específicas de seguridad
- La autenticación, autorización y cifrado son esenciales
- Los protocolos modernos priorizan conexiones seguras (HTTPS, SFTP, SSH)

### Tendencias Actuales

- Virtualización de servicios
- Computación en la nube
- Microservicios y contenedores
- Integración con inteligencia artificial y automatización
Claro, aquí tienes el texto reorganizado, mejorado y con una estructura más clara y profesional, sin perder el tono explicativo:
---
## Servicios de DNS

### 📌 Antecedentes

Antes de que existiera el **Sistema de Nombres de Dominio (DNS)**, se utilizaba un archivo local llamado `/etc/hosts` para resolver nombres de dominio a direcciones IP. Este archivo aún existe y es útil en contextos muy pequeños o locales, pero no escala bien para Internet.

A medida que creció la necesidad de resolver nombres en redes más grandes, surgió el protocolo **DNS (Domain Name System)**. A partir de ahí, se desarrollaron otros protocolos relacionados y se programaron servicios especializados para su operación.

---
### 🧠 Estructura del DNS

El DNS se basa en **bases de datos distribuidas** y **jerárquicas** (en forma de árbol). Tener una sola base de datos centralizada sería impráctico, así que el sistema se diseñó para que:

- Cada parte de la jerarquía tenga su **propia sección de la base de datos**.
    
- Existan **réplicas** de esas bases de datos, lo que garantiza redundancia y disponibilidad.
    
- La información se pueda delegar a distintas organizaciones o servidores.
    
---
### 🗂 Organización del DNS

#### Nivel raíz (Root)

- Representado por un punto (`.`).
    
- Desde aquí se derivan todos los demás dominios.
    
#### Primer nivel (Top-Level Domains o TLDs)

- Algunos ejemplos clásicos (creados inicialmente en EE. UU.):
    
    - `.mil` (militar)
        
    - `.gov` (gobierno)
        
    - `.edu` (educación)
        
    - `.org`, `.net`, `.com` (comercial)
        
- Registrar un dominio en esta base de datos tenía un costo (aprox. $50 USD), a menos que fuera para organizaciones sin fines de lucro.
    
- Cada país también tiene su **código de país** como TLD, por ejemplo: `.mx`, `.uk`, `.jp`.
    
#### Segundo nivel

- Cada dominio de país o genérico puede tener sus propios subdominios.
    
- Por ejemplo, en México:
    
    - `.gob.mx`, `.net.mx`, `.org.mx`, `.edu.mx`, `.com.mx`
        
- Un caso anecdótico: alguien quiso registrar `uaa.mx` dentro de `.edu`, pero eso no era posible en ese momento. La Universidad Autónoma de Acapulco, por ejemplo, usa `uaa.edu.mx`.
    
#### Tercer nivel

- Las instituciones o empresas pueden administrar sus propios subdominios.
    
- Por ejemplo, la UAA (Universidad Autónoma de Aguascalientes) administra subdominios como:
    
    - `aulavirtual.uaa.mx`
        
- La universidad mantiene **cuatro servidores DNS**:
    
    - Tres en el campus central
        
    - Uno en el campus sur
        