man_a = open('./ejemplo3.py')
for linea in man_a:
    linea = linea.rstrip() 
    linea = linea.lstrip()
    if linea.startswith('if') == False:
        continue
    print(linea)
