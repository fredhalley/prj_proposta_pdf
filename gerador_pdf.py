import tkinter as tk
from tkinter.filedialog import askdirectory
from fpdf import FPDF
from tkinter import messagebox

def limpar_campos():
    nome_projeto.delete("1.0", "end")
    horas_estimadas.delete("1.0", "end")
    valor_hora.delete("1.0", "end")
    prazo_entrega.delete("1.0", "end")
    dados_diretorio.delete("1.0", "end")

def selecionar_diretorio():    
    dados_diretorio.delete("1.0", "end")
    diretorio = askdirectory(title="Selecione o diretorio onde sera salvo o documento.")
    var_diretorio.set(diretorio)
    if diretorio:
        dados_diretorio.insert("1.0", diretorio)

def gerar_pdf():
    dados_projeto_imp = nome_projeto.get("1.0", tk.END)
    dados_projeto = dados_projeto_imp.strip()
    horas_projeto_imp = horas_estimadas.get("1.0", tk.END)
    horas_projeto = horas_projeto_imp.strip()
    valor_projeto_imp = valor_hora.get("1.0", tk.END)
    valor_projeto = valor_projeto_imp.strip()
    prazo_projeto_imp = prazo_entrega.get("1.0", tk.END)
    prazo_projeto = prazo_projeto_imp.strip()
    valor_total_projeto = int(horas_projeto) * int(valor_projeto)
    diretorio_imp = dados_diretorio.get("1.0", tk.END)
    diretorio_projeto = diretorio_imp.strip()
    projeto = str(diretorio_projeto) + "/" + dados_projeto + ".pdf"
    #A PARTIR DAQUI INICIA A GERAÇÃO DO PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial")
    #PARA USAR UM TEMPLATE, UTILIZE O CODIGO ABAIXO
    pdf.image('template.png',x=0,y=0)
    #INSERINDO AS INFORMAÇÕES NO PDF
    pdf.text(115, 145, dados_projeto)
    pdf.text(115, 160, horas_projeto)
    pdf.text(115, 175, valor_projeto)
    pdf.text(115, 190, prazo_projeto)
    pdf.text(115, 205, str(valor_total_projeto))
    #SALVANDO O ARQUIVO EM PDF
    pdf.output(projeto)

def validar_dados():
    dados_projeto_imp = nome_projeto.get("1.0", tk.END)
    dados_projeto = dados_projeto_imp.strip()
    horas_projeto_imp = horas_estimadas.get("1.0", tk.END)
    horas_projeto = horas_projeto_imp.strip()
    valor_projeto_imp = valor_hora.get("1.0", tk.END)
    valor_projeto = valor_projeto_imp.strip()
    prazo_projeto_imp = prazo_entrega.get("1.0", tk.END)
    prazo_projeto = prazo_projeto_imp.strip()
    diretorio_imp = dados_diretorio.get("1.0", tk.END)
    diretorio_projeto = diretorio_imp.strip()
    if dados_projeto == "":
        messagebox.showerror("Informe os dados do projeto.", "Favor informar o nome do projeto.")
    elif horas_projeto == "":
        messagebox.showerror("Informe a quantidade de horas do projeto.", "Favor informar a quantidade de horas do projeto.")
    elif not horas_projeto.isdigit():
        messagebox.showerror("Campo quantidade de horas do projeto.", "Favor digitar apenas numeros nesse campo.")
    elif valor_projeto == "":
        messagebox.showerror("Informe o valor cobrado em hora do projeto.", "Favor informar o valor cobrado por horas do projeto.")
    elif not valor_projeto.isdigit():
        messagebox.showerror("Campo valor hora do projeto.", "Favor digitar apenas numeros nesse campo.")
    elif prazo_projeto == "":
        messagebox.showerror("Informe o prazo do projeto.", "Favor informar prazo de termino do projeto.")
    elif diretorio_projeto == "":
        messagebox.showerror("Selecione o diretorio.", "Favor selecionar o diretorio.")
    else:
        gerar_pdf()

janela = tk.Tk()
janela.configure(bg="white")

janela.title("Gerador de PDF")

janela.geometry("560x250")

label01 = tk.Label(text="Nome do Projeto:", bg="white", font=('Microsoft YaHei UI light', 10, 'bold'))
label01.grid(row=0, column=0, padx=10, pady=10)

nome_projeto = tk.Text(width=40, height=1, font=('Microsoft YaHei UI light', 10, 'bold'))
nome_projeto.grid(row=0, column=1, padx=10, pady=10, columnspan=3, sticky='NSEW')

label02 = tk.Label(text="Horas estimadas:", bg="white", font=('Microsoft YaHei UI light', 10, 'bold'))
label02.grid(row=1, column=0, padx=5, pady=5)

horas_estimadas = tk.Text(width=10, height=1, font=('Microsoft YaHei UI light', 10, 'bold'))
horas_estimadas.grid(row=1, column=1, padx=10, pady=10, sticky='NSEW')

label03 = tk.Label(text="Valor hora:", bg="white", font=('Microsoft YaHei UI light', 10, 'bold'))
label03.grid(row=1, column=2, padx=5, pady=5)

valor_hora = tk.Text(width=10, height=1, font=('Microsoft YaHei UI light', 10, 'bold'))
valor_hora.grid(row=1, column=3, padx=10, pady=10, sticky='NSEW')

label04 = tk.Label(text="Prazo de Entrega:", bg="white", font=('Microsoft YaHei UI light', 10, 'bold'))
label04.grid(row=3, column=0, padx=10, pady=10)

prazo_entrega = tk.Text(width=40, height=1, font=('Microsoft YaHei UI light', 10, 'bold'))
prazo_entrega.grid(row=3, column=1, padx=10, pady=10, columnspan=3, sticky='NSEW')

var_diretorio = tk.StringVar()

botao_diretorio_final = tk.Button(text="Informe o diretorio:", width=20, wraplength=150, height=2, command=selecionar_diretorio, font=('Microsoft YaHei UI light', 10, 'bold'), border=0, bg='#57a1f8', fg='white')
botao_diretorio_final.grid(row=4, column=0, padx=10, pady=10)           

dados_diretorio = tk.Text(width=40, height=2, font=('Microsoft YaHei UI light', 10, 'bold'))
dados_diretorio.grid(row=4, column=1, padx=10, pady=10, columnspan=3, sticky='NSEW')

botao_limpar_campos = tk.Button(text="Limpar Campos", width=10, command=limpar_campos, font=('Microsoft YaHei UI light', 10, 'bold'), border=0, bg='#57a1f8', fg='white')
botao_limpar_campos.grid(row=5, column=0, padx=10, pady=10, columnspan=2, sticky='NSEW')

botao_gerar_pdf = tk.Button(text="Gerar PDF", width=10, command=validar_dados, font=('Microsoft YaHei UI light', 10, 'bold'), border=0, bg='#57a1f8', fg='white')
botao_gerar_pdf.grid(row=5, column=2, padx=10, pady=10, columnspan=2, sticky='NSEW')

janela.mainloop()