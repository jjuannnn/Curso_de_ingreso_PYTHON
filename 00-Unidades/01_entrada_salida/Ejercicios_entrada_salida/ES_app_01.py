import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''

Simulacro Turno Tarde

Un gimnasio quiere medir el progreso de sus clientes, para ello se debe ingresar:

 

Nombre

Edad (debe ser mayor a 12)

Altura (no debe ser negativa)

Días que asiste a la semana (1, 3, 5)

Kilos que levanta en peso muerto (no debe ser cero, ni negativo)

 

No sabemos cuántos clientes serán consultados.

Se debe informar al usuario:

El promedio de kilos que levantan las personas que asisten solo 3 días a la semana.

El porcentaje de clientes que asiste solo 1 día a la semana.

Nombre y edad del cliente con más altura.

Determinar si los clientes eligen más ir 1, 3 o 5 días

Nombre y cantidad de kilos levantados en peso muerto, de la persona más joven que solo asista 5 días a la semana.

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        miembros= 0
        un_dia=0
        tres_dias=0
        cinco_dias=0
        acu_kilos=0
        tres_dias_kilos= 0

        while True:
            nom= prompt("Nombre", "Ingrese su nombre: ")

            if nom == None:
                break

            edad= prompt("Edad", "Ingrese su edad: ")
            edad= int(edad)

            while edad<12:
                edad= prompt("Error", "Edad invalida, tiene que ser mayor que 12")
                edad= int(edad)
            
            altura= prompt("aLTURA", "ingrese su altura")
            altura= float(altura) 

            while altura < 0:
                altura= prompt("Error", "La altura no puede ser negativa, reingresela")
                altura= float(altura) 

            dia= prompt("Dia", "Ingrese que día entrena (1, 3 o 5)")
            dia= int(dia)

            while dia != 1 and dia != 3 and dia != 5:
                dia= print("Error","Ingrese un día valido")
            
            kilos= prompt("Kilos", "Ingrese los kilos que levanta: ")
            kilos= int(kilos)

            while kilos < 1:
                kilos= prompt("Error", "Los no kilos pueden ser negativos o 0, reingreselos")
                kilos= int(kilos) 

            miembros+=1
            acu_kilos= kilos
        
            match dia:
                case 1:
                    un_dia+=1
                case 3:
                    tres_dias+=1
                    tres_dias_kilos= kilos
                case _:
                    cinco_dias+=1

        if un_dia > tres_dias and un_dia > cinco_dias:
            mensaje= "La gente suele ir 1 dia"
        elif tres_dias > un_dia and tres_dias > cinco_dias:
            mensaje= "La gente suele ir 3 dias"
        else:
            mensaje="La gente suele ir 5 dias"    


        porcentaje_un_dia= (un_dia * 100) / miembros
        promedio_kilos= acu_kilos/tres_dias  

        alert("", f"El promedio de kilos que levatan las personas que van 3 días a la semana son: {tres_dias_kilos} \nEl porcentaje de personas que asisten un día a la semana es: {porcentaje_un_dia}% \n{mensaje}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
