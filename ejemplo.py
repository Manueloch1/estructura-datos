class Persona:
    altura: float
    def __init__(self, nombre: str, edad: int, altura: float):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
    def saludar(self):

        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

    def esMayor(self):
        return self.edad >= 18

    @staticmethod
    def esMayor(edad: int):
        return edad >= 18
    def __str__(self) -> str:
        return f" Persona(nombre={self.nombre},edad={self.edad},altura={self.altura})"
    
class Estudiante(Persona):
    def __init__(self, nombre: str, edad: int, altura: float, carrera: str):
        super().__init__(nombre, edad, altura)
        self.carrera = carrera

    def estudiar(self) -> str:
        return f"Hola, soy {self.nombre}, estudio {self.carrera}."

    def __str__(self) -> str:
        return f"Estudiante(nombre={self.nombre}, edad={self.edad}, carrera={self.carrera})"

    def getPromedio(self) -> float:
        return self.__promedio
    def setPromedio(self, promedio: float) -> None:
        self.__promedio = promedio


juan = Persona("Juan", 30, 1.75)
maria = Estudiante("Maria", 25, 1.65, "Ingeniería")
print(juan.saludar())
print(maria.estudiar())
juan.altura = 1.75
print(juan)
#print(maria._Estudiante__promedio) #Esto generará un error porque __promedio es privado