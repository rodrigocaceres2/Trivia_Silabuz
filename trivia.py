#!/usr/bin/env python3
#Colores para incluir en la trivia
WHITE = '\033[37m'
RED = '\033[31m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
RESET = '\033[39m'

#elegir el numero de preguntas a mostrar en la trivia
num_preguntas = 5

#importar un archivo csv conteniendo las preguntas y asignarlo a la variable "preguntas"
#la estructura del csv es "enunciado;numero de alternativa correcta;alternativa1;alternativa2;alternativa3;alternativa4"
import csv
preguntas = csv.reader(open('preguntas.csv'),delimiter =';')

#saltarse los nombres de columnas puestos como descripción
next(preguntas, None)

#volver lista a la variable preguntas  para acceder fácilmente a través de un índice
preguntas = list(preguntas)

#Mensaje de bienvenida
print (RED+"HOLA, BIENVENIDOS A MI TRIVIA :)\n\nA CONTINUACIÓN PRESENTO UNA SERIE DE PREGUNTAS SOBRE BIOLOGÍA QUE DE DEBERÁS RESPONDER ESCRIBIENDO LA ALTERNATIVA CORRECTA\n\nMUCHA SUERTE!!")
print ("\n===============================\n"+RESET)

#bucle para hacer repetitivo el ejercicio
condicion = "s"
while condicion in ["s","si","Sí","sí","SI","SÍ","sÍ","sI"]:
    #inicializar la variable de puntaje
    puntaje = 0
    #usar la biblioteca random para elegir una muestra de preguntas de todas las preguntas para incluir en la trivia
    import random
    preguntas_trivia = random.sample(preguntas, num_preguntas)
    #Hacer un bucle para presentar tres preguntas aleatorias del archivo csv de preguntas, i = 0 porque se usará tambien para pasar por los elementos de preguntas_trivia
    i = 0
    while i <= num_preguntas - 1:
        
        #Asignar la pregunta correcta a una variable (columna numero 1, (0-indx))
        alt_corr     = preguntas_trivia[i][1]
        
        #Mostrar el enunciado y las alternativas en pantalla
        print (YELLOW+"Pregunta ", i+1,":", preguntas_trivia[i][0])
        print (WHITE+"1. ", preguntas_trivia[i][2])
        print ("2. ", preguntas_trivia[i][3])
        print ("3. ", preguntas_trivia[i][4])
        print ("4. ", preguntas_trivia[i][5], RESET)
        #Recibir una respuesta escrita por el teclado
        respuesta = input(BLUE+"¿Cuál es el número de alternativa correcta?: ")
        #Determinar si la respuesta es correcta, incorrecta, o no válida
        if respuesta == alt_corr:
            print("\nRespuesta correcta")
            puntaje += 1
        elif respuesta in ['1','2','3','4']:
            print("\nRespuesta incorrecta")
        else:
            print("\nPor favor, elija una alternativa válida (un número de 1 al 4)")
        print("\n\n===================================\n")
         #Avanzar el bucle
        i += 1
            
    #MOSTRAR PUNTAJE FINAL EN ESCALA DE 20 Y UNA CALIFICACIÓN CUALITATIVA
    puntaje_v = (20 * puntaje) / num_preguntas
    puntaje_v = round(puntaje_v)

    print (MAGENTA+"Tu puntaje final es: ", puntaje_v, " de 20", "(",puntaje," de ",num_preguntas,"respuestas correctas )" )
    
    if puntaje_v <= 10:
        print("Necesitas estudiar mucho más :("+RESET)
    elif puntaje_v <= 15:
        print("Buena, aprobaste :)"+RESET)
    else:
        print("EXCELENTE, TE LUCISTE!! :D"+RESET)

    condicion = input(RED+"¿Deseas seguir practicando?(s/n): "+RESET)

    print("\n============================================\n\n")
   
