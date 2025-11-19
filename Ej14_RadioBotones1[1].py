# CBTis 89
# 3°B Programacion
# Macias Reyes David Alejandro
#Ej14_RadioBotones1

import tkinter as tk

#Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calcular Descuentos")
ventana.geometry("400x300")
ventana.resizable(False, False) #Evita que el usuario cambie el tamaño de la ventana

#Etiqueta y caja d texto

#Creamos una etiqueta que indica que debe escribir el usuario
etiqueta_cantidad = tk.Label(ventana, text="Ingresa la cantidad: ")
etiqueta_cantidad.pack(pady=10)

#Caja de texto donde se escribira la cantidad
entrada_cantidad = tk.Entry(ventana, justify="center")
entrada_cantidad.pack()

#Funcion que se ejecuta al seleccionar un boton
def ejecutar_radio():
opcion = seleccion.get()

if opcion == 1:
    cantidad = float(entrada_cantidad.get())
    descuento = cantidad * 0.05
    etiqueta_resultado.config(text=f"Hola estimado cliente usted obtuvo un Descuento del 5%, el cual equivale a : ${descuento:.2f}")

elif opcion == 2:    
    cantidad = float(entrada_cantidad.get())
    descuento = cantidad * 0.10
    etiqueta_resultado.config(text=f"Hola estimado cliente usted obtuvo un Descuento del 10%, el cual equivale a : ${descuento:.2f}")

elif opcion == 3:    
    cantidad = float(entrada_cantidad.get())
    descuento = cantidad * 0.15
    etiqueta_resultado.config(text=f"Hola estimado cliente usted obtuvo un Descuento del 15%, el cual equivale a : ${descuento:.2f}")

#Variable para almacenar la opcion seleccionada 
seleccion = tk.IntVar()

#Crear los radios buttons
radioB1 = tk.Radiobutton(ventana, text="Descuento del 5%", variable=seleccion, value=1, command=ejecutar_radio)
radioB2 = tk.Radiobutton(ventana, text="Descuento del 10%", variable=seleccion, value=2, command=ejecutar_radio)
radioB3 = tk.Radiobutton(ventana, text="Descuento del 15%", variable=seleccion, value=3, command=ejecutar_radio)

#Mostrar los radio buttons en la ventana
radioB1.pack(pady=10)
radioB2.pack(pady=10)
radioB3.pack(pady=10)

#Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="", wraplength=350, justify="left")
etiqueta_resultado.pack(pady=20)

#Iniciar la aplicacion
ventana.mainloop()