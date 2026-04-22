# Sistema de Gestión de Inventario de Red - INACAP

##  Descripción del Proyecto
Este script de Python ha sido desarrollado como una solución profesional para la documentación y gestión de dispositivos intermediarios en infraestructuras de red complejas. Permite registrar, organizar y consultar información técnica de dispositivos siguiendo el modelo jerárquico de red.

---

## Mejoras y Correcciones Aplicadas (Changelog)

### 1. Implementación de Persistencia de Datos
* **Antes:** Los datos se perdían al cerrar el programa.
* **Ahora:** Se implementó un sistema de almacenamiento en **archivos planos (.txt)**. Cada sucursal tiene su propia "memoria", asegurando que la información persista incluso después de reiniciar el sistema Ubuntu.

### 2. Organización por Sucursales (Escalabilidad)
* Se reestructuró el código para utilizar el concepto de **Sucursales** en lugar de Sedes, alineándose con los requerimientos específicos de la topología.
* **Sucursales integradas:** Campus Uno, Campus Matriz, Zona Core / VPN, Sector Outsourcing.

### 3. Validación de Modelo Jerárquico
* Se añadió un sistema de clasificación obligatorio para cada dispositivo:
    * **Capa de Núcleo (Core):** Transporte de alta velocidad.
    * **Capa de Distribución:** Agregación y políticas.
    * **Capa de Acceso:** Conexión de usuarios finales.

### 4. Robustez y Manejo de Errores
* **Tratamiento de caracteres especiales:** Se corrigió el error que impedía crear archivos con caracteres como `/` (usado en la Zona Core / VPN), reemplazándolos automáticamente por guiones bajos para compatibilidad con el sistema de archivos de Linux.
* **Prevención de cierres inesperados:** Se implementaron bloques `try/except` para manejar ingresos de datos erróneos (como letras en campos numéricos), evitando que el programa se rompa durante la ejecución.

### 5. Cumplimiento de Pauta Académica
* El sistema ahora obliga al registro de los **5 parámetros críticos**:
    1. Dirección IP.
    2. Nombre del dispositivo.
    3. VLANs configuradas.
    4. Servicios de red comprometidos.
    5. Capa del modelo jerárquico.

---

##  Tecnologías Utilizadas
* **Lenguaje:** Python 3
* **Sistema Operativo:** Ubuntu (Linux)
* **Control de Versiones:** Git / GitHub
* **Almacenamiento:** Manejo de archivos (I/O) nativo de Python.

---

##  Estructura de Archivos Generados
Al registrar dispositivos, el sistema genera automáticamente los siguientes reportes:
* `Campus_Uno.txt`
* `Campus_Matriz.txt`
* `Zona_Core_VPN.txt`
* `Sector_Outsourcing.txt`


---

**Desarrollado para la asignatura de Redes Avanzadas - Abril 2026**
