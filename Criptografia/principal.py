import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Criptografía")

# Etiqueta de título
label_titulo = tk.Label(ventana, text="Criptografía", font=("Helvetica", 16))
label_titulo.pack(pady=10)

# Entrada para texto a encriptar o desencriptar
entry = tk.Entry(ventana, width=40)
entry.pack(pady=10)

# Botón de encriptar
boton_encriptar = tk.Button(ventana, text="Encriptar")
boton_encriptar.pack(pady=5)

# Botón de desencriptar
boton_desencriptar = tk.Button(ventana, text="Desencriptar")
boton_desencriptar.pack(pady=5)

# Entrada para mostrar el resultado
entry_resultado = tk.Entry(ventana, width=40)
entry_resultado.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()