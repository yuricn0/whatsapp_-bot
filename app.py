import webbrowser   
import pyautogui as gui
from time import sleep
import pyperclip



def escrever_texto(frase):
    pyperclip.copy(frase)
    gui.hotkey('Ctrl', 'v')


numeros = [5511930049601, 5511951592873, 5562981804775]

for indice, numero in enumerate(numeros):
    webbrowser.open(f'https://api.whatsapp.com/send?phone={numero}')
    sleep(10)
    if indice == 0:
        for i in range(5):
            gui.hotkey('shift', 'tab')
    sleep(5)
    escrever_texto('Teste')
    gui.press('enter')
    sleep(20)