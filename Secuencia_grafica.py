# ACTIVIDAD 
# Integrantes: Paula Núñez e Isabella Arrieta
"Programar (preferiblemente en Python) el algoritmo obtenido del teorema de Havel-Hakimi."

print("\nBienvenidx")
continuar= True
while continuar == True:
    n= int(input("Ingrese la cantidad de nodos: "))
    secuencia=[]
    aux = []
    i=0
    while i<n:
        nodo = int(input(f"Ingrese el nodo {i + 1}: "))
        secuencia.append(nodo)
        i+=1    
    secuencia.sort(reverse=True)
    print("La secuencia ingresada es: ", secuencia)
    grafico = True
    Negativo = False
    aux = secuencia[:]
    Todos_Cero= False
   
    while grafico==True and Todos_Cero== False and secuencia!=[]:
        secuencia.sort(reverse=True) # organiza
        print(secuencia)
        primer_elemento = secuencia[0] # toma el primer elemento
        secuencia.pop(0)
        if primer_elemento > len(secuencia):
            print("La secuencia ", aux, " no es un grafico")
            grafico = False
            break
        for i in range(primer_elemento):
            secuencia[i]-=1
            if secuencia[i] <0:
                print(secuencia)
                print("La secuencia ", aux, " no es un grafico")
                grafico = False
                break
        if grafico == False:
            break
        print(secuencia)
        elementos=0
        for j in range(len(secuencia)):
            if secuencia[j] > 0:
                Todos_Cero= False
            if secuencia[j] == 0:
                elementos+=1
        if elementos == len(secuencia) or secuencia == []:
            Todos_Cero = True
        if Todos_Cero:
            grafico = True
            print("La secuencia ", aux, " es un grafico")
            secuencia = []

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
        
