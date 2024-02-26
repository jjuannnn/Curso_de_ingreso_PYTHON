import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        cont_p = 0
        acu_p = 0
        cont_n = 0
        acu_n = 0
        cont_ceros = 0

        while True:
            numero = prompt("", "Ingrese un numero: ")

            if numero is None:
                break

            numero = int(numero)

            if numero > 0:
                cont_p += 1
                acu_p += numero
            elif numero < 0:
                cont_n += 1
                acu_n += numero
            else:
                cont_ceros += 1

        diferencia = cont_p - cont_n

        alert("Numeros", f"La cantidad de numeros negativos es: {acu_n}. La cantidad de numeros positivos es: {acu_p}. La cantidad de numeros positivos acumulados es: {cont_p}. La cantidad de numeros negativos acumulados es: {cont_n}. La cantida de ceros es: {cont_ceros}. La diferencia entre numeros positivos y numeros negativos es: {diferencia}")
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
