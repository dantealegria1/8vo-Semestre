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