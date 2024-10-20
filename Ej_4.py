#Contador de vocales
frase=input("Di una frase: ")
vocales="aAeEiIoOuU"
cant=0
for x in frase:
    if x in vocales:
        cant=cant+1
print("Tiene", cant, "vocales.")