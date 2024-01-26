import tkinter as tk

# Função para realizar cálculos
def calcular():
    try:
        expressao = entrada.get()
        resultado = eval(expressao)
        resultado_var.set(resultado)
    except Exception as e:
        resultado_var.set("Erro")

# Configuração da interface gráfica
app = tk.Tk()
app.title("Calculadora")

# Variáveis
resultado_var = tk.StringVar()

# Entrada
entrada = tk.Entry(app, width=20, font=('Arial', 14), bd=5)
entrada.grid(row=0, column=0, columnspan=4)

# Botões
botoes = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for botao in botoes:
    tk.Button(app, text=botao, padx=20, pady=20, font=('Arial', 14), bd=5, command=lambda x=botao: entrada.insert(tk.END, x) if x != '=' else calcular()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Resultado
resultado = tk.Label(app, textvariable=resultado_var, font=('Arial', 14))
resultado.grid(row=row_val, column=0, columnspan=4)

app.mainloop()
