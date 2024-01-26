import tkinter as tk
from tkinter import messagebox

def verificar_glicemia(glicemia):
    if glicemia > 160:
        return 'Glicemia Elevada'
    else:
        return 'Dados registrados'

def processar_dados():
    nome = entry_nome.get()
    idade = entry_idade.get()
    data = entry_data.get()
    horario = entry_horario.get()
    
    try:
        glicemia = int(entry_glicemia.get())
        resultado = verificar_glicemia(glicemia)
        label_resultado.config(text=f"Nome: {nome}\nIdade: {idade}\nData: {data}\nHorário: {horario}\nGlicemia: {glicemia}\n{resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico para a glicemia.")

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_data.delete(0, tk.END)
    entry_horario.delete(0, tk.END)
    entry_glicemia.delete(0, tk.END)
    label_resultado.config(text="")

# Criar a janela principal
janela = tk.Tk()
janela.title("Monitoramento de Glicemia")

# Criar uma fonte maior
fonte_grande = ("Arial", 14)

# Criar widgets com a fonte maior
label_nome = tk.Label(janela, text="Nome:", font=fonte_grande)
label_idade = tk.Label(janela, text="Idade:", font=fonte_grande)
label_data = tk.Label(janela, text="Data:", font=fonte_grande)
label_horario = tk.Label(janela, text="Horário:", font=fonte_grande)
label_glicemia = tk.Label(janela, text="Glicemia:", font=fonte_grande)

entry_nome = tk.Entry(janela, font=fonte_grande)
entry_idade = tk.Entry(janela, font=fonte_grande)
entry_data = tk.Entry(janela, font=fonte_grande)
entry_horario = tk.Entry(janela, font=fonte_grande)
entry_glicemia = tk.Entry(janela, font=fonte_grande)

button_processar = tk.Button(janela, text="Processar", command=processar_dados, font=fonte_grande)
button_limpar = tk.Button(janela, text="Limpar", command=limpar_campos, font=fonte_grande)

# Adicionar um rótulo para exibir os resultados
label_resultado = tk.Label(janela, text="", font=fonte_grande)

# Posicionar widgets na grade
label_nome.grid(row=0, column=0, sticky="e")
label_idade.grid(row=1, column=0, sticky="e")
label_data.grid(row=2, column=0, sticky="e")
label_horario.grid(row=3, column=0, sticky="e")
label_glicemia.grid(row=4, column=0, sticky="e")

entry_nome.grid(row=0, column=1)
entry_idade.grid(row=1, column=1)
entry_data.grid(row=2, column=1)
entry_horario.grid(row=3, column=1)
entry_glicemia.grid(row=4, column=1)

button_processar.grid(row=5, column=0, columnspan=2, pady=10)
button_limpar.grid(row=6, column=0, columnspan=2)

# Adicionar o rótulo de resultados abaixo dos botões
label_resultado.grid(row=7, column=0, columnspan=2)

# Iniciar a interface gráfica
janela.mainloop()
