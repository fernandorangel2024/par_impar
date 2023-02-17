# programa para determinar si un numero es par o impar
 
#input
X = int(input(" Ingrese un numero: "))

#processing
r = X%2

#output
if r & 1 ==0:
    print("El numero es par")
else:
    print("El numero es impar")
