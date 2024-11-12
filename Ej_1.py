#Usuario y contraseña
Username=input("Nombre de usuario: ")
Password=input("Contraseña: ")
if Username=="Gwen" and Password=="Excalibur":
 print("Usuario y contraseña correctos, puedes ingresar.")
else:
 print("Usuario/contraseña incorrecto. Vuelve a intentarlo!")
 while Username!="Gwen" and Password !="Excalibur":
  Username=input("Nombre de usuario: ")
Password=input("Contraseña: ")
if Username=="Gwen" and Password=="Excalibur":
 print("Usuario y contraseña correctos, puedes ingresar.")
else:
 print("Usuario/contraseña incorrecto. Vuelve a intentarlo!")
