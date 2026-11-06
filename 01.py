import tkinter as tk # importa o tkinter e cria uma abreviacao

janela = tk.Tk() # cria a janela
janela.title(" sistema - login ") # define o titulo da janela
janela.geometry("960x540") # define o tamanho da janela
janela.configure(bg="#ffffff") # define a cor de fundo da janela
tk.Label(janela, text="", bg="#ffffff").pack(pady=50)

imagem_logo = tk.PhotoImage(file="image/logo.png").subsample(2, 2) # carrega a imagem do logo e redimensiona para metade do tamanho original

rotulo_logo = tk.Label(janela, image=imagem_logo, bg ="#ffffff")
rotulo_logo.pack(pady=(10, 50)) # exibe a imagem do logo na janela e define o espaçamento entre a imagem e os elementos acima e abaixo dela, ou seja, 10 pixels acima e 50 pixels abaixo da imagem


campo_email = tk.Entry(
    janela, 
    font=("Arial", 14), 
    width=40,
    bg="#f2f2f2",
    fg="#8a8a8a",
    bd=0,
    highlightthickness=1,
    highlightbackground="#d1d1d1",
)
campo_email.insert(0, "e-mail") # insere o texto "e-mail" no campo de entrada
campo_email.pack(ipady=8)

janela.mainloop() # mantem a janela aberta