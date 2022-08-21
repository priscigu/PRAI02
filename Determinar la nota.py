"""Determinar si un alumno aprueba o reprueba"""
nota1= int(input("Ingrese la primera nota"))
nota2= int(input("Ingrese la segunda nota"))
nota3= int(input("Ingrese la tercera nota"))
promedio= (nota1+nota2+nota3)/3
print("Su promedio es",round(promedio,2))
if promedio>50:
    print("APROBO LA MATERIA")
else:
    print("REPROBO LA MATERIA")
