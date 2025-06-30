# Gestor de contenido de archivos para NVDA

**Versión 1.2**

## Descripción

Este complemento para NVDA permite gestionar de forma ágil y accesible el texto y las rutas de archivos de texto seleccionados en el Explorador de Windows, así como crear nuevos archivos y abrir rutas directamente desde atajos de teclado.  
Desarrollado por **Miguel Barraza**, el plugin ofrece una serie de comandos que facilitan el flujo de trabajo sin necesidad de cambiar de aplicación ni usar menús contextuales.

## Funcionalidades

- Copiar y pegar el contenido completo de un archivo seleccionado.  
- Añadir (“append”) texto de un archivo al portapapeles o viceversa, con inserción automática de saltos de línea.  
- Sobrescribir archivos con el contenido del portapapeles.  
- Crear un nuevo archivo con nombre personalizado y pegar en él el contenido del portapapeles.  
- Copiar la ruta de un archivo en formato Windows (`C:\ruta\al\archivo.txt`) o en formato tipo Linux (`c:/ruta/al/archivo.txt`).  
- Mostrar en el Visor de NVDA el contenido de un archivo o del portapapeles.  
- Abrir directamente en el Explorador de Windows la ruta almacenada en el portapapeles.

## Instalación

1. Descarga el archivo desde [este enlace](https://github.com/MiguelBarrazaAr/fileContentManager/releases/download/v1.2/FileContentManager.nvda-addon).  
2. Eejecuta pulsando enter sobre el archivo FileContentManager.nvda-addon y sigue las instrucciones para instalar.  
3. Reinicia NVDA.

## Atajos de teclado

| Atajo                       | Acción                                                                                 |
| --------------------------- | -------------------------------------------------------------------------------------- |
| NVDA + Control + Shift + C   | Copia al portapapeles todo el contenido del archivo seleccionado                       |
| NVDA + Control + Alt + C     | Añade al portapapeles el contenido del archivo (append), con salto de línea previo     |
| NVDA + Control + Shift + V   | Sobrescribe el archivo seleccionado con el texto del portapapeles                     |
| NVDA + Control + Alt + V     | Añade al final del archivo seleccionado el texto del portapapeles, con salto de línea |
| NVDA + Shift + Espacio       | Muestra en el Visor de NVDA el contenido completo del archivo seleccionado              |
| NVDA + Alt + A              | Abre diálogo para escribir texto y copia al portapapeles                               |
| NVDA + Control + Shift + A   | Abre diálogo para escribir texto y añade al portapapeles con salto de línea           |
| NVDA + Control + Shift + R   | Copia al portapapeles la ruta del archivo en formato Windows                           |
| NVDA + Alt + Control + Shift + R | Copia al portapapeles la ruta del archivo en formato Linux (barras `/`)          |
| NVDA + Control + Shift + F   | Crea un nuevo archivo (nombre personalizado) en la carpeta del foco y pega el portapapeles |
| NVDA + Control + Shift + D   | Abre en el Explorador la ruta que hay en el portapapeles                               |
| NVDA + Control + Shift + Z   | Muestra en el Visor de NVDA el texto que hay actualmente en el portapapeles             |

## Ejemplo de uso

1. Selecciona `notas.txt` en tu carpeta de proyecto en el Explorador de Windows.  
2. Pulsa **NVDA+Control+Shift+C** para copiar todo su contenido.  
3. Abre tu editor y pega con **Ctrl+V**.  
4. Modifica o añade texto en el portapapeles con **NVDA+Control+Shift+A** sin salir del explorador.  
5. Para crear un nuevo archivo `resumen.txt` y pegar en él lo copiado, pulsa **NVDA+Control+Shift+F**, escribe `resumen.txt` y acepta.

## Autor

Miguel Barraza (<miguelbarraza2015@gmail.com>)

## Descarga

Descarga la última versión desde:  
[https://github.com/MiguelBarrazaAr/fileContentManager/releases/download/v1.2/FileContentManager.nvda-addon](https://github.com/MiguelBarrazaAr/fileContentManager/releases/download/v1.2/FileContentManager.nvda-addon)
