import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import math

'''
nombre:
apellido:
---
Ejercicio: entrada_salida_01
---
Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar en la bolsa de 
valores:

Para ello deberás programar el botón  para poder cargar 10 operaciones de compra con los siguientes datos:
    * Nombre
    * Monto en pesos de la operación (no menor a $10000)
    * Tipo de instrumento(CEDEAR, BONOS, MEP) 
    * Cantidad de instrumentos  (no menos de cero) 
    
Realizar los siguientes informes:
 
    #! 1) - Tipo de instrumento que menos se operó en total.
    #! 2) - Cantidad de usuarios que compraron entre 50  y 200 MEP 
    #! 3) - Cantidad de usuarios que no compraron CEDEAR 
    #! 4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
    #! 5) - Nombre y posicion del usuario que invirtio menos dinero
    #! 6) - Promedio de dinero en CEDEAR  ingresado en total.  
    #! 7) - Promedio de cantidad de instrumentos  MEP vendidos en total

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        cont_pacientes: 0

        cont_cedear=0
        cont_bonos=0
        cont_mep=0
        
        while True:
            nombre= prompt("Nombre","Ingrese su nombre")

            if nombre == None:
                break

            monto= int(prompt("Monto", "Ingrese el monto de la operacion"))
            while monto<10000:
                monto=prompt("Error", "El monto no puede ser menor a 10000")

            instrumento= prompt("Instrumento", "Ingrese el tipo de instrumento (CEDEAR, BONOS, MEP)")
            while instrumento != "CEDEAR" and instrumento != "BONOS" and instrumento != "MEP":
                instrumento= prompt("Error", "Escriba una opcion valida")

            cant_instru= int(prompt("Cantidad", "Ingrese la cantidad de instrumentos: "))
            while cant_instru<0:
                cant_instru=prompt("Error", "La cantidad de instrumentos tiene que ser mas que 0")
                cant_instru= int(cant_instru)

            cont_pacientes+= 1

            match instrumento: 
                case "CEDEAR":
                    cont_cedear+=1
                case "BONOS":
                    cont_bonos+=1
                case _:
                    cont_mep+=1

        if cont_cedear<cont_bonos and cont_cedear<cont_mep:
            mensaje="El menos usado fue CEDEAR"
        elif cont_bonos<cont_cedear and cont_bonos<cont_mep:
            mensaje="El menos usado fue BONOS"
        else: 
            mensaje="El menos usado fue MEP"

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()