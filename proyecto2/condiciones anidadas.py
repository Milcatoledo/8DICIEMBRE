# Listado de becarios
#Toledo Milca
estudiantes = [
    {'nombre': 'Milca', 'carrera': 'Soft', 'sexo': 'M', 'estado': 'Medio bajo', 'promedio': 90, 'asistencia': 100,
     'beca': False, 'deuda': 0, 'tipo': ''},
    {'nombre': 'Aaron', 'carrera': 'Soft', 'sexo': 'H', 'estado': 'Medio alto', 'promedio': 92, 'asistencia': 95,
     'beca': False, 'deuda': 0, 'tipo': ''},
    {'nombre': 'Frank', 'carrera': 'Soft', 'sexo': 'H', 'estado': 'Medio bajo', 'promedio': 98, 'asistencia': 90,
     'beca': False, 'deuda': 0, 'tipo': ''},
    {'nombre': 'Elisa', 'carrera': 'Bio', 'sexo': 'M', 'estado': 'Bajo', 'promedio': 86, 'asistencia': 98,
     'beca': False, 'deuda': 0, 'tipo': ''},
    {'nombre': 'Mario', 'carrera': 'Bio', 'sexo': 'H', 'estado': 'Alto', 'promedio': 97, 'asistencia': 99,
     'beca': False, 'deuda': 0, 'tipo': ''},
    {'nombre': 'Adriana', 'carrera': 'Bio', 'sexo': 'M', 'estado': 'Bajo', 'promedio': 95, 'asistencia': 93,
     'beca': False, 'deuda': 0, 'tipo': ''},
    {'nombre': 'Erika', 'carrera': 'Ali', 'sexo': 'M', 'estado': 'Bajo', 'promedio': 99, 'asistencia': 92,
     'beca': False, 'deuda': 0, 'tipo': ''},
    {'nombre': 'Ivan', 'carrera': 'Ali', 'sexo': 'H', 'estado': 'Medio bajo', 'promedio': 92, 'asistencia': 90,
     'beca': False, 'deuda': 0, 'tipo': ''},
    {'nombre': 'Hit', 'carrera': 'Ind', 'sexo': 'H', 'estado': 'Medio alto', 'promedio': 93, 'asistencia': 85,
     'beca': False, 'deuda': 0, 'tipo': ''},
    {'nombre': 'Omar', 'carrera': 'Ind', 'sexo': 'H', 'estado': 'Alto', 'promedio': 95, 'asistencia': 89, 'beca': False,
     'deuda': 0, 'tipo': ''},
]


def beca_academica():
    print('...... Becados por nivel: Academicos ......')
    for i in estudiantes:
        cumplep = False
        cumplea = False
        cumpled = False
        if 95 <= i['promedio'] <= 100:
            cumplep = True

        if 90 <= i['asistencia'] <= 100:
            cumplea = True

        if i['deuda'] == 0:
            cumpled = True

        if cumplep and cumplea and cumpled:
            i['beca'] = True
            i['tipo'] = 'A'

    for i in estudiantes:
        if i['beca'] == True:
            print(f"Beca académica a {i['nombre']} {i['beca']} {i['tipo']} ")


def beca_socioeconomia():
    print('...... Becados por nivel: Socio-economicos ......')
    for i in estudiantes:
        if i['tipo'] == '':
            becado = True
        else:
            becado = False
        if i['estado'] == 'Bajo' or i['estado'] == 'Medio bajo':
            cumplee = True
        else:
            cumplee = False
        if 80 <= i['promedio'] <= 100:
            cumplep = True
        else:
            cumplep = False
        if 90 <= i['asistencia'] <= 100:
            cumplea = True
        else:
            cumplea = False
        if i['deuda'] == 0:
            cumpled = True
        else:
            cumpled = False
        if (cumplee and cumplep and cumplea and cumpled and becado):
            i['beca'] = True
            i['tipo'] = 'S'
            print(f"Beca socioeconomica a {i['nombre']} {i['beca']} {i['tipo']} ")


def run():
    beca_academica()
    beca_socioeconomia()


if __name__ == "__main__":
    run()