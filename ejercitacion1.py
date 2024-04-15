
val_a, val_b, cont = 0, 1, 0
while cont <= 40:
    print(val_a, end=", ")
    val_a, val_b = val_b, val_a + val_b
    cont = cont + 1

val_a, val_b, cont = 0, 1, 0
for nro in range(40):
    if nro >= 12 and nro < 30:
        if val_a % 3 == 0:
            cont = cont + 1
            print("Posición", nro, ":", val_a)
    val_a, val_b = val_b, val_a + val_b
    
print("Total de múltiplos de 3 entre las posiciones 12 y 30:", cont)