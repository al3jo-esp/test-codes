aprobados=0
cantidad=0
sumaAprobados=0
a=input("¿Analizar las notas? 'S' para 'sí':")
while a == "S":
    notas=int(input("Notas del alumno:"))
    if notas> 5:
        aprobados=aprobados+1
        sumaAprobados=sumaAprobados+notas
    cantidad=cantidad+1
    a=input("¿Continuar? 'S' para 'sí':")
print("Porcentaje de alumnos aprobados:", (aprobados*100)/cantidad, "%")
print("media de aprobados:", sumaAprobados/aprobados)
