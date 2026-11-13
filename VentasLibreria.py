import Librerias.salir as sal
import Librerias.operacionesaritmeticas as opa

global contMasc, contFem, contTotalClien, cantMascMayMil, acumTotalVentas, acumVentasFem
global MontoPago, MontoBruto, MontoBono, MontoDscto
contMasc = 0
contFem = 0
contTotalClien = 0
cantMascMayMil = 0
acumTotalVentas = 0
acumVentasFem = 0
 

def Reportar():
    print("\n============ REPORTAR =================\n")
    print(f"La cantidad Total de Clientes es: {contTotalClien}")
    print(f"La cantidad de Clientes Femeninos: {contFem}")
    print(f"La cantidad de Clientes Masculinos: {contMasc}")
    print(f"La cantidad de clientes Macsulino, acumulado >= 1000 es: {cantMascMayMil}")
    print(f"El total de ventas es: {acumTotalVentas}")
    print(f"El acumulado total de ventas de cliente femenino es: {acumVentasFem}")

def sumar():
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))

    num3 = num1+num2
    print(f"La suma de los dos numero es: {num3+1}")
    #ESTO SE AGREGO

def Procesar():
    global contMasc, contFem, contTotalClien, cantMascMayMil, acumTotalVentas, acumVentasFem
    global MontoPago, MontoBruto, MontoBono, MontoDscto

    nombreProd = input("Ingrese el nombre del producto:\t")

    while True:
        precioProd = float(input("Ingrese el precio del producto:\t"))
        if precioProd < 1:
            print("Error, ingrese nuevamente...")
        else: 
            break
    while True:
        cantProd = int(input("Ingrese la cantidad del producto:\t"))
        if cantProd < 1:
            print("Error, ingrese nuevamente...")
        else:
            break
    while True:
        porcDscto = float(input("Ingrese el porcentaje de descuento:\t"))
        if porcDscto < 0:
            print("Error, ingrese nuevamente...")
        else:
            break
    while True:
        genero = input("Ingrese el genero del cliente (F / M):\t").upper()
        if genero != 'F' or genero != 'M':
            print("Error, ingrese nuevamente...")
        else:
            break
    match genero:
        case 'M':
            contMasc += 1

            bono = 0.18
            if cantProd <=10:
                dcto = 0.2
            else:
                dcto = 0.5

        case 'F':
            contFemF += 1

            bono = 0.25
            if cantProd <=10:
                dcto = 0.3
            else:
                dcto = 0.4

    MontoBruto = opa.multiplica(precioProd, cantProd)
    MontoBono = opa.multiplica(MontoBruto, bono)
    MontoDscto = opa.multiplica(MontoBruto, porcDscto)
    MontoPago = opa.sumar(opa.restar(MontoBruto, MontoDscto),MontoBono)

    contTotalClien += 1
    acumTotalVentas = opa.sumar(acumTotalVentas, MontoPago)

    if genero == 'F':
        acumVentasFem += MontoPago
    
    if genero == 'M' and acumTotalVentas >= 1000:
        cantMascMayMil =+ 1
    
    print("\n ============ REPORTE POR CLIENTE =================\n")
    print(f"El Monto Bruto: {MontoBruto}")
    print(f"El Monto Bono:  {MontoBono}")
    print(f"El Monto Descuento: {MontoDscto}")
    print(f"El Monto a Pagar: {MontoPago}")

def Menu():
    print("\n============ MENU OPCIONES =================\n")
    print("1. Procesar")
    print("2. Reportar")
    print("3. Salir")
    print("4. Sumar") #<----- ACA

    while True:
        op = int(input("Ingrese una opcion:\t"))
        if op <1 or op>4:
            print("Error, ingrese una opcion correcta")
        else:
            break
    match op:
        case 1:
            Procesar()
        case 2:
            Reportar()
        case 4:
            sumar()
        case 3:
            while True:
                salir = input("Desea Salir (S/N):\t").upper()
                if salir != "S" and salir !="N":    #<----- Ya arregle mi error de que no podia salir, esto es para mi segundo commit
                    print("Error, ingrese nuevamente...")
                else:
                    break
            if salir == "S":
                sal.salir()
            else:
                Menu()
    return op

def ejecutar():
    while True:
        opcion = Menu()
        if opcion == 3:
            break

ejecutar()
