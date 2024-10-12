import tkinter as tk
from tkinter import messagebox

# Función para gestionar los clics en los botones
def on_click(symbol):
    current = entry.get()  # Obtener el valor de la entrada

    if symbol == 'C':  # Limpiar entrada desde el inicio al final
        entry.delete(0, tk.END)
    elif symbol == '=':  # Realizar la operación
        try:
            result = eval(current)  # eval realiza la operación matemática
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Operación no válida")
    else:
        entry.insert(tk.END, symbol)  # Insertar el símbolo en la entrada

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora")

# Crear el campo de entrada
entry = tk.Entry(root, width=35, borderwidth=5, font=('Arial', 18))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Definir los botones de la calculadora
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Crear y colocar los botones en la ventana
row_val = 1
col_val = 0

for button in buttons:
    action = (lambda x=button: on_click(x))
    b = tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), command=action)
    b.grid(row=row_val, column=col_val, sticky="nsew")

    col_val += 1
    if col_val > 3:  # Cada fila tiene 4 botones
        col_val = 0
        row_val += 1

# Ajustar las columnas para que se expandan
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Ajustar las filas para que se expandan
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

# Iniciar la aplicación
root.mainloop()
