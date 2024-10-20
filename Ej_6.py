#suma de negtivos // media de positivos
SumPos=0
CantPos=0
SumNeg=0
for x in range(6):
    Nro=int(input("Di un número: "))
    if Nro>0:
        SumPos=SumPos+Nro
        CantPos=CantPos+1
    else:
        SumNeg=SumNeg+Nro
print("La suma de los negativos es:", SumNeg)
if CantPos !=0:
    print("La media de positivos es:" ,SumPos/CantPos)