#Identificador de años bisiestos
year=int(input("¿Es un año bisiesto?"))
if year==0:
    if year%100 !=0 or year%400==0:
     print ("Es un año bisiesto")
    else: print("Año no bisiesto")
else:
   print("No es un año bisiesto")

    year=int(input("¿Es un año bisiesto?"))
if year%4==0:
    if year%100==0:
      if year%400==0:
        print ("Es un año bisiesto")
      else:
        print("No es un año bisiesto")
    else:
      print("Es un año bisiesto")
else:
   print("No es un año bisiesto")
