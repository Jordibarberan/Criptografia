
# -*- coding: utf-8 -*-
p = 67
q = 73
n = p * q
zero = (p - 1) * (q - 1)
e = 65537 

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

d = mod_inverse(e, zero)


def encrypt(text, e, n):
    return [pow(ord(char), e, n) for char in text]

def decrypt(text, d, n):
    return ''.join([chr(pow(char, d, n)) for char in text])

print("mensaje a  a cifrar")


try:
    # Abrir el archivo para lectura
    with open('temporal.txt', 'r') as archivo:
        contenido = archivo.read()
        message = contenido

    # Asegúrate de que encrypt y decrypt estén definidas correctamente
    encrypted_message = encrypt(message, e, n)
    decrypted_message = decrypt(encrypted_message, d, n)

    # Mostrar el mensaje original y cifrado
    print("Mensaje original:", message)

    # Guardar el mensaje cifrado en un nuevo archivo
    with open('nuevo_archivo_unico.txt', 'w') as archivo:
        archivo.write(str(encrypted_message))

    # Mostrar el mensaje descifrado (descomenta si es necesario)
    print("Mensaje descifrado:", decrypted_message)

except IOError:
    print("Error: No se pudo acceder al archivo 'temporal.txt'. Verifica si existe y tienes permisos.")
except Exception as error:
    print("Se produjo un error: {}".format(error))


