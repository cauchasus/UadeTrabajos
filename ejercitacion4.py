nro1, nro2, sum_div_1, sum_div_2 = int(input("Ingrese el primer numero: ")), int(input("Ingrese el segundo numero: ")), 0 , 0

for i in range(1, nro1):
    if nro1 % i == 0:
        sum_div_1 = sum_div_1 + i
        
for i in range(1, nro2):
    if nro2 % i == 0:
        sum_div_2 = sum_div_2 + i
        

if sum_div_1 == nro2 and sum_div_2 == nro1:
    print(nro1,"y",nro2,"son numeros amigos")
else:
    print("No son amigos")