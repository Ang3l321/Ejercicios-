#Solicita al usuario tres notas, calcula el promedio y muestra si aprueba o no.
# La nota mínima para aprobar es 3.0.

# Entrada: Nota1: 4.0, Nota2: 3.5, Nota3: 2.0
# Salida: Tu promedio es 3.2. ¡Has aprobado!

Nota1 = float(input("Ingrese porfavor ingrese la Nota 1: "))
Nota2 = float(input("Ingrese porfavor ingrese la Nota 2: "))
Nota3 = float(input("Ingrese porfavor ingrese la Nota 3: "))

Promedio = (Nota1 + Nota2 + Nota3 )// 3

if Promedio >= 3.2:
    print(f'Felicidades tu promedio es mayor a {Promedio} ¡Has aprobado! (～￣▽￣)～ ')
    
else:
    print(f'Lo siento tu promedio es  {Promedio} ¡Has Reprovado estudie vago! (►__◄) ')