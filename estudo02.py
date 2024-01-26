import tkinter as tk
from tkinter import messagebox

def verificar_glicemia(glicemia):
    if glicemia > 160:
        return 'Glicemia Elevada'
    else:
        return 'Siga em frente'

def processar_dados():
    data = entry_data.get()
    horario = entry_horario.get()
    try:
        glicemia = int(entry_glicemia.get())
        resultado = verificar_glicemia(glicemia)
        messagebox.showinfo("Resultado", f"Data: {data}\nHorário: {horario}\nGlicemia: {glicemia}\n{resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico para a glicemia.")

# Criar a janela principal
janela = tk.Tk()
janela.title("Monitoramento de Glicemia")

# Criar widgets
label_data = tk.Label(janela, text="Data:")
label_horario = tk.Label(janela, text="Horário:")
label_glicemia = tk.Label(janela, text="Glicemia:")

entry_data = tk.Entry(janela)
entry_horario = tk.Entry(janela)
entry_glicemia = tk.Entry(janela)

button_processar = tk.Button(janela, text="Processar", command=processar_dados)

# Posicionar widgets na grade
label_data.grid(row=0, column=0, sticky="e")
label_horario.grid(row=1, column=0, sticky="e")
label_glicemia.grid(row=2, column=0, sticky="e")

entry_data.grid(row=0, column=1)
entry_horario.grid(row=1, column=1)
entry_glicemia.grid(row=2, column=1)

button_processar.grid(row=3, column=0, columnspan=2)

# Iniciar a interface gráfica
janela.mainloop()
