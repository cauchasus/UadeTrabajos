dinero = int(input("Cantidad de dinero: "))

sobrante1000 = dinero // 1000
dinero = dinero % 1000
print("Billetes de 1000", sobrante1000)

sobrante500 = dinero // 500
dinero = dinero % 500
print("Billetes de 500", sobrante500)

sobrante100 = dinero // 100
dinero = dinero % 100
print("Billetes de 100", sobrante100)

sobrante50 = dinero // 50
dinero = dinero % 50
print("Billetes de 50", sobrante50)

sobrante10 = dinero // 10
dinero = dinero % 10
print("Billetes de 10", sobrante10)

sobrante5 = dinero // 5
dinero = dinero % 5
print("Billetes de 5", sobrante5)

sobrante1 = dinero // 1
dinero = dinero % 1
print("Billetes de 1", sobrante1)
