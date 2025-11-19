#CBTis 89
#David Alejandro Macias Reyes
#Programacion 3°B

import tkinter as tk
from tkinter import ttk

#Ventana principal
ventana = tk.Tk()
ventana.title("List desplegable Combobox")
ventana.geometry("300x200")

#Etiqueta de instruccion
etiqueta = tk.Label(ventana, text="Elige una opcion: ")
etiqueta.pack(pady=10)

#Lista deplegable (Combobox)
opciones = ["Rojo", "Verde", "Azul","Amarillo", "Morado"]
ComboColores = ttk.Combobox(ventana, values=opciones, state="readonly")
ComboColores.pack(pady=5)

#Funcion que se ejecuta al seleccionar un elemento
def mostrar_seleccion(event):
    seleccion = ComboColores.get()   # Obtiene el valor seleccionado
    etiqueta_resultado.config(text=f"Seleccionaste: {seleccion}")

#Asociar evento al seleccionar un elemento
ComboColores.bind("<<ComboboxSelected>>", mostrar_seleccion)

#Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="Aun no has seleccionado nada")
etiqueta_resultado.pack(pady=20)

#Iniciar bucle principal
ventana.mainloop()
