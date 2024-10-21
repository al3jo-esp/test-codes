#Usuario y contraseña
Username=input("Nombre de usuario: ")
Password=input("Contraseña: ")
if Username=="Gwen" and Password=="excalibur":
 print("Usuario y contraseña correctos, puedes ingresar.")
else:
 print("Usuario/contraseña incorrecto. Vuelve a intentarlo!")

Username=input("Nombre de usuario: ")
Password=input("Contraseña: ")
while Username!="Gwen" or Password!="excalibur":
  print("Usuario/contraseña incorrecto. Vuelve a intentarlo!")
  Username=input("Nombre de usuario: ")
  Password=input("Contraseña: ")
else:
   print("Usuario y contraseña correctos, puedes ingresar.")
