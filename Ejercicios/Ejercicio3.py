'''Escriba un programa que indica si una cadena de caracteres es palíndroma. Esto es, una
palabra o frase que se lee igual de izquierda a derecha que de derecha a izquierda. Algunos
ejemplos de frases palíndromas son las siguientes:
«Isaac no ronca así»
«Sometamos o matemos»'''

frase = "Sometamos o matemos"
frase_min = frase.lower()
frase_pegada = frase_min.replace(" ", "")
longitud_frase = frase_pegada.__len__()
nueva_frase =[]
for i in range(1,frase_pegada.__len__()+1):
    nueva_frase.append(frase_pegada[frase_pegada.__len__() - i])

# print(nueva_frase)
frase_comparar = "".join(nueva_frase)
# print(frase_min)
# print(frase_comparar)

if frase_pegada == frase_comparar:
    print(f"La frase: {frase}... SÍ es palíndroma")
else: print(f"La frase: {frase}... NO es palíndroma")