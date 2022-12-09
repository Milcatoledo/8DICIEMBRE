import json

archivo1 = open('archivo1.txt', 'r')
contenido = archivo1.read()
print(f'{contenido}')
archivo1.close()

archivo2 = open('archivo2.json', 'r')
contenido2 = json.load(archivo2)
print(contenido2)
for i in contenido2:
    print(i)
