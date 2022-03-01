# MAIN_RBG

from random import randrange
import sys
import tkinter

def MostrarMenu():
    print("""        ##################################
        #         Que vols fer:          #
        # 1.- Calculadora                #
        # 2.- Calcul de inversions       #
        # 3.- Número al atzar            #
        # 4.- Numeros romans             #
        # 5.- Taula de multiplicar       #
        # 6.- Calcular el IMC            #
        # 7.- Sortir                     #
        ##################################""")

#1.-CALCULADORA
def MostrarMenuCalculadora():
    print("""        ##################################
        #         Que vols fer:          #
        # 1.- Sumar                      #
        # 2.- Restar                     #
        # 3.- Multiplicar                #
        # 4.- Dividir                    #
        # 5.- Sortir                     #
        # 6.- Tornar menu principal      #
        ##################################""")


def LeerNumero(texto):
    leido = False
    while not leido:
        try:
            numero = float(input(texto))
        except ValueError:
            print("Error: Tens que introduir un número.")
        else:
            leido = True
    return numero

#Calculadora suma
def suma():
    numero1 = LeerNumero("Introdueix el primer valor a sumar\n")
    numero2 = LeerNumero("Introdueix el segon valor a sumar\n")
    print("\n", numero1, " + ", numero2, " = ", numero1+numero2, "\n")

#Caluculadora resta
def resta():
    numero1 = LeerNumero("Introdueix el primer valor\n")
    numero2 = LeerNumero("Introdueix el número a restar\n")
    print("\n", numero1, " - ", numero2, " = ", numero1-numero2, "\n")

#Calculadora multiplicacio
def multiplicacio():
    numero1 = LeerNumero("Introdueix el primer valor a mutiplicar\n")
    numero2 = LeerNumero("Introdueix el segon valor a mutiplicar\n")
    print("\n", numero1, " * ", numero2, " = ", numero1*numero2, "\n")

#Calculadora divisio
def divisio():
    numero1 = LeerNumero("Introdueix el divident\n")
    numero2 = LeerNumero("Introduce el divisor\n")
    try:
        resultat = numero1/numero2
    except ZeroDivisionError:
        print("Error! No es pot dividir per 0\n")
    else:
        print("\n", numero1, " / ", numero2, " = ", round(resultat, 2), "\n")

#main calculadora
def Calculadora():
    fin = False
    while not fin:
        MostrarMenuCalculadora()
        opcio = int(input("\n            Seleccioni una opció:"))
        if(opcio == 1):
            suma()
        elif(opcio == 2):
            resta()
        elif(opcio == 3):
            multiplicacio()
        elif(opcio == 4):
            divisio()
        elif(opcio == 5):
            print("Adeu!")
            exit()
        elif(opcio == 6):

            fin = True
    print("¡Adeu!")

# 2.- CALCUL DE INVERSIONS

def CalculInversions():
    capitalinicial = int(input("\nDis-me el capital inicial a invertir:"))
    interesanual = float(input("\nDis-me el interes %: "))
    anys = float(input("\nDis-me el numero de anys: "))
    interes = capitalinicial*interesanual*anys/100
    capitalfinal = capitalinicial + interes
    print(
        f"Quan finalitzi el periode tindrás un capital de: {capitalfinal} \n")

# 3.- NUMERO AL ATZAR


def atzar():
    fin = False
    while not fin:
        try:
            minim = int(input("Dis-me el número minim que pot sortir : "))
            maxim = int(input("\nDis-me el númro máxim que pot sortir : "))
            fin = True
        except:
            print("Error, han de ser dos números han sencers")
    print(f"\n\tUn número al atzar entre {minim} i {maxim} és el {randrange(minim,maxim)} \n")

#4.- numeros romanos :

class Romano(object):
    def __init__(self, numero):
        self.number = str(numero)
        self.largo = len(self.number)
    def romanizar (self):
        respuestafinal = ''
        for x in range(0,self.largo):
            respuestafinal = respuestafinal + self.romanizardig(self.number[x],self.largo-x-1)
        return respuestafinal
    def romanizardig(self,digito,categoria):
        popurri = {0:'',1:'0',2:'00',3:'000',4:'01',5:'1',6:'10',7:'100',8:'1000',9:'02'}
        categorias = [['I','V','X'],['X','L','C'],['C','D','M']]
        logica = categorias[categoria]
        respuesta = ''
        dig_a_procesar = [x for x in popurri[int(digito)]]
        for x in dig_a_procesar:
            respuesta = respuesta + logica[int(x)]
        return respuesta
popurri = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
class Normalizador(object):
    #Entrem numero i logitud
    def __init__(self, numero):
        self.number = numero
        self.largo = len(numero)
    def normalizar(self):
        popurri = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sumatotal = 0
        #mentres hi haixin dades...
        for x in range(0,self.largo):
            valor = popurri[self.number[x]]
            #agafa el numero roma
            if x != self.largo-1:
                #si esta abans del numero mes gran:
                if valor < popurri[self.number[x+1]]:
                    valor = -valor
                    #print (menos)#mod
            sumatotal += valor
        return (sumatotal)
def NumerosRomanos():
    fin = 1
    while fin == 1 or fin ==2 or fin ==3:
        try:
            opc = int(input("""
        1.-Passar de números romans a arabs
        2.-Passar de múmeros arabs a romans
        3.-Anar al menu principal\n\t\t\t\t
                    Seleccioni una opció:"""))
        except:
            print("Error, sols s'atmet els números 1 2 o 3")
            continue
        if opc == 1:
            text = str(input("Fica el número romá:"))
            Prueba = Normalizador(text)
            print (Prueba.normalizar())
        elif opc == 2:        
            text = input("Fica el número arab:")
            Prueba = Romano(text)
            print (Prueba.romanizar())
        elif opc ==3:
            fin = True
            main()
        else:
            fin = False
            
# 5.- TAULA DE MULTIPLICAR
def taula():
    x = int(input('De quin nùmero vols saber la taula?\n'))
    for y in range(10):
        print(x, "* {} = {}".format(y, y*x))
# 6.- IMC

#6.-IMC
def imc():
    pes = float(input("Dis-me el teu pes amb Kgs: "))
    alçada = float(input("Dis-me la teva alçada amb cms: \n"))
    alçada = alçada/100
    try:
        imc = (pes/((alçada)**2))
        imc = round(imc, 2)
    except ZeroDivisionError:
        print("Error! No es pot dividir per 0\n")
    else:
        print("El teu index de masa corporal es:" + str(imc), "\n")
        if imc > 30:
            print("Tens obesitat.\n")
        elif imc >= 25 and imc <= 30:
            print("Tens sobrepes.\n")
        else:
            print("Tens un pes saludable, felicitats!\n")


def main():
    fin = False
    while not fin:
        MostrarMenu()
        try:
            opcion = int(input("\n            Seleccioni una opció:"))
        except:
            print("Error, ha de ser un número sencer")
        if(opcion == 1):
            Calculadora()
        elif(opcion == 2):
            CalculInversions()
        elif(opcion == 3):
            atzar()
        elif(opcion == 4):
            NumerosRomanos()
        elif(opcion == 5):
            taula()
        elif(opcion == 6):
            imc()
        elif(opcion == 7):
            fin = True
    print("¡Adeu!")


main()
