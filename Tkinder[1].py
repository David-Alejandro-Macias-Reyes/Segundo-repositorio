import tkinter as tk

# ventana principal
ventana = tk.Tk()
ventana.title("Sistema de nombres")
ventana.geometry("400*300")

etiquet = tk.Label(ventana, text="Nombre: ", font=("Arial", 13))
etiquet.pack(pady=10)

entrada = tk.Entry(ventana,font=("Arial",12))
entrada.pack(pady=5)

etiqueta = tk.Label(ventana, text="Apellido: ", font=("Arial", 13))
etiqueta.pack(pady=10)

entrada = tk.Entry(ventana,font=("Arial",12))
entrada.pack(pady=5)


def mostrar_texto():
    texto = entrada.get()
    texto2 = entrada.get()
    etiqueta_resultado.config(text=f"Tu nombre es: {texto} {texto2}")

boton = tk.Button(ventana, text="Mostrar Nombre", command=mostrar_texto)
boton.pack(pady=10)

etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12), fg="green")
etiqueta_resultado.pack(pady=5)

ventana.mainloop()