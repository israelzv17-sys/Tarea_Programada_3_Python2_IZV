Generador de Catálogos e Informes de Imágenes
============================================

Descripción general
-------------------

Este proyecto contiene un script en Python que automatiza el procesamiento por lotes de imágenes en formato .jpg y .png. El código lee las imágenes desde la carpeta ``Imagenes Tarea 2``, las redimensiona a un máximo de 800x800 píxeles, aplica escala de grises, añade una marca de agua con el texto ``Firma empresa`` en la esquina superior izquierda y guarda las versiones procesadas en la carpeta ``Imagenes procesadas``.

Además, genera un reporte en formato Excel llamado ``reporte_imagenes.xlsx`` con los metadatos de cada imagen procesada, incluyendo el nombre del archivo, el formato, el ancho original, el alto original y el estado de procesamiento.

Requisitos
----------

- Python 3.x
- Entorno virtual ``.venv``
- Dependencias listadas en ``requirements.txt``

Instrucciones de ejecución
--------------------------

1. Abrir la carpeta del proyecto en la terminal.
2. Crear y activar el entorno virtual ``.venv``:

.. code-block:: powershell

   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

3. Instalar las dependencias del proyecto:

.. code-block:: powershell

   pip install -r requirements.txt

4. Ejecutar el programa desde la raíz del proyecto:

.. code-block:: powershell

   python main.py

Resultados esperados
--------------------

- Las imágenes procesadas se guardarán en la carpeta ``Imagenes procesadas``.
- Se generará un archivo de Excel llamado ``reporte_imagenes.xlsx`` con el resumen de las imágenes procesadas.
- El script procesa únicamente archivos con extensión ``.jpg`` y ``.png``.
