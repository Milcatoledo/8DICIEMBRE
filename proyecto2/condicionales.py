def run():
    cargos = ({"cargo": "Asistente", "sueldo": 900},
              {"cargo": "Analista", "sueldo": 1500},
              {"cargo": "Especialista", "sueldo": 2000})
    diasmes = 22
    horasdias = 8
    semanashoras = 40
    meshoras = 176
    nombre = input("Ingrese su nombre: ")
    horas = int(input("Ingrese horas: "))
    cargo = int(input("Ingrese un numero (1. Asistente, "
                      "2.Analista, 3. Especialista): "))
    sexo = input("Ingrese sexo (H. Hombre, M. Mujer): ")
    numerohijos = int(input("Ingrese numero de hijos: "))
    cargo = cargo - 1
    sueldo = cargos[cargo]['sueldo']
    valorhora = sueldo/meshoras
    total = round((valorhora * horas), 2)

    print(f"Estimado/a {nombre} usted ha elaborado un total de {horas} horas, su cargo es {cargos[cargo]['cargo']} "
          f"y su sueldo del mes {total} ")

    if (sexo == 'H'):
        bono = 20 * numerohijos
    else:
        bono = 30 * numerohijos
    total = total + bono
    print(f"Usted tiene un bono de {bono}, su sueldo actualizado del mes es {total}")


if __name__ == "__main__":
    run()
