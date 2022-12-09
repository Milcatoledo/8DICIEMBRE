import json

archivo = open('publicacion.json')
contenido = json.load(archivo)
profesores = []

def datos():
    for docente in contenido:
        cedula = docente['cedula']
        apellidos = docente['apellidos']
        datos = {
            'cedula': cedula,
            'apellidos': apellidos,
            'publicaciones': 0,
            'tipos': {'cientificas': 0, 'regionales':0},
            'areas': []
        }
        if datos not in profesores:
            profesores.append(datos)
    publicaciones()
    areas()
    tipop()
    presentar()
def publicaciones():
    for docente in profesores:
        cedula = docente['cedula']
        for docente in contenido:
            if profesores['cedula'] == cedula:
                docente['publicaciones'] += 1

def tipop():
    for docente in profesores:
        cedula = docente['cedula']
        tipos = docente['tipos']
        for docente in contenido:
            if docente['cedula'] == cedula:
                tipo = docente['tipobases']
                if tipo == 'cientificas':
                    tipos['cientificas'] += 1
                else:
                    tipos['regionales'] += 1

def areas():
    for docente in profesores:
        cedula = docente['cedula']
        areatra = docente['areas']
        for docente in contenido:
            if docente['cedula'] == cedula:
                area = docente['area']
                if not area in areatra:
                    areatra.append(area);

def presentar():
    for docente in profesores:
        print('     INFORMACION DE DOCENTES       ')
        print(f" Nombre: {docente['apellidos']}")
        print(f" Cedula: {docente['cedula']}")
        print(f" Publicaciones: {docente['publicaciones']}")
        tipos = docente['tipos']
        print(f"       TIPO DE ARTICULOS")
        print(f" Cientificos: {docente['cientificas']}")
        print(f" Regionales: {docente['regionales']}")
        areas = docente['areas'];
        print('        AREAS TRABAJADAS')
        for key in areas:
            print(key)


if __name__ == "__main__":
    datos();