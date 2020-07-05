# Tarea 1
import csv                                              # Para leer archivos .csv
# Se definen las variables para cada caracteristica
A = 0
B = 0
C = 0
D = 0
AB = 0
AC = 0
AD = 0
BC = 0
BD = 0
CD = 0
with open('lote.csv') as csvfile:                       # Se lee el archivo .csv
    creader = csv.reader(csvfile, delimiter =',')       # Cada espacio del array esta separado por una coma
    for row in creader:                                 # row[1], row[2], row[3] y row[4] representan la cantidad de caracteristicas A, B, C y D respectivamente, se le suma 1 a cada caracteristica cuando se presenta en una linea
        if row[1] == '1':
            A += 1
            if row[2] == '1':                           # Ademas, se agregan la cantidad de pares en cada linea del archivo
                AB += 1  
            if row[3] == '1':
                AC += 1
            if row[4] == '1':
                AD += 1        
        if row[2] == '1':
            B += 1
            if row[3] == '1':
                BC += 1
            if row[4] == '1':
                BD += 1               
        if row[3] == '1':
            C += 1
            if row[4] == '1':
                CD += 1      
        if row[4] == '1':
            D += 1
# Se calculan las probabilidades de cada caracteristica, "A, B, C y D" tienen la cantidad de 1s que hay en el documento leido para cada caracteristica                                 
    probA = float(A) / 500   
    probB = float(B) / 500   
    probC = float(C) / 500   
    probD = float(D) / 500  
# Se calculan las intersecciones, los pares encontrados en el documento leido estan en las variables AB, AC, AD, BC, BD y CD
    AnB = float(AB) / 500   
    AnC = float(AC) / 500   
    AnD = float(AD) / 500 
    BnC = float(BC) / 500   
    BnD = float(BD) / 500   
    CnD = float(CD) / 500   
    
# Pregunta 1 
# Se imprimen las probabilidades de cada caracteristica
    print('')
    print('Probabilidad de A: {} %'.format(probA))
    print('Probabilidad de B: {} %'.format(probB)) 
    print('Probabilidad de C: {} %'.format(probC)) 
    print('Probabilidad de D: {} %'.format(probD))    

# Pregunta 2
# Se imprimen las probabilidades de A dados B, C o D
    print('')
    print('')
    probAB = AnB/probB
    probAC = AnC/probC
    probAD = AnD/probD
    print('Probabilidad de A dado B: {} %'.format(probAB))
    print('Probabilidad de A dado C: {} %'.format(probAC))
    print('Probabilidad de A dado D: {} %'.format(probAD))
# Se imprimen las probabilidades de B dados A, C o D
    print('')
    probBA = AnB/probA
    probBC = BnC/probC
    probBD = BnD/probD
    print('Probabilidad de B dado A: {} %'.format(probBA))
    print('Probabilidad de B dado C: {} %'.format(probBC))
    print('Probabilidad de B dado D: {} %'.format(probBD))
# Se imprimen las probabilidades de C dados A, B, D
    print('')
    probCA = AnC/probA
    probCB = BnC/probB
    probCD = CnD/probD
    print('Probabilidad de C dado A: {} %'.format(probCA))
    print('Probabilidad de C dado B: {} %'.format(probCB))
    print('Probabilidad de C dado D: {} %'.format(probCD))
# Se imprimen las probabilidades de D dados A, B, C
    print('')
    probDA = AnD/probA
    probDB = BnD/probB
    probDC = CnD/probC
    print('Probabilidad de D dado A: {} %'.format(probDA))
    print('Probabilidad de D dado B: {} %'.format(probDB))
    print('Probabilidad de D dado C: {} %'.format(probDC))

# Pregunta 3
# Se considera el criterio de que si la diferencia entre la probabilidad de ocurrencia de una caracteristica y otra es menor o igual a 5%, estas son caracteristicas estadisticamente independientes
# Funcion que devuelve el porcentaje de diferencia entre la probabilidad de que ocurra una caracteristica y la probabildad de que ocurra esta caracteristica dado otra
# first: Probabilidad de que ocurra esta caracteristica
# second: Probabilidad de que ocurra esta caracteristica dado otra
# return: devuelve 100 si first y second son iguales, devuelve 9999 si second es cero, devuelve el porcentaje de diferencia entre first y second si no se cumplen ninguna de las anteriores
    def get_percentage(first, second):
        if first == second:
            return 1
        try:
            return (abs(first - second) / second) * 100.0
        except ZeroDivisionError:
            return 9999
    print('')
# Funcion que imprime en la pantalla los resultados
# eventone: primer caracteristica    
# eventtwo: segunda caracteristica 
# dependency: porcentaje de diferencia entre la probabilidad de que ocurra eventone y la probabildad de que ocurra eventone dado eventtwo  
    def prints_t(eventone, eventtwo, dependency):
        print('Entre {} y {}:'.format(eventone,eventtwo))
        if dependency == 9999:
            print('Son eventos mutuamente excluyentes, por lo tanto son eventos dependientes')
        elif dependency <= 5:
            print('La diferencia entre ambos es de {} %, por lo tanto se consideran eventos estadisticamente independientes'.format(dependency))   
        else:
            print('La diferencia entre ambos es mayor a 5 %, por lo tanto se consideran eventos estadisticamente dependientes')
        print('')
# Resultados de get_percentage                    
    depenAB = 0  
    depenAB = get_percentage(probA, probAB)        
    depenAC = 0  
    depenAC = get_percentage(probA, probAC)
    depenAD = 0  
    depenAD = get_percentage(probA, probAD)
    depenBA = 0  
    depenBA = get_percentage(probB, probBA)
    depenBC = 0  
    depenBC = get_percentage(probB, probBC)
    depenBD = 0  
    depenBD = get_percentage(probB, probBD) 
    depenDA = 0  
    depenDA = get_percentage(probD, probDA)   
    depenDB = 0  
    depenDB = get_percentage(probD, probDB)
    depenDC = 0  
    depenDC = get_percentage(probD, probDC)
# prints
    prints_t('A', 'B', depenAB)
    prints_t('A', 'C', depenAC)
    prints_t('A', 'D', depenAD)
    prints_t('B', 'A', depenBA)
    prints_t('B', 'C', depenBC)
    prints_t('B', 'D', depenBD)
    prints_t('D', 'A', depenDA)
    prints_t('D', 'B', depenDB)
    prints_t('D', 'C', depenDC)
                   
# Pregunta 4
# Se aplica teorema de Bayes para determinar la probabilidad de que, dada una caracteristica D haya tambien una caracterista A
    print('')
    probADbayes = (probDA * probA)/probD
    print('Por el teorema de Bayes, la probabilidad de que si hay una caracteristica tipo D tambien haya la caracteristica A es: {} %'.format(probADbayes))


