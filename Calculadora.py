from Potencia import potencia
from division import dividir
from Multiplicacion import MultiplicarNumeros
from Resta import Resta
from Suma import Suma



#Menu
print " Seleccione una de las siuiente opciones"
print " 1.Sumar"
print " 2.Restar"
print " 3.Multiplicacion"
print " 4.Division"
print " 5.Potencia"
print "-----------------------------------------"
#entrada
seleccion= input("ingresa el numero de la opcion que quieres: ")
a=input("ingrese el primer numero: ")
b=input("ingrese el segundo numero: ")
#procesamiento
if seleccion == 1:
    resultado =Suma(a,b)
elif seleccion ==2:
    resultado =Resta(a,b)
    
elif seleccion ==3:
    resultado =MultiplicarNumeros(a,b)
elif seleccion ==4:
    resultado=dividir(a,b)
elif seleccion ==5:
    resultado=potencia(a,b)
#salida
print "resultado =", resultado
