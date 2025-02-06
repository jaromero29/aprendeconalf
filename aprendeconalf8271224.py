#Escribir un programa que pida al usuario dos numeros enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r>
# donde <n> y <m> son los numeros introducidos por el usuario y <c> son el cociente y el resto de la división entera  respectivamente.

n = input("Introduzca su primer numero:  ")
m = input("Introduzca su segundo numero: ")
#c = str(n/m)

n = input("Introduce el dividendo (entero): ")
m = input("Introduce el divisor (entero): ")
print(n , " entre " ,  m , " da un cociente " , str(int(n) // int(m)) , " y un resto " , str(int(n) % int(m)))
