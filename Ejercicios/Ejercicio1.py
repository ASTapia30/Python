'''Escriba programa que encuentre el máximo común divisor de dos números. Esto es: el mayor
número que divide exactamente a dos o más números. Por ejemplo, el máximo común
divisor de 15 y 20 es 5.'''

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro numero: "))

MCD1=[]
MCD2=[]
MCD_COMUNES = []

#Calculamos los múltiplos de cada numero
for i in range (1, num1):
    if (num1 % i == 0):
        MCD1.append(i)
    
    if (num2 % i == 0):
        MCD2.append(i)

print(MCD1)
print(MCD2)

#Verificamos primero que lista es mayor. Luego comparamos los elementos que sean similares en ambas listas y creamos una nueva con esos elementos
if (len(MCD1) > len(MCD2)):
    for element in MCD2:
        if (element in MCD1):
            MCD_COMUNES.append(element)
else:
    for element in MCD1:
        if (element in MCD2):
            MCD_COMUNES.append(element)

print(MCD_COMUNES)

#Mostramos en pantalla el elemento mayor de la lista de múltiplos que comparten ambas listas iniciales
print(f"El Máximo Común Divisor de {num1} y {num2} es: {max(MCD_COMUNES)}")