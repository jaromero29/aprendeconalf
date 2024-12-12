# Escribir un programa que pregunte al usuariopor el numero de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

HorasT = float(input("Por favor digame el numero de horas trabajadas:  "))
CostHor = float(input("Por favor digame el costo por hora: "))

Total = HorasT * CostHor
print("Le corresponde de paga", Total) 
  
