# ACTIVIDAD 
# Integrantes: Paula Núñez e Isabella Arrieta
"Programar (preferiblemente en Python) el algoritmo obtenido del teorema de Havel-Hakimi."

print("\nBienvenidx")
continuar= True
while continuar == True:
    n= int(input("Ingrese la cantidad de nodos: "))
    secuencia=[]
    i=0
    while i<n:
        nodo = int(input(f"Ingrese el nodo {i + 1}: "))
        secuencia.append(nodo)
        i+=1    
    print("La secuencia ingresada es: ", secuencia)
    print("Desea continuar? 1.Si 2.No")
    op=int(input("-> "))
    while op!= 1 and op!= 2:
        print("Ingrsese una opción valida 1.Si 2.No")
        op=int(input("-> "))
    if op==2:
        print("¡Muchas gracias por implementar el programa!")
        continuar= False
    else:
        continuar= True
        print("*************************************************************\n")
        
