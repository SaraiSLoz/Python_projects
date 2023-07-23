#Developed by: Sarai Santiago Lozano and Humberto Pérez Galindo
from numpy import *
from sys import*
import random
import os
import time
numero = False
#Distribution of the work:
#Page 1: Saraí
#Page 4: Saraí/Humberto
#Page  4.x: Los dos
#Page 5: Respuestas (Humberto)
#Page 5: Both (they are different exams)
print ('Bienvenid@ a tu apoyo para la prueba PISA en la sección de matemáticas');
print ('Para empezar ingrese sus datos personales');                             
arch = open('datospersonales.txt','w'); ### Create the file .txt for each student
nom = input('Nombre completo: '); # Insert the name of the user
while numero == False: # Start a while loop to check that the user enters an integer number for the variable [ed].
    ed = input('Edad: ');
    try:                 # Use loops and exceptions to verify that [ed] is an integer number
        os.system("cls") #
        edad = int(ed)   #
        numero = True    #
    except ValueError:#
        print("Error, tu edad no es valida")      # 
        print("Asegurate de introducir un número")# 
        numero = False# 
esc = input('Escuela: ');            # Insert the user's school
corr = input('Correo electrónico: ');# Insert the user´s school
linea = "Nombre: " + nom + '\n'+ "Edad: " + ed + '\n' + "Escuela: " + esc + '\n' + "Correo Electronico Registrado: " + corr + '\n' 
arch.write(linea); 
arch.close();      #close "datospersonales.txt
for i in range (6):                                                                        
    if i == 1:                                                                                
        os.system("cls")                                                                    
        print("Gracias ", nom, " estamos por comenzar con tus pruebas de aprendizaje PISA")
        print("\n" + "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO".center(50, " "))
        time.sleep(1)
    elif i == 2:
        os.system("cls")
        print("Gracias ", nom, " estamos por comenzar con tus pruebas de aprendizaje PISA")
        print("\n" + "------OOOOOOOOOOOOOOOOOOOOOOOOOOOOO".center(50, " "))
        time.sleep(1)
    elif i == 3:
        os.system("cls")
        print("Gracias ", nom, " estamos por comenzar con tus pruebas de aprendizaje PISA")
        print("\n" + "------------OOOOOOOOOOOOOOOOOOOOOOO".center(50, " "))
        time.sleep(1)
    elif i == 4:
        os.system("cls")
        print("Gracias ", nom, " estamos por comenzar con tus pruebas de aprendizaje PISA")
        print("\n" + "--------------------OOOOOOOOOOOOOOO".center(50, " "))
        time.sleep(1)
    elif i == 5:
        os.system("cls")
        print("Gracias ", nom, " estamos por comenzar con tus pruebas de aprendizaje PISA")
        print("\n" + "-----------------------------------".center(50, " "))
        time.sleep(1)
        
punt = 0    
punt_r = 10 
def puntaje(i,punt,punt_r):  #Function start (score) to obtain the learning exam grade
    if i == 1 :              # 
        punt = punt + 10;    # If the user gets it right on the first attempt, they will receive the full value of the points
        return punt;         # 
    elif i == 5:             # If the user uses all of their attempts
        punt = punt + 0      #  then they will lose the 10 points for the question
        return punt          #
    elif i > 1:              #
        punt = punt + punt_r;#
        return punt;         #
os.system("cls")
print ('Ejercicio 1.'); #Star the exercises
print('Si se aplica la fórmula a la manera de caminar de Enrique y éste da 70 pasos por minuto');#  Instructions
print('¿Cuál es la longitud paso de Enrique?');                                                  #  First Exercise
Resp = float(input('Ingresa la respuesta: ')); # user's answer
Respcorrect = 70 / 140;
i = 1;
while Resp != Respcorrect and i <= 4: # Start while loop in case the user insert a wrong answer
    os.system("cls")
    print('No es correcto...');#
    print('¿Necesitas ayuda?');# 
    print ('1. Sí');           # 
    print ('2. No');           #
    n = int(input('Ingrese el número de su elección: '));# A menu for hints
    if n == 1:                                                                                      #
        os.system("cls")                                                                            #
        print('Un tip para solucionar problemas es idetificar los conceptos claves de la preguna'); #
        print('Identifca que datos te están dando.... ¿te dan n? ¿o te dan P ?');                   #
        print ('Intento: ', i + 1);#print the attempt for the user
        print('-----------------------------------------------');
        print('¿Cuál es la longitud paso de Enrique?');
        Resp = float(input('Ingresa la respuesta: '));
        print('-----------------------------------------------');
        i = i +1;
        punt_r = punt_r - 2;
    if n == 2:
        os.system("cls")
        print ('Intento: ', i);
        print('-----------------------------------------------');
        print('¿Cuál es la longitud paso de Enrique?');
        Resp = float(input('Ingresa la respuesta: '));
        print('-----------------------------------------------');
        i = i + 1;
        punt_r = punt_r - 2;
if Resp == Respcorrect:
    os.system("cls")
    print("\n" + 'Correcto!');
    print('Si se ocupa la formula n/P = 140, conocemos n, por lo cual se despeja P y el resultado es: 0,5 m.');
    print("\n" + "Presiona ENTER para continuar")
    input()
cal_1=puntaje(i,punt,punt_r);
punt_r = 10
os.system("cls")
print ('Ejercicio 2.'); #Exercise 2
print('Completa esta tabla escribiendo la cantidad de penicilina que permanecerá activa en la sangre de la mujer'+'\n'+' a intervalos de una hora desde las 8:00 hasta las 11:00 hrs.');#Instrucciones
linea = ['Horas          ','8:00','9:00','10:00','11:00']; 
print ("|".join(linea)); 
linea2 = ['Penincilina(mg)','300']
print("|".join(linea2)); 
matriz = []; #
datos = [];  # 
datos_r = [];#
for i in range (2): #Create an array with the data
    if i == 0:
        datos= linea;
        matriz.append (datos);
    if i == 1:
        datos_i = linea2;
        for j in range (1,4):
            res = float(input ('Ingrese el resultado (números enteros)'+str(j)+': '));
            datos_r = datos_r + [res];
        matriz. append(datos_i +datos_r);
matriz2 = array(matriz);
print (matriz2);
i = 1;
while (matriz [1][2] != 180.0 or matriz [1][3] != 108.0 or matriz [1][4] != 65.0) and i <= 4:
    matriz.clear();
    os.system("cls")
    print('No es correcto...'); #
    print('¿Necesitas ayuda?'); # 
    print ('1. Sí');            #
    print ('2. No');            #
    n = int(input('Ingrese el número de su elección: ')); #
    if n == 1:
        os.system("cls")
        print('Un tip para solucionar problemas es idetificar los datos claves, el primer dato es la cantidad inicial 300 gr ');          #
        print('El segundo dato es que después de 1 hora la siguiente cantidad es el 60 % de la anterior');                                # A hint for the user
        print('Por lo cual, como te piden la cantidad cada hora, debes calcula el 60% de la cantidad actual para encontrar la siguiente');#
        print("\n" + "|".join(linea) + "\n" + "|".join(linea2)) # Print the table again
        print ('Intento: ', i + 1); #Print the aatempt
        print('-----------------------------------------------');
        for j in range (2): #Creat the matrix 
            if j == 0:
                datos= linea;
                matriz.append (datos);
            elif j == 1:
                datos_i = linea2;
                datos_r = [];
                for k in range (1,4):
                    res = float(input ('Ingrese el resultado (números enteros)'+str(k)+': '));
                    datos_r = datos_r + [res];
                matriz. append(datos_i + datos_r);
        matriz2 = array(matriz); 
        print (matriz2);
        print('-----------------------------------------------');
        i = i+1;
        punt_r = punt_r - 2;
    if n == 2:
        os.system("cls")
        print ('Intento: ', i + 1);
        print("\n" + "|".join(linea) + "\n" + "|".join(linea2))
        print('-----------------------------------------------');
        for j in range (2):
            if j == 0:
                datos= linea;
                matriz.append (datos);
            if j == 1:
                datos_i = linea2;
                datos_r = [];
                for k in range (1,4):
                    res = float(input ('Ingrese el resultado (números enteros)'+str(k)+': '));
                    datos_r = datos_r + [res];
                matriz. append(datos_i +datos_r);
        matriz2 = array(matriz);
        print (matriz2);
        print('-----------------------------------------------');
        i = i +1;
        punt_r = punt_r - 2;
if matriz [1][2] == 180.0 and matriz [1][3] == 108.0 and matriz [1][4] == 65.0:
    os.system("cls")
    print('Correcto!');
    print('Se debe calcular el 60% de la cantidad actual para obtener la siguiente cantidad. Por lo cual, para obtener la primera cantida es 300 * .60');
    print("\n" + "Presiona ENTER para continuar")
    input()
cal_2 = puntaje(i,cal_1,punt_r);

punt_r = 10
os.system("cls")
print ('Ejercicio 3.');
print ('¿A partir de qué edad la frecuencia cardíaca recomendada aumenta como resultado de la introducción de la fórmula nueva');
Resp = int(input('Ingresa la respuesta: '));
i = 1;
while Resp != 41 and Resp != 40 and i <= 4: 
    print('No es correcto...');
    print('¿Necesitas ayuda?');
    print ('1. Sí');
    print ('2. No');
    n = int(input('Ingrese el número de su elección: '));
    if n == 1:
        print('\n');
        print('Un tip para resolverlo es entender el problema tine la incógnita de edad');
        print('Y como las dos fórmulas son para la frecuencia cardíaca máxima, se pueden igualar');
        print('Por último solo debes obtener la edad');
        print ('Intento: ', i);#Print the attempt
        print('-----------------------------------------------');
        print ('¿A partir de qué edad la frecuencia cardíaca recomendada aumenta como resultado de la introducción de la fórmula nueva');
        Resp = float(input('Ingresa la respuesta: '));
        print('-----------------------------------------------');
        i = i +1;
        punt_r = punt_r - 2;
    if n == 2:
        print ('Intento: ', i);
        print('-----------------------------------------------');
        print ('¿A partir de qué edad la frecuencia cardíaca recomendada aumenta como resultado de la introducción de la fórmula nueva');
        Resp = float(input('Ingresa la respuesta: '));
        print('-----------------------------------------------');
        i = i + 1;
        punt_r = punt_r - 2;
if Resp == 40 or Resp == 41:
    print('Correcto!');
    print('Sí se igualan las ecuaciones 208 - (0.7x edad) = 220 - edad, obtienes que edad= 40');
cal_3 = puntaje(i,cal_2,punt_r);


#ejercicio 4
punt_r = 10
print ('Ejercicio 4.');
print ('¿Cuánto dinero recibió Mei-Ling en rands africanos?');
print('1 SGD = 4,2 ZAR');
Resp_co = 4.2 * 3000;
Resp = int(input('Ingresa la respuesta: '));
i = 1;
while Resp != Resp_co and i <= 4:
    print('No es correcto...');
    print('¿Necesitas ayuda?');
    print ('1. Sí');
    print ('2. No');
    n = int(input('Ingrese el número de su elección: '));
    if n == 1:
        print('\n');
        print('Para resolver el problema necesitas entender la relación entre los datos');
        print('Puedes plantear una regla de tres; sí 1 SGD vale 4,2 ZAR, ¿Cuánto valdrá 3000 SGD');
        print ('Intento: ', i);
        print('-----------------------------------------------');
        print ('¿Cuánto dinero recibió Mei-Ling en rands africanos?');
        Resp = float(input('Ingresa la respuesta: '));
        print('-----------------------------------------------');
        i = i +1;
        punt_r = punt_r - 2;
    if n == 2:
        print ('Intento: ', i);
        print('-----------------------------------------------');
        print ('¿Cuánto dinero recibió Mei-Ling en rands africanos?');
        Resp = float(input('Ingresa la respuesta: '));
        print('-----------------------------------------------');
        i = i + 1;
        punt_r = punt_r - 2;
if Resp == Resp_co:
    os.system("cls")
    print('Correcto!');
    print('Si se ocupa la formula del promedio, conocemos que 240 es la suma de los primeros exámenes, así solo se se suma el 80 y se divide entre 5');
    print("\n" + "Presiona ENTER para continuar")
    input()
cal_4 = puntaje(i,cal_3,punt_r);

#Ejercicio 5
punt_r = 10
def ejer_5 ():
    lista = [];
    print('¿Cuál de las siguientes conclusiones se puede sacar certeramente de esta información?');
    print('-----------------------------------------------');
    print ('Los dos estudiantes eran niñas : ');
    a = pregunta();
    lista = lista + [a];
    print('-----------------------------------------------');
    print ('Uno de los estudiantes era un niño y el otro era una niña ');
    b = pregunta ();
    lista = lista + [b];
    print('-----------------------------------------------');
    print ('Los dos estudiantes tenían la misma estatura');
    c = pregunta ();
    lista = lista + [c];
    print('-----------------------------------------------');
    print('La estatura promedio de todos los estudiantes no varió');
    d = pregunta ();
    lista = lista + [d];
    print('-----------------------------------------------');
    print ('Carlos sigue siendo el más bajo');
    e = pregunta ();
    lista = lista + [e];
    print('-----------------------------------------------');
    return lista
def pregunta ():
    print ('Opciones');
    print ('1. Sí');
    print ('2. No');
    r = int(input('Ingrese el número de su respuesta: '));
    print(r);
    return r

#Ejercicio 5
print('-----------------------------------------------');
print('Ejercicio 5');
lista = ejer_5();
lista_cor = [2,2,2,2,1];
i = 1
punt_r = 10;
while lista != lista_cor and i <= 4:
    print('No es correcto...');
    print('¿Necesitas ayuda?');
    print ('1. Sí');
    print ('2. No');
    n = int(input('Ingrese el número de su elección: '));
    if n == 1:
        print ('Consejos con base a sus erroes: ');
        if lista [0] == 1:
            print('Debes tomar en cuenta que el promedio de las chicas no varió');
            print('-----------------------------------------------');
        if lista [1] == 1:
            print ('Que sea uno niño y el otro niña no implica que no haya variado el promedio');
            print('-----------------------------------------------');
        if lista [2] == 1:
            print ('Al no saber si son niños o niñas, no podemos afirmar que tengan la misma estatura');
            print('-----------------------------------------------');
        if lista [3] == 1:
            print ('Sabemos que la estatura promedio no varió, por lo cual no puede ser una conclusión');
            print('-----------------------------------------------');
        if lista [4] == 2:
            print ('Para que el promedio no varie, el rango de estaturas no debe variar mucho, por lo cual la estatura de Carlos debe ser la menor');
            print('-----------------------------------------------');
        print('-----------------------------------------------');
        print ('Intento: ', i);#Print the user attempt
        lista = ejer_5();
        print('-----------------------------------------------');
        i = i + 1;
        punt_r = punt_r - 2;
    elif n == 2:
        print ('Intento: ', i);
        print('-----------------------------------------------');
        lista = ejer_5();
        print('-----------------------------------------------');
        i = i + 1;
        punt_r = punt_r - 2;
if lista == lista_cor:
    print('Correcto!');
    print('Como la estatura más baja sigue siendo la de Carlos, el promedio no variará ');
cal_5 = puntaje(i,cal_4,punt_r);

#Ejercicio 6
punt_r = 10
correcto = int(0)
estatus = False
respuestaa = []
conteo = 0
def instrucciones_6():
    print()
    print("Ejercicio 6")
    print()
    print("Claudia quiere pasar una carpeta de fotografias de su pc a su memoria USB.")
    print()
    print("Album 1 --- 100 MB")
    print("Album 2 --- 150 MB") 
    print("Album 3 --- 90  MB") 
    print("Album 4 --- 170 MB") 
    print("Album 5 --- 60  MB") 
    print("Album 6 --- 180 MB") 
    print("Album 7 --- 75  MB")
    print("Album 8 --- 124 MB")
    print()
    print("Si la carpeta de fotografias pesa 350MB. ¿Es posible pasar los datos a la memoria USB?")
    print("Selecciona los dos albumes que deberias eliminar")
instrucciones_6()
while estatus == False:
    conteo = conteo + 1
    respuestaa = []
    if conteo > 1:
        print("Intento: ", conteo,"/5")
    for i in range (2):
        revision = False
        while revision == False:
            edad = 0
            respuesta = input("Ingresa tu respuesta " + str(i+1) + "/2: ")
            try:
                edad = int(respuesta)
                revision = True
                respuestaa.append(edad)
            except ValueError:
                print()
                print("Error, tu respuesta no es valida")
                print("Asegurate de introducir un número")
                print()
                revision = False
    if (4 in respuestaa) and (6 in respuestaa):
        estatus = True
        os.system("cls")
        print("Correcto. Siguiente pregunta")
    elif conteo == 5:
        estatus = True
    else:
        print("¿Necesitas ayuda?")
        print("1. Si. Necesito ayuda")
        print("2. No, quiero intentarlo de nuevo")
        print()
        revision1 = False
        while revision1 == False:
            ayuda = input("Responde únicamente 1 o 2 con número para continuar: ")
            try:
                asd = int(ayuda)
                revision1 = True
            except ValueError:
                print()
                print("Error, tu respuesta no es valida")
                print("Asegurate de introducir un número")
                print()
            if ayuda == "1":
                estatus = True
                os.system("cls")
                print()
                instrucciones_6()
                print()
                print("-------------------------------------------------------------------------------------------------------------------------")
                print()
                print("¿Que nos pide este ejercicio?")
                print()
                print("Primero debemos observar cuales datos nos pide la pregunta y cuales nos da")
                print()
                print("Este nos dice que debemos encontrar dos albumes que al eliminarlos, podamos tener 350MB de espacio libre en el USB")
                punt_r = punt_r - 2;
                estatus = False
            elif ayuda == "2":
                estatus = False
                punt_r = punt_r - 2;
            elif (ayuda != "1") and (ayuda != "2"):
                print()
                print("Tu respuesta no es reconocida, intenta otra vez")
                revision1 = False
cal_6 = puntaje(conteo,cal_5,punt_r);

#Ejercico 7
punt_r = 10
correcto = int(0)
estatus = False
conteo = 0
revision = False
def instrucciones_7():
    print()
    print("Ejercicio 7")
    print()
    print("Se aplicará una infusion intravenosa a un pasciente, a un ritmo de 30 gotas por minuto durante 3 horas")
    print("Si se aplicara la infusión a un factor de 25 gotas por mililitro. ¿Cual es el volumen de la infusión?")
    print("Escribe tu respuesta redondeada a dos decimales") 
    print()
instrucciones_7()
while estatus == False:
    conteo = conteo + 1
    if conteo > 0:
        print()
        print("Intento: ", conteo,"/5")#Print the aatempt
        print("Escribe tu respuesta") 
    revision = False
    while revision == False:
        edad = 0
        respuesta = input("Respuesta: ")
        try:
            edad = int(respuesta)
            revision = True
        except ValueError:
            print()
            print("Error, tu respuesta no es valida")
            print("Asegurate de introducir un número")
            print()
            revision = False
        revision = True
    if edad == 216:
        estatus = True
        print("Correcto. Siguiente pregunta")
    elif conteo == 5:
        estatus = True
    else:
        print("¿Necesitas ayuda?")
        print("1. Si. Necesito ayuda")
        print("2. No, quiero intentarlo de nuevo")
        print()
        revision1 = False
        while revision1 == False:
            ayuda = input("Responde únicamente 1 o 2 con número para continuar: ")
            try:
                asd = int(ayuda)
                revision1 = True
            except ValueError:
                print()
                print("Error, tu respuesta no es valida")
                print("Asegurate de introducir un número")
                print()
            if ayuda == "1":
                estatus = True
                os.system("cls")
                print()
                instrucciones_7()
                print()
                print("-------------------------------------------------------------------------------------------------------------------------")
                print()
                print("Pista:")
                print()
                print("G = (gv)/60n")
                print()
                print("G es la frecuencia de goteo expresado en [gotas por minuto] ")
                print("g es el factor de goteo expresado en [gotas por mililitro]")
                print("V es el vólumen de la infusion intravenosa en [mililitros]")
                print("n es la cantidad de tiempo que durará la intravenosa expresado en [horas]")
                punt_r = punt_r - 2;
                estatus = False
            elif ayuda == "2":
                estatus = False
                punt_r = punt_r - 2;
            elif (ayuda != "1") and (ayuda != "2"):
                print("Tu respuesta no es reconocida, intenta otra vez")
                revision1 = False
cal_7 = puntaje(conteo,cal_6,punt_r);


#jercicio 8
punt_r = 10
correcto = int(0)
estatus = False
conteo = 0
revision = False
revision1 = False
correcta = ["SS", "CC", "SC", "CS"]
def instrucciones_8():
    print()
    print("Ejercicio 8")
    print()
    print("Imagina que lanzamos una moneda 2 veces")
    print("Escribe todas las posibilidades de este evento")
    print("Tendrás que ingresar primero la cantidad de eventos y después describir la posibilidad")
    print("Ejemplo:")
    print("Se realiza un lanzamiento y el primer resultado es Cara. El segundo es sol")
    print("La respuesta de este primer evento es: CS")
    print()
instrucciones_8()
while estatus == False:
    event = 0
    eventosfor = 0
    respuestaa = []
    tap = 0
    revision = False
    revision1 = False
    conteo = conteo + 1
    if conteo > 1:
        print("Intento: ", conteo,"/5")
        print()
    while revision1 == False:
        eventos = input("Ingresa la cantidad de eventos totales: ")
        try:
            eventosfor = int(eventos)
            revision1 = True
        except ValueError:
            print()
            print("Error, tu respuesta no es valida")
            print("Recuerda que aqui debes introducir la cantidad de eventos posibles expresado en números")
            revision1 = False
    for p in range (eventosfor):
        revision = False
        while revision == False:
            respuesta = input("Evento " + str(p+1) + ": ")
            try:
                edad = str(respuesta)
                indice = 0
                mayuscula = 0
                numero = 0
                for i in range ((len(respuesta))):
                    letra = edad[indice]
                    if letra.isupper() == True:
                        mayuscula = mayuscula + 1
                    indice = indice + 1
                if mayuscula == 2:
                    revision = True
                    respuestaa.append(edad)
                else:
                    edad = int(respuesta)
                    revision = False
            except ValueError:
                print()
                print("Error, tu respuesta no es valida")
                print("Asegurate de introducir dos letras Mayusculas")
                print(mayuscula)
                revision = False
        if (edad in correcta):
            tap = tap + 1
    for w in range (4):
        for h in range (eventosfor):
            a = respuestaa[h] in correcta[w]
            if a == True:
                event = event + 1
    if len(correcta) == len(respuestaa) and event == 4:
        estatus = True
        os.system("cls")
        print("Correcto. Siguiente pregunta")
    elif conteo == 3:
        estatus = True
    else:
        print("¿Necesitas ayuda?")
        print("1. Si. Necesito ayuda")
        print("2. No, quiero intentarlo de nuevo")
        print()
        revision1 = False
        while revision1 == False:
            ayuda = input("Responde únicamente 1 o 2 con número para continuar: ")
            try:
                asd = int(ayuda)
                revision1 = True
            except ValueError:
                print()
                print("Error, tu respuesta no es valida")
                print("Asegurate de introducir un número")
                print()
            if ayuda == "1":
                estatus = True
                os.system("cls")
                print()
                instrucciones_8()
                print()
                print("-------------------------------------------------------------------------------------------------------------------------")
                print()
                print("Pista:")
                print()
                print("Recuerda que la cantidad de eventos posibles se calcula usando las posibilidades y los eventos como en el primer ejemplo")
                print()
                estatus = False
                punt_r = punt_r - 2;
            elif ayuda == "2":
                estatus = False
                punt_r = punt_r - 2;
            elif (ayuda != "1") and (ayuda != "2"):
                print()
                print("Tu respuesta no es reconocida, intenta otra vez")
                revision1 = False
cal_8 = puntaje(conteo,cal_7,punt_r);

#ejercicios 9
punt_r = 10
correcto = int(0)
estatus = False
conteo = 0
revision = False
def instrucciones_9():
    print()
    print("Ejercicio 9")
    print()
    print("En una feria hay un mago jugando con un maso de cartas inglesas. Anuncia que el que logre sacar un [as] será el ganador")
    print("Si en un mazo de cartas inglesas hay 52 cartas. ¿Cual es la probabilidad de que al primer intento saques un [as] de cualquier color del maso?")
    print("Escribe tu respuesta redondeada a dos decimales") 
    print()
instrucciones_9()
while estatus == False:
    revision = False
    conteo = conteo + 1
    decimales = []
    if conteo > 1:
        print()
        print("Intento: ", conteo,"/5")
        print("Escribe tu respuesta")
    while revision == False:
        edad = 0
        respuesta = input("Respuesta: ")
        decimales = respuesta.split(".")
        try:
            if len(decimales) == 2:
                if (len(decimales[1]) > 2):
                    edad = int(respuesta)
                    revision= False
                elif (len(decimales[1]) <= 2):
                    revision = True
            elif len(decimales) == 1:
                edad = int(respuesta)
                revision = True
        except ValueError:
            print()
            print("Error, tu respuesta no es valida")
            print("Asegurate de introducir un número")
            print()
            revision = False
        #revision = True
    if respuesta == "0.08":
        estatus = True
        print("Correcto. Siguiente pregunta")
    elif conteo == 5:
            estatus = True
    else:
        print()
        print("Respuesta Incorrecta")
        print()
        print("¿Necesitas ayuda?")
        print("1. Si. Necesito ayuda")
        print("2. No, quiero intentarlo de nuevo")
        print()
        revision1 = False
        while revision1 == False:
            ayuda = input("Responde únicamente 1 o 2 con número para continuar: ")
            try:
                asd = int(ayuda)
                revision1 = True
            except ValueError:
                print()
                print("Error, tu respuesta no es valida")
                print("Asegurate de introducir un número")
                print()
            if ayuda == "1":
                estatus = True
                os.system("cls")
                print()
                instrucciones_9()
                print()
                print("-------------------------------------------------------------------------------------------------------------------------")
                print()
                print("Pista: ")
                print()
                print("Las cartas inglesas tienen 52 cartas dividida entre 4 tipos diferentes y dos colores distintos")
                print()
                print("Solo Existe un as por tipo de carta")
                estatus = False
                punt_r = punt_r - 2;
            elif ayuda == "2":
                estatus = False
                punt_r = punt_r - 2;
            elif (ayuda != "1") and (ayuda != "2"):
                print("Tu respuesta no es reconocida, intenta otra vez")
                revision1 = False
cal_9 = puntaje(conteo,cal_8,punt_r);
#Ejercicio 10
punt_r = 10
correcto = int(0)
estatus = False
conteo = 0
revision = False
def instrucciones_10():
    print()
    print("Ejercicio 10")
    print()
    print("Estas vacaciones, los papás de jorge le dijeron que si su promedio en la escuela era mayor a 76 entonces le darian un sorpresa")
    print("Matematicas: 70  Ciencias: 80  Español: 95 Geografia: 90  Ingles: 85  Computación: 100")
    print()
    print("Escribe tu respuesta redondeada a dos decimales") 
    print()
instrucciones_10()
while estatus == False:
    conteo = conteo + 1
    if conteo > 1:
        print()
        print("Intento: ", conteo,"/5")
        print("Escribe tu respuesta") 
    revision = False
    while revision == False:
        edad = 0
        respuesta = input("Respuesta: ")
        decimales = respuesta.split(".")
        try:
            if len(decimales) == 2:
                if (len(decimales[1]) > 2):
                    edad = int(respuesta)
                    revision= False
                elif (len(decimales[1]) <= 2):
                    revision = True
            elif len(decimales) == 1:
                edad = int(respuesta)
                revision = True
        except ValueError:
            print()
            print("Error, tu respuesta no es valida")
            print("Asegurate de introducir un número")
            print()
            revision = False
            #revision = True
    if (respuesta == "86.67") or (respuesta == "86.66"):
        estatus = True
        print("Correcto. Siguiente pregunta")
    if conteo == 5:
        estatus == True
    elif respuesta != "86.67" and respuesta != "86.66":
        print()
        print("Respuesta Incorrecta")
        print()
        print("¿Necesitas ayuda?")
        print("1. Si. Necesito ayuda")
        print("2. No, quiero intentarlo de nuevo")
        print()
        revision1 = False
        while revision1 == False:
            ayuda = input("Responde únicamente 1 o 2 con número para continuar: ")
            try:
                asd = int(ayuda)
                revision1 = True
            except ValueError:
                print()
                print("Error, tu respuesta no es valida")
                print("Asegurate de introducir un número")
                print()
            if ayuda == "1":
                estatus = True
                os.system("cls")
                print()
                instrucciones_10()
                print()
                print("-------------------------------------------------------------------------------------------------------------------------")
                print()
                print("Este se trata de un problema de estadistica")
                print()
                print("Para obtener el promedio de un conjunto de datos se toman en cuenta cosas como el total de la suma de los datos y la cantidad de datos sumados")
                print()
                estatus = False
                punt_r = punt_r - 2;
            elif ayuda == "2":
                estatus = False
                punt_r = punt_r - 2;
            elif (ayuda != "1") and (ayuda != "2"):
                print("Tu respuesta no es reconocida, intenta otra vez")
                revision1 = False

cal_10 = puntaje(conteo,cal_9,punt_r);
print("Los resultados de tu examén de aprendizaje es de:", cal_10)
arch = open('datospersonales.txt','a');
calificacion1 = "Calificación de tu Examen de Aprendizaje: " + str(cal_10) + "\n"
arch.write(calificacion1)
arch.close()
print()
print("Oprime ENTER para continuar")

input()

def examen():
    punt = 0;
    correcta = 0;
    incorrecta = 0;

    def pregunta_1(punt, correcta, incorrecta):
        print('Ejercicio 1');
        print('Cuando son las 7:00 de la tarde en Sydney, ¿Qué hora es en Berlín?');
        print('Primero solo ingrese el número de la hora, sin el am o pm; no se acepta respuesta como 13 horas');
        Resp = input('Ingrese el número de su respuesta: ');
        print('¿am o pm?');
        print('1. am');
        print('2. pm');
        Resp_2 = int(input('Ingrese el número de su elección: '));
        if Resp_2 == 1: # Asegurar que la respuesta tendrá am o pm
            Resp_F = Resp + 'am'; 
            print(Resp_F);
        elif Resp_2 == 2:
            Resp_F = Resp + 'pm';
            print(Resp_F);
        Resp_Correct = '10am';
        if Resp_F == Resp_Correct:
            correcta = correcta + 1; # Sumar a las preguntas correctas
            punt = punt + 10;
            return (punt, correcta, incorrecta)
        elif Resp_F != Resp_Correct:
            incorrecta = incorrecta + 1;
            return (punt, correcta, incorrecta)
    
#################################################################################################################################
    
    def pregunta_2(punt, correcta, incorrecta):
        print('Ejercicio 2');
        print('¿Cuántas combinaciones diferentes podría seleccionar Jaime?');
        Resp = int(input('Ingrese el número de su respuesta: '));
        if Resp == 6:
            correcta = correcta + 1 # Sumar a las preguntas correctas
            punt = punt + 10;
            return (punt, correcta, incorrecta)
        else:
            incorrecta = incorrecta + 1;
            return (punt, correcta, incorrecta)

####################################################################################################################################

    def pregunta_3(punt, correcta, incorrecta):
        print('Ejercicio 3');
        print('¿Cuál es la secuencia de teclas que deberás presionar para que el resultado sea el más cercano a 100?');
        print('La respuesta será por secuencia, por ejemplo AMAM');
        Resp = input('Ingrese la secuencia de su respuesta: ');
        if Resp == 'MMA' or Resp == 'mma':
            correcta = correcta + 1 # Add to the correct questions
            punt = punt + 10;
            return (punt, correcta, incorrecta)
        else:
            incorrecta = incorrecta + 1;
            return (punt, correcta, incorrecta)
####################################################################################################################################
    
    def pregunta_4(punt, correcta, incorrecta):
        print('Ejercicio 4');
        print ('¿A partir de qué edad la frecuencia cardíaca recomendada aumenta como resultado de la introducción de la fórmula nueva?');
        Resp = int(input('Ingrese su respuesta: '));
        if Resp == 40 or Resp == 41:
            correcta = correcta + 1 # Add to the correct questions
            punt = punt + 10;
            return (punt, correcta, incorrecta)
        else:
            incorrecta = incorrecta + 1;
            return (punt, correcta, incorrecta)

#####################################################################################################################################

    def pregunta_5(punt, correcta, incorrecta):
        print('Ejercicio 5');
        print('¿Cuánto dinero recibió en dólares de Singapur?');
        Resp = int(input('Ingrese su respuesta: '));
        if Resp == 975:
            correcta = correcta + 1; # Add to the correct questions
            punt = punt + 10;
            return (punt, correcta, incorrecta)
        else:
            incorrecta = incorrecta + 1;
            return (punt, correcta, incorrecta)

#######################################################################################################################################################

    def pregunta_6(punt, correcta, incorrecta):
        estatus = False
        conteo = 0
        revision = False
        print()
        print("Ejercicio 6")
        print()
        print("Una caja se llena con 8 tarjetas de color rojo, 2 tarjetas de color azul y 4 tarjetas de color verde")
        print("Si se elije una carta al azar de esta caja. ¿Cual es la probabilidad de que la tarjeta que saque NO sea de color azul?")
        while estatus == False: 
            revision = False
            while revision == False:
                respuesta = input("Respuesta: ")
                decimales = respuesta.split(".")
                try:
                    if len(decimales) == 2:
                        if (len(decimales[1]) > 4):
                            edad = int(respuesta)
                            revision= False
                        elif (len(decimales[1]) <= 4):
                            revision = True
                    elif len(decimales) == 1:
                        edad = int(respuesta)
                        revision = True
                except ValueError:
                    print()
                    print("Error, tu respuesta no es valida")
                    print("Asegurate de introducir un número y usar solo 4 posiciones decimales después del punto")
                    print()
                    revision = False
            if respuesta == "0.8571":
                estatus = True
                correcta = correcta + 1
                punt = punt + 10
                return (punt, correcta, incorrecta)
            elif respuesta != "0.8571":
                incorrecta = incorrecta + 1
                return (punt, correcta, incorrecta)
            
            

#####################################################################################################################################################
            
    def pregunta_7(punt, correcta, incorrecta):
        estatus = False
        revision = False
        print()
        print("Ejercicio 7")
        print()
        print("Como se puede ver, utiliza un cuadrado para el Nivel 1, tres cuadrados para el Nivel 2, y seis para el Nivel 3")
        print("¿Cuántos cuadrados en total deberá usar para construir hasta el cuarto nivel?")
        print()
        print("                    ----")
        print("                    |  |")
        print("         ----       -------")
        print("         |  |       |  |  |")
        print(" ----    -------    ----------")
        print(" |  |    |  |  |    |  |  |  |")
        print(" ----    -------    ----------")
        print()
        print("Nivel 1  Nivel 2     Nivel 3")
        while estatus == False:
            while revision == False:
                respuesta = input("Respuesta: ")
                decimales = respuesta.split(".")
                try:
                    if len(decimales) == 2:
                        if (len(decimales[1]) > 2):
                            edad = int(respuesta)
                            revision= False
                        elif (len(decimales[1]) <= 2):
                            revision = True
                    elif len(decimales) == 1:
                        edad = int(respuesta)
                        revision = True
                except ValueError:
                    print()
                    print("Error, tu respuesta no es valida")
                    print("Asegurate de introducir un número")
                    print()
                    revision = False
            #revision = True
            if (respuesta == "10"):
                estatus = True
                punt = punt + 10
                correcta = correcta + 1
                return(punt, correcta, incorrecta)
            elif respuesta != "10":
                incorrecta = incorrecta + 1
                return (punt, correcta, incorrecta)
            
###############################################################################################################################################
            
    def pregunta_8(punt, correcta, incorrecta):
        estatus = False
        revision = False
        print()
        print("Ejercicio 8")
        print()
        print("Si (C^2) = (a^2) + (b^2)")
        print("         /|")
        print("        / |")
        print("       /  |")
        print("      /   |")
        print("c=?  /    |  a = 4")
        print("    /     |")
        print("   /      |")
        print("  /       |")
        print(" /        ¬")
        print(" ----------")
        print("    b = 5")
        print()
        print("Calcula el valor de la hipotenusa C")
        while estatus == False:
            revision = False
            while revision == False:
                edad = 0
                respuesta = input("Respuesta: C =")
                decimales = respuesta.split(".")
                try:
                    if len(decimales) == 2:
                        if (len(decimales[1]) > 2):
                            edad = int(respuesta)
                            revision= False
                        elif (len(decimales[1]) <= 2):
                            revision = True
                    elif len(decimales) == 1:
                        edad = int(respuesta)
                        revision = True
                except ValueError:
                    print()
                    print("Error, tu respuesta no es valida")
                    print("Asegurate de introducir un número y usar solo 2 posiciones decimales después del punto")
                    print()
                    revision = False
                #revision = True
            if respuesta == "25":
                estatus = True
                punt = punt + 10
                correcta = correcta + 1
                return (punt, correcta, incorrecta)
            elif respuesta != "25":
                incorrecta = incorrecta + 1
                return (punt, correcta, incorrecta)

######################################################################################################################################
            
    def pregunta_9(punt, correcta, incorrecta):
        correcto = int(0)
        estatus = False
        revision = False
        print()
        print("Ejercicio 9")
        print()
        print("Elena fue en bicicleta desde su casa al rio que esta a 4 km de distancia. Esto le tomó 9 minutos. Luego volvio a casa por una ruta mas corta de 3km, en esta solo se taro 6 minutos")
        print("¿Cual fue la velocidad promedio, en kilometros por hora (km/h) de Elena entre sus dos recorridos?")
        print("Escribe tu resultado en números y redondeado a dos espacios decimales después del punto (Si aplica)")
        print()
        while estatus == False:
            revision = False
            while revision == False:
                edad = 0
                respuesta = input("Respuesta:")
                decimales = respuesta.split(".")
                try:
                    if len(decimales) == 2:
                        if (len(decimales[1]) > 2):
                            edad = int(respuesta)
                            revision= False
                        elif (len(decimales[1]) <= 2):
                            revision = True
                    elif len(decimales) == 1:
                        edad = int(respuesta)
                        revision = True
                except ValueError:
                    print()
                    print("Error, tu respuesta no es valida")
                    print("Asegurate de introducir un número y usar solo 2 posiciones decimales después del punto")
                    print()
                    revision = False
                #revision = True
            if respuesta == "28" or respuesta == "28.2":
                estatus = True
                punt = punt + 10
                correcta = correcta + 1
                return (punt, correcta, incorrecta)
            elif respuesta != "28" or respuesta != "28.2":
                incorrecta = incorrecta + 1
                return (punt, correcta, incorrecta)
########################################################################################################################################################


    def pregunta_10(punt, correcta, incorrecta):
        correcto = int(0)
        estatus = False
        revision = False
        print()
        print("Pregunta 10")
        print()
        print("En una clase hay 20 alumnos. La estatura media de la clase es de 120cm")
        print("Si se encontro un error en la estatura de uno de los alumnos y en vez de medir 120cm mide 147")
        print("¿Cual es el valor correcto de la media de la clase en metros?")
        print()
        while estatus == False:
            revision = False
            while revision == False:
                edad = 0
                respuesta = input("Respuesta:")
                decimales = respuesta.split(".")
                try:
                    if len(decimales) == 2:
                        if (len(decimales[1]) > 2):
                            edad = int(respuesta)
                            revision= False
                        elif (len(decimales[1]) <= 2):
                            revision = True
                    elif len(decimales) == 1:
                        edad = int(respuesta)
                        revision = True
                except ValueError:
                    print()
                    print("Error, tu respuesta no es valida")
                    print("Asegurate de introducir un número y usar solo 2 posiciones decimales después del punto")
                    print()
                    revision = False
            #revision = True
            if respuesta == "1.47" or respuesta == "1.47":
                estatus = True
                punt = punt + 10
                correcta = correcta + 1
                return (punt, correcta, incorrecta)
            elif respuesta != "1.47" or respuesta != "1.47":
                incorrecta = incorrecta + 1
                return (punt, correcta, incorrecta)
    (punt, correcta, incorrecta) = pregunta_1(punt, correcta, incorrecta)
    (punt, correcta, incorrecta) = pregunta_2(punt, correcta, incorrecta)
    (punt, correcta, incorrecta) = pregunta_3(punt, correcta, incorrecta)
    (punt, correcta, incorrecta) = pregunta_4(punt, correcta, incorrecta)
    (punt, correcta, incorrecta) = pregunta_5(punt, correcta, incorrecta)
    (punt, correcta, incorrecta) = pregunta_6(punt, correcta, incorrecta)
    (punt, correcta, incorrecta) = pregunta_7(punt, correcta, incorrecta)
    (punt, correcta, incorrecta) = pregunta_8(punt, correcta, incorrecta)
    (punt, correcta, incorrecta) = pregunta_9(punt, correcta, incorrecta)
    (punt, correcta, incorrecta) = pregunta_10(punt, correcta, incorrecta)
    print("Puntos: ", punt)
    print("Correctas: ", correcta)
    print("Incorrectas: ", incorrecta)
    arch = open('datospersonales.txt','a');
    linea1 = "Puntos del Examen Final: " + str(punt)
    arch.write(linea1)
    arch.close()
    
examen()
