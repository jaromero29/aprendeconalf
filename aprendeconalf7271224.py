# Escribr un programa que pida al usuario su peso en Kg y estatura en mts, calcule el indice de masa corporal y lo almacene en un variable
# y muestre por pantalla la frase "Tu indice de masa corporal es <imc>", donde <imc> es el indice de masa corporal calculado redondeado
# con dos decimales

p = float(input("Introduzca su peso en Kg:  "))
e = float(input("Introduzca su estura en Mts:  "))
mc = p * e
print("Tu indice de masa corporal es:", mc)

peso = input("¿Cuál es tu peso en kg? ")
estatura = input("¿Cuál es tu estatura en metros?")
imc = round(float(peso)/float(estatura)**2,2)
print("Tu índice de masa corporal es " + str(imc))     