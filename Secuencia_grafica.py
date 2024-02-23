# ACTIVIDAD 
# Integrantes: Paula Núñez e Isabella Arrieta
"Programar (preferiblemente en Python) el algoritmo obtenido del teorema de Havel-Hakimi."

import networkx as nx
import matplotlib.pyplot as plt


print("\nBienvenidx")
continuar= True
while continuar == True: 
    n= int(input("Ingrese la cantidad de nodos: "))
    secuencia=[]
    aux = []
    i=0
    while i<n:
        nodo = int(input(f"Ingrese el grado del nodo {i + 1}: "))
        secuencia.append(nodo)
        i+=1    
    secuencia.sort(reverse=True) 
    print("La secuencia ingresada es: ", secuencia)
    grafico = True # variable para saber si es un grafico
    aux = secuencia[:] # copia de la secuencia
    Todos_Cero= False # variable para saber si todos los elementos son cero
   
    while grafico==True and Todos_Cero== False and secuencia!=[]: # mientras sea un grafico y no todos los elementos sean cero
        secuencia.sort(reverse=True) # #organiza la secuencia de mayor a menor
        print(secuencia)
        primer_vertice = secuencia[0] # toma el primer vertice
        secuencia.pop(0) # elimina el primer vertice
        if primer_vertice > len(secuencia): #Verificar si el primer vertice es mayor que la longitud de la secuencia
            print("La secuencia ", aux, " no es un grafico, cantidad insuficiente para el vertice 1")
            grafico = False
            break
        for i in range(primer_vertice):
            secuencia[i]-=1 # resta 1 de acuerdo a la longiud del primer vertice
            if secuencia[i] <0: # verificar si el elemento es menor que 0
                print(secuencia)
                print("La secuencia ", aux, " no es un grafico")
                grafico = False
                break
        if grafico == False:
            break
        print(secuencia)
        elem=0
        for j in range(len(secuencia)):
            if secuencia[j] > 0: # verificar si el vertice es mayor que 0 para seguir con el ciclo
                Todos_Cero= False
            if secuencia[j] == 0:
                elem+=1 # contar los vertices que son cero
        if elem == len(secuencia) or secuencia == []: # verificar si todos los vertices son cero o la secuencia esta vacia
            Todos_Cero = True
        if Todos_Cero:
            grafico = True
            print("La secuencia ", aux, " es un grafico")
            G = nx.havel_hakimi_graph(aux)  # Generar el grafo simple G, dada una secuencia d, con el algoritmo H-H
            pos = nx.random_layout(G)  # Asignación del atributo 'posición' (pos) para posicionar los vértices en forma random
            nx.draw_networkx_nodes(G, pos, node_size=50)  # Dibujar solo los vértices del Grafo G con los atributos especificados
            nx.draw_networkx_edges(G, pos, width=0.5)  # Dibujar solo las aristas del Grafo G con los atributos especificados
            plt.axis("equal")  # Redimensionar los ejes a longitudes iguales
            plt.show()  # Mostrar el grado d-regular por pantalla
            
            secuencia = []
    print("Desea continuar? 1.Si 2.No")
    op=int(input("-> "))
    while op!= 1 and op!= 2:
        print("Ingrese una opción valida 1.Si 2.No")
        op=int(input("-> "))
    if op==2:
        print("¡Muchas gracias por implementar el programa!")
        continuar= False
    else:
        continuar= True
        print("*************************************************************\n")

    
