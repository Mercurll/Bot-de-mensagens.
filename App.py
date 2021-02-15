import keyboard
import pywhatkit
import time
from datetime import datetime
# 1. Definir para quais contatos enviar.
contatos = ['Número']
# 2. Definir intervalo de envios.
while len(contatos) >= 1:
    pywhatkit.sendwhatmsg(contatos[0], 'Hello World.', datetime.now().hour, datetime.now().minute + 1)
    del contatos[0]
    time.sleep(60)
    keyboard.press_and_release('ctrl + w')
#Testar!
