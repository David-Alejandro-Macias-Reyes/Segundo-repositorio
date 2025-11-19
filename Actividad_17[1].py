# CBTis 89
# Macias Reyes David Alejandro
# Programacion 3°B
# Operaciones

import tkinter as tk



def sumar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        suma = num1 + num2 
        resultado.config(text=f"Resultado de la suma:  {suma}")
    except ValueError:
        resultado.config(text="Por favor, ingresa solo numeros")
        
def restar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resta = num1 - num2 
        resultado.config(text=f"Resultado de la suma:  {resta}")
    except ValueError:
        resultado.config(text="Por favor, ingresa solo numeros")
        
def multiplicar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        producto = num1 * num2 
        resultado.config(text=f"Resultado de la suma:  {producto}")
    except ValueError:
        resultado.config(text="Por favor, ingresa solo numeros")   
        
def dividir():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        if num2 == 0:
            resultado.config(text="No se puede dividir entre cero")
        else:
            division = num1 / num2     
        resultado.config(text=f"Resultado de la suma:  {division}")
    except ValueError:
        resultado.config(text="Por favor, ingresa solo numeros")  
        
# Creacion de la ventana 
ventana = tk.Tk()
ventana.title("Menu de Operaciones")
ventana.geometry("350x300")

#Creacion de los cuadros de texto
entrada1 = tk.Entry(ventana) 
entrada2 = tk.Entry(ventana)
entrada1.pack(pady=5)                  
entrada2.pack(pady=5)

#Creacion de los botones de las operaciones 
boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack(pady=5)

boton_restar = tk.Button(ventana, text="Restar", command=restar)
boton_restar.pack(pady=5)      

boton_multi = tk.Button(ventana, text="Multiplicar", command=multiplicar)
boton_multi.pack(pady=5)

boton_divi = tk.Button(ventana,text="Dividir", command=dividir)
boton_divi.pack(pady=5)

#Creacion de la etiqueta que muestra el resultado
resultado = tk.Label(ventana, text="Resultado: ")
resultado.pack(pady=10)

#Ejecucion del programa
ventana.mainloop()