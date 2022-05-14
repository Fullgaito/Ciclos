nEstudiantes=int(input("Ingrese la cantidad de estudiantes: ")) #se pide el total de estudiantes
desaprobados=0 #Contador para las notas no aprobadas
aprobados=0 #contador para las notas aprobadas
for i in range(1,nEstudiantes+1,1): #como se conoce la cantidad de estudiantes se implementa un for para ejecutar una serie de pasos cuando se conoce el fin del ciclo
    nota=float(input(f"Ingrese la nota del estudiante {i}: ")) #se pide las notas
    while nota<0 or nota>5: #se valida que las notas sean correctas
        nota=int(input("Por favor ingrese una nota entre 0 y 5: ")) #se vuelve a pedir la nota en caso de que esta no sea correcta
    if nota>=0 and nota<=2.9: #se usa un condicional para indicar cuando una nota es desaprobada
        print("La nota es no aprobada")
        desaprobados+=1 #se incrementa el contador en 1 en caso de que esa nota no sea aprobada
    else:
        print("La nota es aprobada")
        aprobados+=1 #se incrementa el contador en 1 en caso de que la nota sea aprobada
print(f"La cantidad de estudiantes fueron:{nEstudiantes}") #se muestra la cantidad de estudiantes ingresados
print(f"La cantidad de estudiantes que aprobaron fueron:{aprobados}") #se muestra la cantidad de estudiantes que aprobaron
print(f"La cantidad de estudiantes que desaprobaron fueron:{desaprobados}") #se muestra la cantidad de estudiantes que no aprobaron
