def inage():
    boolean = True
    global edad
    edad = input("Ingrese su edad en años: ")
    for var in edad:
        try:
            int(var)
        except ValueError:
            boolean = False
    
    if boolean == False:
        print("Ingresaste mal tu edad")
        inage()
    else:
        disday()

def disday():
    conversion = int(edad) * 365
    print("Tienes: ", conversion, "dias")
    

inage()
