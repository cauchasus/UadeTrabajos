import random
cant_de_emp, sueldo15, sueldo1220, sueldomax = int(input("Ingrese la cantidad de empleados: ")), 0, 0, 0
for x in range(0, cant_de_emp):
    sueldo = random.randint(10000, 30000)
    if sueldo > 15000:
        sueldo15 = sueldo15 +1
        print(sueldo15)
    if 12000 < sueldo <= 20000:
        sueldo1220 = sueldo1220 +1
        print(sueldo1220)
    if sueldo > sueldomax:
        sueldomax = sueldo
        
print("La cantidad de sueldos mayores a 15000 es: ", sueldo15)
print("La cantidad de sueldos entre 12000 y 20000 es de : ", sueldo1220)
print("El sueldo máximo es de: ", sueldomax)
        
    
    