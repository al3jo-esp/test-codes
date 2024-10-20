#Cambio de número entero a factorial
NumEnt=int(input("Di un número entero: "))
fact=1
if NumEnt !=0:
    for x in range(1, NumEnt+1):
     fact=fact*x
print("Su factorial es: ", fact)
