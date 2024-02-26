import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su proximo desarrollo en python, 
que promete revolucionar el mercado. 
Las posibles aplicaciones son las siguientes: 
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA), 
# Internet de las cosas (IOT)  

Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:

Los datos a ingresar por cada encuestado son:
    * nombre del empleado
    * edad (no menor a 18)
    * genero (Masculino - Femenino - Otro)
    * tecnologia (IA, RV/RA, IOT)   

En esta opción, se ingresaran empleados hasta que el usuario lo desee.

Una vez finalizado el ingreso, mostrar:

    #! 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
    #! 2) - Tecnología que mas se votó.
    #! 3) - Porcentaje de empleados por cada genero
    #! 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  
    #! 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
    #! 6) - Nombre y género del empleado que voto por RV/RA con menor edad.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_validar_letra = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_validar_letra_on_click)
        self.btn_validar_letra.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_validar_letra_on_click(self):
        cont_masc_tecno= 0
        cont_iot= 0
        cont_ia=0
        cont_vr=0

        cont_masc=0
        cont_fem=0
        cont_otro=0

        cont_iot_edad=0

        cont_fem_ia=0
        acu_edad_fem=0

        primer_rv = 0

        seguir = True
        while seguir == True:
            nombre= prompt("aa", "Ingrese su nombre: ")
            edad= prompt("Edad", "Ingrese su edad: ")
            edad= int(edad)

            while edad < 18:
                edad= prompt("error", "Reingrese su edad: ")
                edad= int(edad)
            
            genero = prompt("genero", "Ingrese su genero: ")
            while genero!= "masculino" and genero!= "femenino" and genero!= "otro":
                genero= prompt("error", "reingrese su genero")
            
            tecnologia = prompt("tecno", "Ingrese la aplicación tecnologica que prefiera: ")
            while tecnologia!= "IA" and tecnologia!= "IOT" and tecnologia!= "RV/RA":
                tecnologia= prompt("error", "reingrese su genero")

#--------------------------------------------------------------------------------------------------------------------------------

            if genero == "masculino" and tecnologia == "IOT" or tecnologia =="IA" and edad >24 and edad <51:
                cont_masc_tecno+=1
            
            match tecnologia:
                case"IOT":
                    cont_iot+=1
                    if edad > 18 and edad < 25 or edad > 33 and edad <42:
                        cont_iot_edad +=1

                case"IA":
                    cont_ia+=1
                case _:
                    cont_vr+=1
                    if edad < minimo_edad or primer_rv == False :
                        minimo_edad= edad
                        nombre_minimo=nombre
                        genero_minimo=genero
                        primer_rv= True

            match genero:
                case"masculino":
                    cont_masc+=1
                case"femenino":
                    cont_fem+=1
                    if tecnologia=="IA":
                        cont_fem_ia+=1
                        acu_edad_fem+=edad

                case _:
                    cont_otro+=1
            


            seguir = question("Seguir", "Ingrese a otro empleado")


        if cont_iot > cont_ia and cont_iot > cont_vr:
            mensaje="Se votó mas IOT"
        elif cont_ia > cont_iot and cont_ia > cont_vr:
            mesaje= "Se votó mas IA"
        else:
            mensaje="Se votó mas RV/RA"

        tot_empleados= cont_masc + cont_fem + cont_otro
        
        porcentaje_femenino= (cont_fem*100)/tot_empleados                 #tambien se puede poner el porcentaje como: porcen_fem= 100 - (cont_masc+cont_otro) --- menos procesamiento del proce
        porcentaje_masculino= (cont_masc*100)/tot_empleados
        porcentaje_otro= (cont_otro*100)/tot_empleados

        porcentaje_iot_edad= (cont_iot_edad*100)/tot_empleados

        if cont_fem_ia > 0:
            prom_edad_femenino= acu_edad_fem/cont_fem_ia
        else:
            prom_edad_femenino= "No se ingresaron femeninos que votaran IA"

        alert("", f"Cantidad de masculinos que votaron IOT/IA: {cont_masc_tecno}")
        alert("", f"{mensaje}")
        alert("", f"Porcentaje: \n\ Masculino = {porcentaje_masculino}% \n\ Femenino = {porcentaje_femenino}% \n\ Otro = {porcentaje_otro}")
        alert("", f"El porcentaje de personas que votaron IOT y tienen cierto rango de edad es: {porcentaje_iot_edad}%")
        




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()