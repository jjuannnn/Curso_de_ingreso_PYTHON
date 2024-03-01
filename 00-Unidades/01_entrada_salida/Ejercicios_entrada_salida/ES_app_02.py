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

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        cont_miembros=0

        dia1= 0
        dia3= 0
        dia5= 0
        
        acu_kilos=0
        acu3= 0
        bandera_primer_ing= False
        altura_max= 0
        nombre_mas_alto= ""
        edad_persona_alta= 0 

        bandera_dia_5= False
        edad_joven_5 = 0
        nombre_joven_5= ""
        kilos_joven_5= 0

        while True:

            nombre= prompt("Nombre", "Ingrese su nombre")

            if nombre == None:
                break

            edad= int(prompt("Edad", "Ingrese su edad: "))

            while edad<12: 
                edad=prompt("Error", "Tenes que ser mayor que 12")
                edad=int(edad)

            altura= float(prompt("Altura", "Ingrese su altura"))

            while altura<0:
                altura=prompt("Error", "La altura no puede ser negativa")
                altura=float(altura)
            
            dia= int(prompt("Día", "Cuantos días asiste a la semana?"))

            while dia !=1 and dia !=3 and dia !=5:
                dia=prompt("Error","Elija un día valido (1, 3 o 5)")
                dia=int(dia)

            kilos= int(prompt("Kilos", "Ingrese los kilos"))

            while kilos<1:
                kilos=prompt("Error", "Los kilos no pueden ser negativos y deben ser mas de 1")
                kilos=int(kilos)
            
            cont_miembros+=1

            match dia:
                case 1:
                    dia1 += 1
                case 3:
                    dia3 += 1
                    acu3 +=kilos
                case _:
                    dia5 += 1
                    if bandera_dia_5 == False:
                        edad_joven_5 = edad
                        nombre_joven_5 =nombre
                        kilos_joven_5 = kilos
                        bandera_dia_5 = True
                    elif edad < edad_joven_5:
                        edad_joven_5 = edad
                        nombre_joven_5 =nombre
                        kilos_joven_5 = kilos
            
            if altura > altura_max or bandera_primer_ing == False: 
                    altura_max = altura
                    nombre_mas_alto =nombre
                    edad_persona_alta = edad
                    bandera_primer_ing = True

        if dia1>dia3 and dia1>dia5:
            mensaje="La gente va mas un día"
        elif dia3>dia1 and dia3>dia5:
            mensaje="La gente va mas 3 días"
        else:
            mensaje="La gente va mas 5 días"
        
        promedio_kilos= acu3/dia3
        porcentaje_undia= (dia1*100)/cont_miembros
            
        alert("Mensaje", f"El promedio de kilos de las personas que van 3 días a la semana es de: {promedio_kilos}") 
        alert("Mensaje", f"El porcentaje de gente que va 1 día es de: {porcentaje_undia}%")
        alert("Mensaje", f"El nombre de la persona mas alta es {nombre_mas_alto} y su edad es {edad_persona_alta}")
        alert("Mensaje", f"{mensaje}")
        alert("Mensaje", f"El nombre de la persona mas joven que asiste 5 días es {nombre_joven_5} y levanta {kilos_joven_5}")



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()