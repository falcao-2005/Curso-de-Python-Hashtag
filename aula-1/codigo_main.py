import pyautogui
import time

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(x=405, y=71)
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(2)

pyautogui.click(x=947, y=430)
pyautogui.write("fernandoaefm@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua senha")

pyautogui.press("tab")
pyautogui.press("enter")

import pandas as pd

tabela = pd.read_csv("produtos.csv")

for linha in tabela.index:
    pyautogui.click(x=1037, y=319)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    if(obs != "nan"):
        pyautogui.write(obs)
    
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)
