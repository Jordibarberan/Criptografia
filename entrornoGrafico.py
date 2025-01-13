
import tkinter as tk
from tkinter import filedialog, messagebox
from sympy import randprime
import random

# Es generen els paràmetres d'encripació RSA de forma aleatòria
def generate_rsa_parameters():
    p = randprime(10**5, 10**6)
    q = randprime(10**5, 10**6)
    n = p * q
    zero = (p - 1) * (q - 1)
    e = 65537
    d = mod_inverse(e, zero)
    return p, q, n, zero, e, d

# Ús de l'algoritme Euclidean i mòdul invers
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def mod_inverse(e, zero):
    gcd, x, y = extended_gcd(e, zero)
    if gcd != 1:
        raise ValueError("No existe inverso multiplicativo")
    else:
        return x % zero

# Funcions d'encriptació i desnecriptació
def encrypt(text, e, n):
    return [pow(ord(char), e, n) for char in text]

def decrypt(text, d, n):
    return ''.join([chr(pow(char, d, n)) for char in text])

# Funcions GUI per encriptació
def abrir_ventana_encriptado():
    def cargar_archivo():
        archivo = filedialog.askopenfilename(title="Seleccionar archivo")
        if archivo:
            archivo_label.config(text=f"Archivo seleccionado: {archivo}")
            guardar_como_bajada(archivo)
        else:
            messagebox.showwarning("Advertencia", "No se seleccionó ningún archivo.")

    def guardar_como_bajada(ruta_original):
        try:
            with open(ruta_original, 'rb') as archivo_entrada:
                contenido = archivo_entrada.read()

            contenido_texto = contenido.decode('latin1')

            encrypted_message = encrypt(contenido_texto, e, n)

            print(encrypted_message)
            encrypted_message_str = str(encrypted_message)

            with open("archivo_encriptado.txt", 'w', encoding='utf-8') as archivo_salida:
                archivo_salida.write(encrypted_message_str)

            messagebox.showinfo("Éxito", "Archivo guardado como 'archivo_encriptado.txt'.")
        except Exception as ex:
            messagebox.showerror("Error", f"No se pudo guardar el archivo: {ex}")

    ventana_encriptado = tk.Toplevel(root)
    ventana_encriptado.title("Encriptado")
    ventana_encriptado.geometry("500x300")

    tk.Label(ventana_encriptado, text="Subir y guardar un archivo como 'archivo_encriptado'", font=("Arial", 14)).pack(pady=20)
    archivo_label = tk.Label(ventana_encriptado, text="No se ha seleccionado ningún archivo", font=("Arial", 12))
    archivo_label.pack(pady=10)
    tk.Button(ventana_encriptado, text="Seleccionar archivo", font=("Arial", 12), command=cargar_archivo).pack(pady=10)
    tk.Button(ventana_encriptado, text="Cerrar", font=("Arial", 12), command=ventana_encriptado.destroy).pack(pady=20)

# Funcions GUI per desencriptació
def abrir_ventana_desencriptado():
    def cargar_archivo():
        archivo = filedialog.askopenfilename(title="Seleccionar archivo")
        if archivo:
            archivo_label.config(text=f"Archivo seleccionado: {archivo}")
            guardar_como_bajada(archivo)
        else:
            messagebox.showwarning("Advertencia", "No se seleccionó ningún archivo.")

    def guardar_como_bajada(ruta_original):
        try:
            with open(ruta_original, 'rb') as archivo_entrada:
                contenido = archivo_entrada.read()

            contenido_texto = contenido.decode('latin1')

            contenido_texto = contenido_texto.strip("[]")
            contenido_texto = [int(x) for x in contenido_texto.split(",")]

            desencrypted_message = decrypt(contenido_texto, d, n)

            desencrypted_message_str = str(desencrypted_message)

            with open("archivo_desencriptado.txt", 'w', encoding='utf-8') as archivo_salida:
                archivo_salida.write(desencrypted_message_str)

            messagebox.showinfo("Éxito", "Archivo guardado como 'archivo_desencriptado.txt'.")
        except Exception as ex:
            messagebox.showerror("Error", f"No se pudo guardar el archivo: {ex}")

    ventana_encriptado = tk.Toplevel(root)
    ventana_encriptado.title("Encriptado")
    ventana_encriptado.geometry("500x300")

    tk.Label(ventana_encriptado, text="Subir y guardar un archivo como 'archivo_desencriptado'", font=("Arial", 14)).pack(pady=20)
    archivo_label = tk.Label(ventana_encriptado, text="No se ha seleccionado ningún archivo", font=("Arial", 12))
    archivo_label.pack(pady=10)
    tk.Button(ventana_encriptado, text="Seleccionar archivo", font=("Arial", 12), command=cargar_archivo).pack(pady=10)
    tk.Button(ventana_encriptado, text="Cerrar", font=("Arial", 12), command=ventana_encriptado.destroy).pack(pady=20)

# Generar paràmetres RSA
p, q, n, zero, e, d = generate_rsa_parameters()

# Codi de GUI
root = tk.Tk()
root.title("Menú de Encriptación")
root.geometry("600x400")

label = tk.Label(root, text="Escoja una opcion", font=("Arial", 18), fg="black")
label.pack(pady=20)

encriptado = True
encrypt_button = tk.Button(root, text="Encriptar", font=("Arial", 14), bg="lightblue", command=abrir_ventana_encriptado)
encrypt_button.pack(pady=10)

encriptado = False
decrypt_button = tk.Button(root, text="Desencriptar", font=("Arial", 14), bg="lightgreen", command=abrir_ventana_desencriptado)
decrypt_button.pack(pady=10)

root.mainloop()
# -*- coding: utf-8 -*-
