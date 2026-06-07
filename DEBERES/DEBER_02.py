class Persona:

    def __init__(self,nombre,edad,sexo,altura):
        #Variable de instancia
        self.nombre = nombre 
        self.edad= edad
        self.sexo= sexo
        self.altura= altura
    
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"edad: {self.edad}")
        print(f"sexo: {self.sexo}")
        print(f"altura: {self.altura}")
        
    def saltar(self):
        print(f"{self.nombre} esta saltando")
    
    def correr(self):
        print(f"{self.nombre} esta corriendo")

mi_persona = Persona("Antony",24,"masculino",1.83)
mi_otra_persona = Persona("Marliz",23,"femenino",1.67)

mi_persona.saltar()
mi_otra_persona.correr()


    