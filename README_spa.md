# Automatización de Descarga y Envío de PDFs a través de Telegram

## Descripción
Este proyecto consiste en un script de Python que realiza automáticamente las siguientes tareas:
1. Lee URLs y nombres de carpetas de un archivo de texto.
2. Para cada URL, descarga todos los archivos PDF encontrados en la página.
3. Guarda cada PDF en una carpeta específica en el servidor/local.
4. Envía los PDFs descargados a un chat de Telegram mediante un bot.

## Cómo Funciona
- **Carga de Datos**: El script lee un archivo `webs.txt` que contiene pares de nombre de carpeta y URL separados por comas.
- **Descarga de PDFs**: Para cada URL, el script busca enlaces a archivos PDF y los descarga en la carpeta correspondiente.
- **Envío a través de Telegram**: Cada archivo PDF descargado se envía automáticamente a un chat de Telegram específico mediante un bot.

## Requisitos
Para ejecutar este script, necesitarás:
- Python 3.x
- Bibliotecas de Python: `requests`, `bs4` (BeautifulSoup), `os`, `urllib`, `telebot`, `dotenv`.
- Un archivo `.env` con las variables `TELEBOT_TOKEN` y `CHAT_ID` configuradas para el bot de Telegram.
- Un archivo `webs.txt` con los nombres de las carpetas y las URLs.

## Instalación y Ejecución
1. **Instalación de Dependencias**: Asegúrate de tener todas las bibliotecas necesarias instaladas.
2. **Configuración del Archivo `.env`**: Crea un archivo `.env` en el mismo directorio del script con las variables requeridas.
3. **Preparación de `webs.txt`**: Crea y rellena el archivo `webs.txt` con los nombres de las
