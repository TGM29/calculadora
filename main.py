from tkinter import *

x = []

# Definindo calculadora e suas operacoes

def button_add():
    i = 0
    for i in range (10):
        button = Button(tela,text=i, padx =40, pady =40)
        button.grid(row = 0, column=i )
        i = i + 1
    buttonClear = Button(tela,text=i, padx =40, pady =40)
    button.grid(row=0, column=i)


tela = Tk()

button_add()


tela.mainloop()

