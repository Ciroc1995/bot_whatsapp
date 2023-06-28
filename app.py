import webbrowser
import pyautogui
from time import sleep

# telefones = [5533984439480, 5533984557830, 5533988174189]

telefones = []

with open('fones.txt','r') as arquivo:
    for linha in arquivo:
        telefones.append(linha.split('\n')[0])
    print(telefones)

for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(10)
    pyautogui.click(1164,227,duration=1)
    sleep(10)
    pyautogui.typewrite('Ola, boa tarde')
    sleep(5)
    pyautogui.press('enter')
    sleep(300)