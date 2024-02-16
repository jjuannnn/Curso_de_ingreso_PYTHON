import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Juan Cruz
apellido: Leiva
---
Ejercicio: Match_09
---
Una agencia de viajes cobra $15.000 por cada estadía como base. 
Luego para calcular las tarifas total realiza el siguiente cálculo, 
en función de la estación del año y del destino elegido:
    Si es invierno: 
        Bariloche tiene un aumento del 20% 
        Cataratas y Córdoba tienen un descuento del 10%
        Mar del plata tiene un descuento del 20%
    Si es Verano:
        Bariloche tiene un descuento del 20%
        Cataratas y Cordoba tienen un aumento del 10%
        Mar del plata tiene un aumento del 20%
    Si es Primavera u Otoño:
        Bariloche tiene un aumento del 10%
        Cataratas tiene un aumento del 10%
        Mar del plata tiene un aumento del 10%
        Córdoba tiene precio sin descuento

'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_estaciones = customtkinter.CTkLabel(master=self, text="Estaciones")
        self.label_estaciones.grid(row=0, column=0, padx=20, pady=10)
        estaciones = ['Verano', 'Otoño', 'Invierno', 'Primavera']
        self.combobox_estaciones = customtkinter.CTkComboBox(master=self, values=estaciones)
        self.combobox_estaciones.grid(row=1, column=0, padx=20, pady=(10, 10))

        
        self.label_destinos = customtkinter.CTkLabel(master=self, text="Destinos")
        self.label_destinos.grid(row=2, column=0, padx=20, pady=10)
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Cordoba']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=3, column=0, padx=20, pady=(10, 10))

        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        estaciones= self.combobox_estaciones.get()
        destino= self.combobox_destino.get()
        estadia= 15000
        match estaciones:
            case "Invierno":
                if destino == "Bariloche":
                    aumento= estadia * 0.20
                    descuento=0
                elif destino == "Cataratas":
                    aumento=0
                    descuento=estadia * 0.10
                elif destino == "Cordoba":
                    aumento=0
                    descuento=estadia * 0.10
                else:
                    aumento=estadia * 0.20
                    descuento=0

            case "Verano": 
                if destino == "Bariloche":
                    aumento=0
                    descuento= estadia * 0.20
                elif destino == "Cataratas":
                    aumento=estadia * 0.10
                    descuento=0
                elif destino == "Cordoba":
                    aumento=estadia * 0.10
                    descuento=0
                else:
                    aumento=estadia * 0.20
                    descuento=0

            case _: 
                if destino == "Bariloche":
                    aumento= estadia * 0.10
                    descuento=0
                elif destino == "Cataratas":
                    aumento=estadia * 0.10
                    descuento=0
                elif destino == "Cordoba":
                    aumento=0
                    descuento=0
                else:
                    aumento=estadia * 0.10
                    descuento=0
                
            
        precio_final= estadia + aumento - descuento

        alert("Viaje", f"El viaje tendria el siguiente valor: {precio_final} ")
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()