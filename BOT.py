import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
import telebot
from dotenv import load_dotenv


# Carga las variables de entorno del archivo .env
load_dotenv()

# Usa las variables de entorno
bot = telebot.TeleBot(os.getenv("TELEBOT_TOKEN"))
chat_id = int(os.getenv("CHAT_ID"))

def check_website_and_send_pdfs(folder_name, url):
    # Ruta base donde se guardará cada carpeta
    base_folder_path = os.path.dirname(os.path.abspath(__file__))

    # Crear la carpeta con el nombre especificado si no existe
    specific_folder_path = os.path.join(base_folder_path, folder_name)
    if not os.path.exists(specific_folder_path):
        os.makedirs(specific_folder_path)

    # Ruta del archivo donde se guardarán los enlaces descargados
    downloaded_links_file = os.path.join(specific_folder_path, 'downloaded_links.txt')

    if not os.path.exists(downloaded_links_file):
        open(downloaded_links_file, 'w').close()

    with open(downloaded_links_file, 'r') as f:
        downloaded_links = [line.strip() for line in f.readlines()]

    response = requests.get(url, verify=False)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        pdf_links = soup.find_all('a', {'href': lambda href: (href and href.endswith('.pdf'))})

        if pdf_links:
            for i, pdf_link in enumerate(pdf_links):
                full_url = urljoin(url, pdf_link['href'])

                if full_url not in downloaded_links:
                    filename = os.path.basename(full_url)
                    file_path = os.path.join(specific_folder_path, filename)
                    r = requests.get(full_url, verify=False)

                    with open(file_path, 'wb') as f:
                        f.write(r.content)
                    
                    with open(file_path, 'rb') as pdf_file:
                        bot.send_document(chat_id, pdf_file, caption=f"#{folder_name}")

                    downloaded_links.append(full_url)

                    with open(downloaded_links_file, 'w') as f:
                        f.write('\n'.join(downloaded_links))

'''
Lee el archivo web.txt con esta estructura: NOMBRE,http://www.direccion.com
El "nombre" se utilizará para nombrar la carpeta para guardar los archivos pdf y
tamién será el tag utilizado en el mensaje de telegram.
'''
with open('webs.txt', 'r') as file:
    for line in file:
        folder_name, url = line.strip().split(',')
        check_website_and_send_pdfs(folder_name, url)
