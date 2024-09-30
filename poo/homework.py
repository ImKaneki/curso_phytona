#crear una clase  banco sus atributos seran nombre apellidos deni numero de cuenrta
#y saldo inicial

#como metodos podremos hacer deposito retirar dinero y ver estado de cuenta

class banco:
    #atributos
    def __init__(self,nombre,apellidos,dni,numero_de_cuenta,saldo_inicial):
        self.nombre=nombre
        self.apellidos=apellidos
        self.dni=dni
        self.numero_de_cuenta=numero_de_cuenta
        self.saldo_inicial=saldo_inicial
    #metodos
    def deposito(self):
        print("estoy haciendo un deposito de 20")
    def retirar(self):
        print("estoy haciendo un retiro de 20")
    def get_status(self):
        print("estoy viendo el get status actual de mi cuenta")
juan=banco("juan","perez olarte",7455125,1220,1222)
print(juan.retirar())

#Ejercicio 02 I #Crear una clase agencia #con sus atributos nombre y apellidos del pasajero dni numero de asiento fecha de viaje 
# #sus metodos seran ingresar origen, ingresar destino, cancelar viaje, ver estado de pasaje
