import tkinter as tk
from tkinter import Toplevel

ventana_principal = tk.Tk()
ventana_principal.title("Ventana Principal")
ventana_principal.geometry("300x200")

def abrir_ventana_1():
    ventana_1 = Toplevel(ventana_principal)
    ventana_1.title("Ventana 1")
    ventana_1.geometry("250x150")

    etiqueta = tk.Label(ventana_1, text="David Alejandro Macias Reyes", font=("Arial", 12))
    etiqueta.pack(pady=10)
    
    boton_cerrar = tk.Button(ventana_1, text="Cerrar", command=ventana_1.destroy)
    boton_cerrar.pack(pady=10)

boton_abrir = tk.Button(ventana_principal, text="Boton 1", command=abrir_ventana_1)
boton_abrir.pack(pady=20)  

def abrir_ventana_2():
    ventana_2 = Toplevel(ventana_principal)
    ventana_2.title("Ventana 2")
    ventana_2.geometry("250x150")

    etiqueta = tk.Label(ventana_2, text="Programado con Python", font=("Arial", 12))
    etiqueta.pack(pady=10)
    
    boton_cerrar = tk.Button(ventana_2, text="Cerrar", command=ventana_2.destroy)
    boton_cerrar.pack(pady=10)

boton_abrir = tk.Button(ventana_principal, text="Boton 2", command=abrir_ventana_2)
boton_abrir.pack(pady=20)

ventana_principal.mainloop()