nombre = input('Ingresa un nombre de archivo:')
nombre ='./' + nombre
manejador = open(nombre)

print ("Este programa muestra el caracter que mas se repite en el archivo seleccionado")

contadores = dict()
for linea in manejador:
    palabras = linea.split()
    for palabra in palabras:
        contadores[palabra] = contadores.get(palabra,0) + 1
   


grancontador = None
granpalabra = None
for palabra,contador in contadores.items():
    if grancontador is None or contador > grancontador:
        granpalabra = palabra
        grancontador = contador
print(granpalabra)
print(grancontador)
