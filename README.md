# Mejora del Codigo - Redes Avanzadas I

Este proyecto presenta una mejora al script original para la documentación de una red jerárquica.

## Mejoras Realizadas:
Escalabilidad: Se implementó una lista dinámica de sedes (Campus) que permite el crecimiento de la red sin modificar la lógica principal.

Persistencia de Datos: Se corrigió el manejo de archivos externos para que cada sucursal tenga su propio registro `.txt` independiente.

Requerimientos Técnicos: Se añadieron campos obligatorios que faltaban en el script original: Direccionamiento IP y VLANs.

Modelo Jerárquico: El programa ahora clasifica automáticamente cada dispositivo en las capas de Núcleo, Distribución o Acceso.

Interfaz de Usuario: Se limpió la lógica de menús para evitar opciones duplicadas y errores de entrada.
