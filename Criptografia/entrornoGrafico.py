# -*- coding: utf-8 -*-
import tkinter



root = tkinter.Tk()
root.title("Prueba de tkinter")
label = tkinter.Label(root, text="¡tkinter funciona correctamente!", font=("Arial", 14))
label.pack(pady=20)
root.mainloop()