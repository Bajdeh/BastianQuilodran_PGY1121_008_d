import datetime
import numpy
platinum = 120000
gold = 80000
silver = 50000
total = 0
cont_platinum = 0
cont_gold = 0
cont_silver = 0
total_platinum= 0
total_gold = 0
total_silver = 0
concierto = numpy.zeros((10,10),int)
listarut=[]
fecha_actual = datetime.datetime.now()
def menu():
    while True:
        print("""
        1.Comprar entradas
        2.Mostrar ubicaciones disponibles
        3.Ver listado de asistentes
        4.Mostrar Ganancias totales
        5.Salir""")
        return
    
def validar_opcion():
    while True:
        try:
            opc=int(input("Ingrese la opcion que necesite(1-5): "))
            if opc in (1,2,3,4,5):
                return opc
            else:
                print("Debe ingresar una opcion de 1 hasta 5")
        except:
            print("Ingrese numeros enteros")
def validar_rut():
    while True:
        try:
            rut=int(input("Ingrese su rut (sin digito verificador)"))
            if len(str(rut)) == 8:
                print("Su rut fue guardado correctamente")
                listarut.append(rut)
                return rut
            else:
                print("Ingrese un rut valido")
        except:
            print("Ingrese numeros enteros")
def mostrar_concierto():
    for x in range(10):
        print(f"fila:{x+1}",end=" ")
        for y in range(10):
            print(concierto[x][y],end=" ")
        print()
        print()        
def cant_entradas():
    
    while True:
        try:
            cant=int(input("Ingrese cantidad de entradas(1-3): "))
            if cant >= 1 and cant <=3:
                return cant
            else:
                print("Ingrese una cantidad valida")
        except:
            print("Ingrese numeros enteros")
      
def fila():
    while True:
        try:
            fil=int(input("Ingrese su fila: "))
            if fil in range(0,9):
                print("Su fila fue guardada con exito")
                return fil
            else:
                print("Ingrese un valor valido")
        except:
            print("Ingrese un numero entero")
def columna():
    global total_platinum
    global total_gold
    global total_silver
    global cont_gold
    global cont_platinum
    global cont_silver
    while True:
        try:
            colum=int(input("Ingrese su columna: "))
            if colum in range(0,19):
                total_platinum = total_platinum +(platinum*cant_entradas())
                cont_platinum = cont_platinum + cant_entradas()
                print("Su valor es de: ",total_platinum)
                return colum
            elif colum in range(20,49):
                total_gold = total_gold + (gold*cant_entradas())
                cont_gold = cont_gold + cant_entradas()
                print("Su valor es de: ",total_gold)
                return colum
            elif colum in range(50,99):
                total_silver = total_silver + (silver*cant_entradas())
                cont_silver = cont_silver + cant_entradas()
                print("Su valor es de : ",total_silver)
                return colum
            else:
                print("Ingrese una columna valida")
        except:
            print("Ingrese un valor entero")
      
def salir():
    print(f"Mi nombre es Bastian Quilodran y la fecha de hoy es: {fecha_actual}")
    return 


def ver_listadorut():
    listarut.sort
    listarut.reverse
    print(listarut)


def comprastotales():
    print("El total de Platinum fue: ",total_platinum)
    print("El total Gold fue de :",total_gold)
    print("El total de silver fue de", total_silver)
    print("TOTAL : ",total)

def compra():
    if columna() == 0 and fila() == 0:
        print("El asiento a sido reservado para usted")
    else:
        print("El asiento está ocupado")