import tkinter as tk # importa o tkinter e cria uma abreviacao
from tkmacosx import Button # importa o Button do tkmacosx para criar botoes com bordas arredondadas

# def alternar_senha():
#     if campo_senha.cget("show") == "*": # .cget("show") lê o estado atual da propriedade "show"
#         campo_senha.config(show="") # mostra o texto normal
#     else:
#         campo_senha.config(show="*") # volta a mostrar o texto como asteriscos



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
campo_email.insert(2, "e-mail") # insere o texto "e-mail" no campo de entrada
campo_email.pack(ipady=8)

campo_senha = tk.Entry(
    janela, 
    font=("Arial", 14), 
    width=40,
    bg="#f2f2f2",
    fg="#8a8a8a",
    bd=0,
    highlightthickness=1,
    highlightbackground="#d1d1d1",
    show="*"
)
campo_senha.pack(ipady=8, pady=(10, 5))

# checkbox_senha = tk.Checkbutton( # cria o checkbox para mostrar a senha
#     janela, 
#     text="Mostrar senha", # define o texto do checkbox
#     font=("Arial", 12),
#     bg="#ffffff",
#     command=alternar_senha # o command serve para chamar a função alternar_senha() quando o checkbox for clicado
# )
# checkbox_senha.pack(pady=(0, 15))

botao_acessar = Button(
    janela,
    text="Acessar",
    font=("Arial", 12, "bold"),
    bg="#298fc2",
    fg="#ffffff",
    borderless=1,
    highlightthickness=0,
    cursor="hand2",
    width=330
)
botao_acessar.pack(pady=2, ipady=10)


texto_link = "PRIMEIRO ACESSO"
link_primeiro_acesso = tk.Label(
    janela,
    text= texto_link.upper(),  # converte o texto para maiúsculas
    font=("arial", 10, "bold"),
    bg="#ffffff",
    fg="#298fc2",
    cursor="hand2"
)
link_primeiro_acesso.pack(pady=(0, 10))

janela.mainloop() # mantem a janela aberta