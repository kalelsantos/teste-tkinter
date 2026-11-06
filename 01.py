import tkinter as tk # importa o tkinter e cria uma abreviacao

janela = tk.Tk() # cria a janela
janela.title(" janela ") # define o titulo da janela
janela.geometry("960x540") # define o tamanho da janela

texto = tk.Label(janela, text="Olá, Tkinter!", font=("Arial", 16))
texto.pack(pady=20)













janela.mainloop() # mantem a janela aberta