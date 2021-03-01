print ("Ejecutando programa *Calculadora*...")
def calculadora():
    def menu():
        print (" ")
        print ("************** Calculadora *************")
        print (" ")
        print (">>>> By: Raydell Rios <<<<")
        print (" ")
        print ("SELECCIONE UNA OPCIÓN:")
        print ("1)Suma")
        print ("2)Resta")
        print ("3)Multiplicación")
        print ("4)División")
        print ("5)Salir")
        try:
            opc=int(input(">"))   
        except ValueError:
            print ("Porfavor ingrese una cantidad numérica de las opciones.")
            return menu()
        
        if opc==5:
            print ("Programa finalizado")

        elif opc==0:
            print (" ")
            print (" ")
            print ("NO ME TOMES DEL PELO/ ¿EN QUE MOMENTO HABIA UNA OPCIÓN 0?")
            print (" ")
            print (" ")
            return menu()

        elif opc==1:
            print ("Has elegido sumar")
            def suma():
                try:
                    A= float(input("Ingrese un numero >"))
                except ValueError:
                    print ("ERROR: **Porfavor use solo numeros**")
                    return suma()
                try:
                    B= float(input("Ingrese otro numero >"))
                except ValueError:
                    print ("ERROR: **Porfavor use solo numeros**")
                    return suma()
                R= A+B
                print ("R//: " + str(R))
                return menu()

            suma()

        elif opc==2:
            print ("Has elegido restar")
            def resta():
                try:
                    A= float(input("Ingrese un numero >"))
                except ValueError:
                    print ("ERROR: **Porfavor use solo numeros**")
                    return resta()
                try:
                    B= float(input("Ingrese otro numero >"))
                except ValueError:
                    print ("ERROR: **Porfavor use solo numeros**")
                    return resta()
                R= A-B
                print ("R//: " + str(R))
                return menu()
                
            resta()
            
        elif opc==3:
            print("Has elegido multiplicar")
            def multiplicar():
                try:
                    A= float(input("Ingrese un numero >"))
                except ValueError:
                    print ("ERROR: **Porfavor use solo numeros**")
                    return multiplicar()
                try:
                    B= float(input("Ingrese otro numero >"))
                except ValueError:
                    print ("ERROR: **Porfavor use solo numeros**")
                    return multiplicar()
                R= A*B
                print ("R//: " + str(R))
                return menu()
                
            multiplicar()

        elif opc==4:
            print ("Has elegido dividir")
            def dividir():
                try:
                    A= float(input("Ingrese el dividendo >"))
                except ValueError:
                    print ("ERROR: **Porfavor use solo numeros**")
                    return dividir()
                try:
                    B= float(input("Ingrese el divisor >"))
                except ValueError:
                    print ("ERROR: **Porfavor use solo numeros**")
                    return dividir()
                R= A/B
                print ("R//: " + str(R))
                return menu()
        else:
            print("La opción ingresada no es válida.")
            return menu()
                
            dividir()
    menu()
calculadora()
