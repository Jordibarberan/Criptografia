import tkinter as tk
from tkinter import filedialog, messagebox
from sympy import randprime, gcd
import random

# Generar els paràmetres RSA
def generate_rsa_parameters():
    p = randprime(10**5, 10**6)
    q = randprime(10**5, 10**6)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Valors comuns de la clau pública
    common_e_values = [3, 5, 17, 257, 65537]
    
    # Seleccionar un valor de la clau pública dels valors comuns
    e = random.choice(common_e_values)
    while gcd(e, phi) != 1:
        e = random.choice(common_e_values)
    
    d = mod_inverse(e, phi)
    return p, q, n, phi, e, d

# Ús del algoritme Euclidean i del mòdul invers
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y 

def mod_inverse(e, phi):
    gcd, x, y = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError("No multiplicative inverse exists")
    else:
        return x % phi

# Funcions d'encriptació i desencriptació
def encrypt(text, e, n):
    return [pow(ord(char), e, n) for char in text]

def decrypt(cipher, d, n):
    return ''.join([chr(pow(char, d, n)) for char in cipher])

# Funcions GUI per enrcriptar
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

            encrypted_message_str = ','.join(map(str, encrypted_message))

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

# Funcions GUI per desencriptar
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
            with open(ruta_original, 'r', encoding='utf-8') as archivo_entrada:
                contenido = archivo_entrada.read()

            # Dividir el text de brackets amb comes
            contenido_texto = contenido.strip().split(",")

            # Convertir els elements en int
            contenido_texto = [int(x.strip()) for x in contenido_texto]

            desencrypted_message = decrypt(contenido_texto, d, n)

            with open("archivo_desencriptado.txt", 'w', encoding='utf-8') as archivo_salida:
                archivo_salida.write(desencrypted_message)

            messagebox.showinfo("Éxito", "Archivo guardado como 'archivo_desencriptado.txt'.")
        except ValueError as ve:
            messagebox.showerror("Error de conversión", f"Error al convertir el contenido a enteros: {ve}")
        except Exception as ex:
            messagebox.showerror("Error", f"No se pudo guardar el archivo: {ex}")

    ventana_desencriptado = tk.Toplevel(root)
    ventana_desencriptado.title("Desencriptado")
    ventana_desencriptado.geometry("500x300")

    tk.Label(ventana_desencriptado, text="Subir y guardar un archivo como 'archivo_desencriptado'", font=("Arial", 14)).pack(pady=20)
    archivo_label = tk.Label(ventana_desencriptado, text="No se ha seleccionado ningún archivo", font=("Arial", 12))
    archivo_label.pack(pady=10)
    tk.Button(ventana_desencriptado, text="Seleccionar archivo", font=("Arial", 12), command=cargar_archivo).pack(pady=10)
    tk.Button(ventana_desencriptado, text="Cerrar", font=("Arial", 12), command=ventana_desencriptado.destroy).pack(pady=20)

# Generar els paràmetres de RSA
p, q, n, phi, e, d = generate_rsa_parameters()

# Codi de GUI
root = tk.Tk()
root.title("Menú de Encriptación")
root.geometry("600x400")

label = tk.Label(root, text="Escoja una opcion", font=("Arial", 18), fg="black")
label.pack(pady=20)

encrypt_button = tk.Button(root, text="Encriptar", font=("Arial", 14), bg="lightblue", command=abrir_ventana_encriptado)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(root, text="Desencriptar", font=("Arial", 14), bg="lightgreen", command=abrir_ventana_desencriptado)
decrypt_button.pack(pady=10)

root.mainloop()




