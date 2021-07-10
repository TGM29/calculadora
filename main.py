import tkinter as tk


# Definindo calculadora e suas operacoes
class calculadora:

    def soma(x, y):
        resultado = x + y
        return resultado

    def subtracao(x, y):
        resultado = x - y
        return resultado

    def divisao(x, y):
        resultado = x / y
        return resultado

    def multiplicacao(x, y):
        resultado = x * y
        return resultado


tela = tk.Tk()

label1 = tk.Label(tela, text="Bem vindo a calculadora")
label1.grid(column=0, row=0)


def botao():
    i = 0
    for i in range(11):
        botao = tk.Button(tela, text=f"{i}")
        botao.grid(column=i + 1, row=2)
        i = i + 1


botao()
tela.mainloop()

