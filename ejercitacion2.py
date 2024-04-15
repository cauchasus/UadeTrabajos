q_de_animales, gatos, perros_h, conejos_m, nro = 0, 0, 0, 0, 0

pregunta1 = int(input("Ingrese el tipo de animal: "))
pregunta2 = int(input("Ingrese el sexo del animal: "))

while nro != -1:
    pregunta1 = int(input("Ingrese el tipo de animal: "))
     
    if pregunta1 == 1:
        perros_h, q_de_animales = perros_h + 1, q_de_animales + 1
        pregunta2 = int(input("Ingrese el sexo del animal: "))
        if pregunta2 == 2:
            perros_h = perros_h + 1
    elif pregunta1 == 2:
        gatos, q_de_animales = gatos + 1, q_de_animales +1
        pregunta2 = int(input("Ingrese el sexo del animal: "))
    elif pregunta1 == 3:
        conejos_m, q_de_animales = conejos_m +1, q_de_animales +1
        pregunta2 = int(input("Ingrese el sexo del animal: "))
        if pregunta2 == 1:
            conejos_m == conejos_m + 1
    elif pregunta1 == -1:
        nro = -1
        
print("La cantidad de animales tratados fue: ", q_de_animales)
print("La cantidad de perros hembra tratados fue:", perros_h)
print("La cantidad de conejos machos tratados fue: ", conejos_m)

pc_gatos = (gatos / q_de_animales) * 100
print("El porcentaje de gatos ingresados fue de: ", pc_gatos)