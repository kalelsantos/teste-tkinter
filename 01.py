import tkinter as tk # importa o tkinter e cria uma abreviacao

janela = tk.Tk() # cria a janela
janela.title(" sistema - login ") # define o titulo da janela
janela.geometry("960x540") # define o tamanho da janela
janela.configure(bg="#ffffff") # define a cor de fundo da janela
tk.Label(janela, text="", bg="#ffffff").pack(pady=60)

campo_email = tk.Entry(
    janela, 
    font=("Arial", 14), 
    width=20,
    bg="#f2f2f2",
    fg="#8a8a8a",
    bd=0,
    highlightthickness=1,
    highlightbackground="#d1d1d1",
)
campo_email.insert(0, "e-mail") # insere o texto "e-mail" no campo de entrada

campo_email.pack(ipady=8)

janela.mainloop() # mantem a janela aberta