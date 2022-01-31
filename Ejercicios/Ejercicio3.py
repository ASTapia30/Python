'''Escriba un programa que indica si una cadena de caracteres es palíndroma. Esto es, una
palabra o frase que se lee igual de izquierda a derecha que de derecha a izquierda. Algunos
ejemplos de frases palíndromas son las siguientes:
«Isaac no ronca así»
«Sometamos o matemos»'''

frase = "Isaac no ronca asi"
palabras = frase.split()
palabras = list(reversed(palabras))
nueva = " ".join(palabras)
nueva.replace(""," ")
print(nueva)

