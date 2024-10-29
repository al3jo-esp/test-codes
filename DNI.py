#Conseguir NIF a partir del DNI
num=int(input ("Introduce tu DNI: "))
letras='TRWAGMYFPDXBNJZSQVHLCKE'
print("La letra correspondiente a tu DNI es: ", letras[num%23])