sueldo_bas = float(input("Ingrese su sueldo base en pesos: "))
antig = float(input("Ingrese sus años de antiguedad: "))
es_civ = float(input("Ingrese su estado civil, (1 si es soltero 2 si es casado:) "))

if es_civ == 1:
    sueldo_bas = (sueldo_bas * 1.05)
    sueldo_fin = sueldo_bas - (sueldo_bas * 0.11) - (sueldo_bas * 0.03) - (sueldo_bas * 0.03)
    print("Su sueldo neto es de: ", sueldo_fin)
    
elif es_civ == 2:
    sueldo_bas = (antig * 0.07) + sueldo_bas
    sueldo_fin = sueldo_bas - (sueldo_bas * 0.11) - (sueldo_bas * 0.03) - (sueldo_bas * 0.03)
    print("Su sueldo neto es de: ", sueldo_fin)
