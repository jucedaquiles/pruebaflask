contadores = dict()
nombres = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for nombre in nombres :
    contadores[nombre] = contadores.get(nombre, 0) + 1
print(contadores)
