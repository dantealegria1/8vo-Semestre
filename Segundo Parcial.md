## **Procesos**

Un **proceso** es una tarea activa que tiene la posibilidad de ejecutarse en el sistema operativo. Los procesos compiten entre sí por los recurs os del sistema, como tiempo de CPU y memoria. Cada proceso se identifica y gestiona mediante una **orden** o **comando** que incluye las instrucciones y los datos necesarios para su ejecución.

### **Características de un proceso**

Un proceso en Unix o Linux se identifica y administra mediante los siguientes atributos:

- **PID (Process ID):** Es el identificador único del proceso en el sistema.
- **Dueño:** Usuario que creó o ejecutó el proceso.
- **Grupo:** El proceso pertenece a un grupo de usuarios. Un proceso solo puede pertenecer a un grupo principal.
- **Estado:** El estado del proceso puede ser:
    - **Ejecutándose** (running)
    - **En espera** (waiting)
    - **Detenido** (stopped)
    - **Terminado** (terminated)
- **Permisos:** Define qué usuarios o grupos pueden ver o interactuar con el proceso.

---

### **Estructura de entrada y salida**

Un proceso en Unix/Linux gestiona **tres flujos principales** de datos:

1. **Entrada estándar (stdin)** → Canal de entrada para recibir datos (teclado, archivo, etc.).
2. **Salida estándar (stdout)** → Canal de salida para mostrar resultados (pantalla, archivo, etc.).
3. **Salida de error (stderr)** → Canal de salida para mostrar errores generados durante la ejecución.

---

### **Relación entre procesos**

- Un proceso puede generar otros procesos secundarios (hijos).
- Un proceso secundario **conoce a su proceso padre** mediante el **PID del proceso padre (PPID)**.
- Sin embargo, el proceso padre **no tiene conocimiento directo** de los procesos hijos, a menos que se implemente un mecanismo de seguimiento.

---

### **Ejecución desde la CLI**

Cuando ejecutas una orden desde la línea de comandos (CLI), esta contiene:

- **Instrucciones:** El código o comando que se va a ejecutar.
- **Datos:** La información que el comando necesita para ejecutarse correctamente.

Ejemplo desde la CLI:

```bash
ps aux
```

Este comando muestra una lista de todos los procesos en ejecución y sus atributos (PID, usuario, estado, etc.).

---

### **Competencia por recursos**

Los procesos compiten por varios recursos del sistema, como:

- **Procesamiento:** Tiempo de CPU.
- **Memoria:** Espacio en RAM y memoria de intercambio (swap).
- **Entradas y salidas:** Acceso a archivos, dispositivos, etc.
### Línea de Órdenes (CLI)

La línea de órdenes (CLI) permite ejecutar comandos mediante parámetros y metacaracteres que tienen un significado especial para el sistema, permitiendo realizar acciones específicas más allá de los caracteres mismos.
#### **Metacaracteres**

Los metacaracteres tienen un significado especial en el contexto del CLI, permitiendo realizar operaciones avanzadas con los comandos.

- **TAB** → Separador de parámetros.
- **""** → Agrupador que permite la sustitución de variables.
- **''** → Delimitador que agrupa texto literalmente (sin sustituciones).
- **()** → Agrupador de valores o expresiones.
- **\** → Escapa metacaracteres, eliminando su significado especial.
#### **Redirecciones**

Los operadores de redirección permiten manipular la entrada y salida de comandos en el CLI.

- **>** → Redirige la salida a un archivo (sobrescribe el contenido).
- **>>** → Redirige la salida a un archivo (añade al contenido existente).
- **<** → Redirige la entrada desde un archivo.
- **<<** → Redirige la entrada desde un bloque de texto definido.