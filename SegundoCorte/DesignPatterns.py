#Design Paterns


# Creational Patterns
# Cómo se crean los objetos
#1. Singleton: permite que se cree solo una instancia de obejto
from abc import ABC, abstractmethod

class NoSingleton:
    pass

class Singleton:
# Atributo de clase que guarda una referencia a la instancia
#Una vez se cree
    _instance = None

    def __new__(cls,user, password):
        if cls._instance is None:
            #Crea una sola instancia de clase si esta no existe:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.__setattr__("user", user)
            cls._instance.__setattr__("password",password)
        return cls._instance 
    
    def getUser(this):
        return this.user
    
    def getPassword(this):
        return this.passaword
    
#Ejemplo con un objeto que maneja sesion: 

sesion1 = Singleton("Diego", "abcd1234")
sesion2 = Singleton("Diego2","abcd456")
print (f"{sesion1.getUser()}")
print(f"{sesion2.getUser()}")


# objeto1 = Singleton()
# objeto2 = Singleton()

# objeto3 = NoSingleton()
# objeto4 = NoSingleton()

# #Objeto 1 y objeto 2 son la misma instacnia de clase, es decir son el mismo objeto
# print(f"Objeto 1 es objeto 2?: {objeto1 is objeto2}")
# print(f"El objeto 1 es {objeto1}")
# print(f"El objeto 2 es: {objeto2}")

# print(f"El objeto 1 es {objeto3}")
# print(f"El objeto 2 es: {objeto4}")

#Structural
# Cómo se relacionan, de forma estructural


# 2. Abstract Factory:
#Permite creer familias de objetos relacionados sin especificar las subclases
#Ejemplo: abstract factory para crear elementos  de GUI:
class Button(ABC):
    @abstractmethod
    def click(this):
        psss
class Menu(ABC):
    @abstractmethod
    def Open(this):
        pass 

#Implementació de las clases concretas (Windows):
class WindowsUIButton(Button):
    def click(this):
        return "Me comporto como un bóton de windows"

class WindowsUIMenu(Menu):
    def Open(this):
        return "Me comporto como un menu de windows"

class LinuxIUButton(Button):
    def click(this):
        return "Me comporto como un bóton de Linux"

class LinuxUIMenu(Menu):
    def Open(this):
        return "Me comporto como un menu de Linux"
    
#CREAR EL ABSTRACT FACTORY:
class GUIAbstractFactory(ABC):

    @abstractmethod
    def createButton(this) -> Button:
    
    @abstractmethod
    def createMenu(this) -> Button:
        pass
#SE CREA UNA CONCRETE FACTORY PARA CADA CASO DE USO:
class WindowsFcatory(GUIAbstractFactory):
    def createButton(this) -> Button:
        return WindowsUIButton()
    
    def createMenu(this) -> Menu:
        return WindowsUIMenu()

class LinuxFactory(GUIAbstractFactory):
    def createButton(this) -> Button:
        return LinuxIUButton()
    def createMenu(this) -> Menu:
        return LinuxUIMenu()

#Clase cliente consume el abstract factory

def GUI_FactoryClient(os_type: str) -> GUIAbstractFactory:
    if os_type =="Windows":
        return WindowsFcatory

    elif os_type =="Linux":
        return LinuxFactory
    else:
        raise ValueError("Sistema Operativo no válido")
#Uso del patrón Abstract Factory:

factory = GUI_FactoryClient("Windows") #Cambia a "Windows" para otra interfaz
button = factory.create_button()
menu = factory.create_menu()

#Ejercicio: Abstract Factory para crear enemigos en un videojuego: easy, middle, nightmare


        
#Structurl
# Cómo se relacionan, de forma estructural
#3. Adapter

#Es un patrón que permite adaptar la comunicación entre objetos que tiene interfaces distintas
#Ejemplo:

class CelsiusTemperturaSensor:
    def getTempCelsius(this):
        return this.celsius_temp

class FahrenheitTemperaturaSensor:
    def getTempFahr(this):
        pass

#CLASE ADAPTADOR ENTRE LAS DOS CLASES:
#Se recibe como parámetro la clase A la cual se va adaptar la información de
# la clase  incompable
class TemperatureAdapter(FahrenheitTemperaturaSensor):

    #Se inicializa con la clase incompatible:
    def __init__(this, sensor):
        this.sensor
    #FUNCIÓN QUE ADAPTA DESDE NO COMPATIBLE PARA QUE EL CLIENTE LA PUEDA CONSUMIR
    def getTempFahr(this):
        #Código que adapta desde no compatible: 
        celsius= this.sensor.getTempCelsius()

        return celsius * (9/5) + 32

#Ejemplo de uso de la clase adaptadora:

sensor = CelsiusTemperturaSensor(23)
adaptador = TemperatureAdapter(sensor)
print(f"")

# 3. Decorator

#Behavioral Patterns
# Cómo se comportan entre ellos, y en el sistema. Idenfitica patrones de 
#comunicación entre objetos. 

# 5. Strategy

#6. Command
