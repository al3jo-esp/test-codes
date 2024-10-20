#Ticket de la compra con condiciones

total=0
art=float(input("Precio del artículo: €"))
while art!=0:
    if art<0:
        print("Artículo no válido")
    else:
        total=total+art
    art=float(input("Precio del artículo: €"))
if total>1000:
    total=total-(total/10)
print("Precio total: €", total)
