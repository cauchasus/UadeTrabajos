"""#Generar la serie de Fibonacci hasta el elemento 50
Informar cuales son los valores que tienen raíz cuadrada exacta entre las posiciones 10 a 40
Pensar como saber si un nro puede tener raíz exacta. Debatirlo con el profesor"""

val_a, val_b, cont = 0, 1, 0
while cont <= 50:
    print(val_a, end=", ")
    val_b, val_a = val_a + val_b, val_b
    cont = cont + 1
    if (val_a ** 0.5) % 1 == 0 and cont >= 10 and cont <= 40:
        print("Este número tiene raiz exacta: ", val_a, "en la posición: ", cont)
