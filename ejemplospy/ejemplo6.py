contadores = dict()
print('Ingresa una línea de texto:')
lineaa = input('')

palabras = lineaa.split()

print('Palabras:', palabras)

print('Contando...')
for palabra in palabras:
    contadores[palabra] = contadores.get(palabra,0) + 1
print('Contadores', contadores)
