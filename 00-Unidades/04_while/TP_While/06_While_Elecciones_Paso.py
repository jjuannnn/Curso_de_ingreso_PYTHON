import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Juan Cruz
apellido: Leiva
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        cont_votos= 0
        cont_nombre= 0
        acu_edades= 0
        maximo= -1000
        nombre_max= ""

        while True:
            nombre= prompt("Nombre", "Ingrese el nombre del candidato que va a votar: ")
            if nombre == None:
                break

            edad= prompt("Edad", "Ingrese la edad del candidato: ")
            edad= int(edad)

            while edad < 25:
                edad= prompt("Error", "Escriba una edad valida")
                edad= int(edad)
            
            cont_nombre+=1
            cont_votos+=1

            if cont_votos > maximo:
                maximo=cont_votos
                nombre_max= nombre
            
        
        alert("asd",f"El candidato mas votado fue: {nombre_max}")


'''
            cont=0
        maximo= -1000
        minimo= 1000

        while True:
            num= prompt("Numero", "Ingrese un numero: ")

            if num == None:
                break

            num= int(num)

            if num > maximo:
                maximo= num
            if num < minimo:
                minimo= num
        
        self.txt_maximo.delete(0,100)
        self.txt_maximo.insert(0,maximo)
        self.txt_minimo.delete(0,100)
        self.txt_minimo.insert(0,minimo)

'''

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
