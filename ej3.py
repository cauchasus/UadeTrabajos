def inputnum():
    boolean = True
    global par1
    par1 = input("Ingrese la nota del primer parcial: ")
    global par2
    par2 = input("Ingrese la nota del segundo parcial: ")
    global parciales
    parciales = [par1, par2]
    for var in parciales:
        try:
            float(var)
        except ValueError:
            boolean = False
        
    if boolean:
        promediof()
    else:
        print("Por favor ingrese un número")
        inputnum()



def promediof():
    promedio = (float(par1) + float(par2))/2
    print("Su nota promedio es: ", promedio)
    

inputnum()
