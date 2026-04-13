print("Dejenme renunciar al MacDonaaaaaaaal")

# Creando variables

titulo="clima de hoy" #string
diaDelmes=13 #int
mes=4 #int
temperatura = 22.3 #float
llueve=False #boolean

print(titulo)
print("Dia del mes ", diaDelmes)
print("Estamos en el mes ", mes)
print("La temperatura es ", temperatura, " grados")
if llueve==True:
    print("Hoy debe llevar paraguas")
else: 
    print("Hoy se puede llevar polera mangacorta")

# ej 1

sas=0
pin=3435
pas="temu"
while sas<3:

    print("Hola usuario. por favor ingrese el  pin de cuatro digitos: ") 
    pinL=int(input()) 
    print("Hola usuario. por favor ingrese la contraseña con letra minuscula: "  ) 
    pasL=input()


    if pinL==pin and pasL==pas:
        print("Bienvenido")
        sas=4
    else: print("Clave o pin incorrectos")

#ej 2
credito=0
ingreso=int(input("ingrese su sueldo "))
print("1.- basico")
print("2.- medio")
print("3.- superior")
edu=int(input("ingrese su nivel educaciónal "))

nacionalidad=input("ingrese su nacionalidad (chilena/otra): ")

if ingreso>=500000 and ingreso<=1000000:
    credito=credito+300000
elif ingreso>=1000000 and ingreso<=1500000:
    credito=credito+650000
elif credito>1500001:
    credito=credito+1000000
else:
    print("")
print(credito)
if edu==1:
    print("No tiene credito por educación")
elif edu==2:
    credito=credito*1.3
elif edu==3:
    credito=credito*1.5
else:
    print("")
print(credito)
if nacionalidad=="chilena":
    credito=credito+300000
else:
    print("no tiene bono por nacionalidad")
print(credito)
print("Su puntaje de credito es ", credito)