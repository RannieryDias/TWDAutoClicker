import time, pyautogui, winsound
#import cx_freeze
from random import randint

#pegar o retorno da posicao atual de x e y do mouse e passar o valor da tupla para as duas variaveis
x, y = pyautogui.position()
print("Posicao atual do mouse:")

print("x = "+str(x)+" y = "+str(y))

print("")

#retorna verdadeiro se x & y estiverem dentro da tela
print ("Esta dentro da tela?")
resp = pyautogui.onScreen(x, y)
print(str(resp))

n = 0 #numero de curtidas feitas
b = winsound.Beep
pyautogui.click(414,1057)

#i = randint(30,50) #quantidade de fotos a serem curtidas
i = 500
intervalo = randint(5,10) #intervalo entre as curtidas

while(i != 0):
    time.sleep(1)
    pyautogui.click(1077, 670)
    time.sleep(4)
    pyautogui.click(804, 764)
    time.sleep(40)
    pyautogui.click(1745, 940)
    time.sleep(3)
    pyautogui.click(969, 672)
    time.sleep(2)
    pyautogui.click(969, 672)
    time.sleep(1)
    n += 1
    i -= 1

b(500,500)
