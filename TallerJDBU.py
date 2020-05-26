




#2

"""class Cuenta():
   def __init__(self, cedula,nombre,fecha,cantidad):
      self.__cedula=cedula
      self.__nombre=nombre
      self.__fecha=fecha
      self.__cantidad=cantidad

   def getcedula(self):
      return self.__cedula

   def getnombre(self):
      return self.__nombre

   def getfecha(self):
      return  self.__fecha

   def getcantidad(self):
      return self.__cantidad

   def setcedula(self,cedula):
      self.__cedula= cedula

   def setnombre(self,nombre):
      self.__nombre = nombre

   def setfecha(self,fecha):
      self.__fecha = fecha

   def setcantidad(self, cantidad):
      self.__cantidad = cantidad


cedula=1234
nombre="Duber"
fecha=2/12/2020
cantidad=2000



monto_a_ingresar=int(input("ingrese el monto: \n"))

ingresar_cantidad=monto_a_ingresar+cantidad
cantidad=monto_a_ingresar+cantidad
print(nombre,"la cantidad es:",cantidad)

monto_a_retirar=int(input("cunato va retirar:\n"))
cantidad=cantidad-monto_a_retirar
print(nombre,"su saldo es: \n",cantidad)"""




"""#3
class persona(peso, estatura):
    return peso / estatura**2
Nombre="Duber"
Apellido="Rodriguez"
Sexo="Masculino"
peso= float(input("Digite su peso por favor(kg): \n"))
estatura=float(input("digita tu estatura por favor (mts): \n"))
indice=persona(peso,estatura)
print(Nombre,"su indice  de masa corporal es:\n {}".format(indice))
if indice <20:
   print("ESTAS EN BAJO PESO")
elif indice <=25:
   print(" ES NORMAL")
elif indice >25:
   print(" ESTAS EN SOBREPESO")"""


""" #4
class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color {}, {} ruedas".format(self.color, self.ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindraje):
        self.color =color
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindraje = cilindraje

    def __str__(self):
        return "color {}, {} ruedas, {} Km/h, {} cc".format(self.color, self.ruedas,
                                                            self.velocidad,self.cilindraje)
Coche =Coche("Gris",4,180,1800)
print(Coche)

class Camioneta(Vehiculo):
    def __init__(self, color, ruedas, carga):
        self.color = color
        self.ruedas =ruedas
        self.carga = carga

    def __str__(self):
        return "color {}, {} ruedas, {} Kg".format(self.color,self.ruedas, self.carga)


Camioneta = Camioneta("Negro",4,1000)
print(Camioneta)

class Bicicleta(Vehiculo):
    def __init__(self,color, ruedas, tipo):
        self.color = color
        self.ruedas =ruedas
        self.tipo = tipo

    def __str__(self):
        return "color {}, {} ruedas, tipo: {}".format(self.color, self.ruedas, self.tipo)

Bicicleta = Bicicleta("verde", 2, "deporte")
print(Bicicleta)
class Motocicleta(Vehiculo):
    def __init__(self,color, ruedas,velocida,cilindraje):
        self.color = color
        self.ruedas = ruedas
        self.velocidad = velocida
        self.cilindraje = cilindraje

    def __str__(self):
        return "color {}, {} ruedas, {} Km/h, {} cc".format(self.color,self.ruedas,
                                                                         self.velocidad,self.cilindraje)

Motocicleta = Motocicleta("blanca", 2, 120, 200)
print(Motocicleta)

vehiculos = ["Gris","4 ruedas","180 km/h","1800 cc",
            "Negro", "4 ruedas", "1000kg"],["verde","2 ruedas","deporte",
            "blanca","2 ruedas","180 Km/h","200 cc"]

print(vehiculos[0])"""





