import random
import statistics

def Tablero():
    i=1
    n=0
    posiciones=[0,0,0,0,0]
    iteracion1=0
    Generacion=1
    while i<6:
        lista=['0    ','0    ','0    ','0    ','0    ']
        salida=random.choice(['000','001','010','011','100'])#Posición aleatoria
        print("Posicion para la reina "+str(i)+": "+str(salida))#Acomodo de cada gen
        if(salida=='000'):
            lista[0]='Reina'   
        if(salida=='001'):
            lista[1]='Reina'
        if(salida=='010'):
            lista[2]='Reina'  
        if(salida=='011'):
            lista[3]='Reina'  
        if(salida=='100'):
            lista[4]='Reina'
            
        if(n==0):
            lista1=lista
            posiciones[0]=salida
        if(n==1):
            lista2=lista
            posiciones[1]=salida
        if(n==2):
            lista3=lista
            posiciones[2]=salida
        if(n==3):
            lista4=lista
            posiciones[3]=salida
        if(n==4):
            lista5=lista
            posiciones[4]=salida
       
        i+=1
        n+=1
    
    print("\n")
    print('Renglón 1'+str(lista1))
    print('Renglón 2'+str(lista2))
    print('Renglón 3'+str(lista3))
    print('Renglón 4'+str(lista4))
    print('Renglón 5'+str(lista5))
    
    print("\nLa población actual es: "+str(posiciones))
    
    #Aptitud
    repetir=0
    while(repetir==False):#Para trabajar con la nueva generación
        print("\n-------------------------FUNCIÓN DE EVALUACIÓN DE APTITUD-------------------------\n")
        print("Generacion: "+str(Generacion))
        print("\nVamos a evaluar la aptitud de nuestro individuo o población actual")
        j=0
        k=0
        l=0
        o=0
        p=0
        total=0
        
        if('000'==posiciones[0]):
            j+=1
        if('000'==posiciones[1]):
            j+=1
        if('000'==posiciones[2]):
            j+=1
        if('000'==posiciones[3]):
            j+=1
        if('000'==posiciones[4]):
            j+=1
        
        if(j==3 or j==4 or j==5):
            total+=2
        elif(j>1):
            total+=1
                
        if('001'==posiciones[0]):
            k+=1
        if('001'==posiciones[1]):
            k+=1
        if('001'==posiciones[2]):
            k+=1
        if('001'==posiciones[3]):
            k+=1
        if('001'==posiciones[4]):
            k+=1
        
        if(k==3 or k==4 or k==5):
            total+=2
        elif(k>1):
            total+=1
        
        if('010'==posiciones[0]):
            l+=1
        if('010'==posiciones[1]):
            l+=1
        if('010'==posiciones[2]):
            l+=1
        if('010'==posiciones[3]):
            l+=1
        if('010'==posiciones[4]):
            l+=1
        
        if(l==3 or l==4 or l==5):
            total+=2
        elif(l>1):
            total+=1
        
        if('011'==posiciones[0]):
            o+=1
        if('011'==posiciones[1]):
            o+=1
        if('011'==posiciones[2]):
            o+=1
        if('011'==posiciones[3]):
            o+=1
        if('011'==posiciones[4]):
            o+=1
                
        if(o==3 or o==4 or o==5):
            total+=2
        elif(o>1):
            total+=1
        
        if('100'==posiciones[0]):
            p+=1
        if('100'==posiciones[1]):
            p+=1
        if('100'==posiciones[2]):
            p+=1
        if('100'==posiciones[3]):
            p+=1
        if('100'==posiciones[4]):
            p+=1
                
        if(p==3 or p==4 or p==5):
            total+=2
        elif(p>1):
            total+=1
        
        print("\nSi hay dos reinas en la misma posición o sólo una en una posición la aptitud es buena")
        print("\nSi hay tres reinas o más en la misma posición la aptitud es media-mala")
        
        print("\nDe acuerdo a nuestra población actual la aptitud es: ")
        if(total<=1):
            print(total)
            print("\n\t\t\t\tLa aptitud es buena")
        else:
            print("\n\t\t\t\tLa aptitud es media-mala") 
            print(total)
        
        if(total!=0):
            #Selección
            print("\n-------------------------SELECCIÓN POR RULETA-------------------------\n")
            decimal=[]
            print("Sabemos que las posiciones dadas están en números binarios, así que para hacer la selección trabajaremos con decimales\n")
            print("000 = 0\n001 = 1\n010 = 2\n011 = 3\n100 = 4\n")
            print("Binario: "+str(posiciones))
            
            if(posiciones[0]=='000'):
                decimal.append(0)
            if(posiciones[0]=='001'):
                decimal.append(1)
            if(posiciones[0]=='010'):
                decimal.append(2)
            if(posiciones[0]=='011'):
                decimal.append(3)
            if(posiciones[0]=='100'):
                decimal.append(4)
                
            if(posiciones[1]=='000'):
                decimal.append(0)
            if(posiciones[1]=='001'):
                decimal.append(1)
            if(posiciones[1]=='010'):
                decimal.append(2)
            if(posiciones[1]=='011'):
                decimal.append(3)
            if(posiciones[1]=='100'):
                decimal.append(4)
                
            if(posiciones[2]=='000'):
                decimal.append(0)
            if(posiciones[2]=='001'):
                decimal.append(1)
            if(posiciones[2]=='010'):
                decimal.append(2)
            if(posiciones[2]=='011'):
                decimal.append(3)
            if(posiciones[2]=='100'):
                decimal.append(4)
        
            if(posiciones[3]=='000'):
                decimal.append(0)
            if(posiciones[3]=='001'):
                decimal.append(1)
            if(posiciones[3]=='010'):
                decimal.append(2)
            if(posiciones[3]=='011'):
                decimal.append(3)
            if(posiciones[3]=='100'):
                decimal.append(4)
                
            if(posiciones[4]=='000'):
                decimal.append(0)    
            if(posiciones[4]=='001'):
                decimal.append(1)    
            if(posiciones[4]=='010'):
                decimal.append(2)
            if(posiciones[4]=='011'):
                decimal.append(3)    
            if(posiciones[4]=='100'):
                decimal.append(4)
        
            print("\nDecimal: "+str(decimal))
            print("\nSacando sus probabilidades tenemos que:\n")
            suma=int(decimal[0])+int(decimal[1])+int(decimal[2])+int(decimal[3])+int(decimal[4])
            print("\tLa suma total es: "+str(suma))
            media=statistics.mean(decimal)
            print("\tLa media es: "+str(media))
            best=max(decimal)
            print("\tEl mejor es: "+str(best))
            worst=min(decimal)
            print("\tEl peor es: "+str(worst))
            prob1=decimal[0]/suma
            print("\nLa probabilidad de que se escoja el primer digito es:"+str(prob1))
            prob2=decimal[1]/suma
            print("La probabilidad de que se escoja el segundo digito es:"+str(prob2))
            prob3=decimal[2]/suma
            print("La probabilidad de que se escoja el tercer digito es:"+str(prob3))
            prob4=decimal[3]/suma
            print("La probabilidad de que se escoja el cuarto digito es:"+str(prob4))
            prob5=decimal[4]/suma
            print("La probabilidad de que se escoja el quinto digito es:"+str(prob5))
            
            resultado1=prob1+prob2
            resultado2=prob1+prob2+prob3
            resultado3=prob1+prob2+prob3+prob4
            resultado4=prob1+prob2+prob3+prob4+prob5
            print("\nTenemos entonces que el primer digito va a ir de: 0 a: "+str(prob1))
            print("\nEl segundo dígito va a ir de: "+str(prob1)+" a: "+str(resultado1))
            print("\nEl tercer digito va a ir de: "+str(resultado1)+" a: "+str(resultado2))
            print("\nEl cuarto digito va a ir de: "+str(resultado2)+" a: "+str(resultado3))
            print("\nEl quinto digito va a ir de: "+str(resultado3)+" a: "+str(resultado4))
            
            print("\n-------------------------CRUZA-------------------------\n")
            solucionado=0
            poblacion1=[]
            
            while(solucionado==False):
                print("\nGeneramos dos números aleatorios para continuar al siguiente proceso")
                a=1
                seleccionado=[]
                seleccionado2=[]
                
                while(a<3):
                    ruleta=random.random()
                    print("\nEl número "+str(a)+" es: "+str(ruleta))
                    if(ruleta>0 and ruleta<=prob1):
                        print("\nSe selecciona el primer dígito")
                        seleccionado.append(decimal[0])
                        seleccionado2.append(posiciones[0])
                    elif(ruleta>prob1 and ruleta<=resultado1):
                        print("\nSe selecciona el segundo dígito")
                        seleccionado.append(decimal[1])
                        seleccionado2.append(posiciones[1])
                    elif(ruleta>resultado1 and ruleta<=resultado2):
                        print("\nSe selecciona el tercer dígito")
                        seleccionado.append(decimal[2])
                        seleccionado2.append(posiciones[2])
                    elif(ruleta>resultado2 and ruleta<=resultado3):
                        print("\nSe selecciona el cuarto dígito")
                        seleccionado.append(decimal[3])
                        seleccionado2.append(posiciones[3])
                    elif(ruleta>resultado3 and ruleta<=resultado4):
                        print("\nSe selecciona el quinto dígito")
                        seleccionado.append(decimal[4])
                        seleccionado2.append(posiciones[4])
                    a+=1
                
                if(seleccionado[0]==seleccionado[1]):
                    print("\nLos números seleccionados son iguales por lo tanto no se puede hacer una cruza")
                    iteracion1+=1
                    solucionado=False
                else:
                    print("\nLos padres seleccionados fueron:")
                    print(seleccionado)
                    
                    print("\nAntes de definir el punto de cruza daremos la probabilidad de cruza que está entre .5 y .9")
                    print("\nPara este problema se escogió la probabilidad de .8")
                    probabilidad=random.random()
                    print(probabilidad)
                    if(probabilidad<=.8):
                        print("\nLa probabilidad cumple, podemos seguir")
                        print("\nVamos a generar la posición donde se van a cruzar nuestros cromosomas")
                        print("\nPara eso vamos a volver a los números binarios")
                        print(seleccionado2)
                        error=0
                        verificar1=0
                        verificar2=0
                        iteracion=0
                        while(error<2):
                            cruza=random.randrange(1,3)
                            print("\nEl punto de la cruza es: "+str(cruza))
                            progenitor1=seleccionado2[0]
                            progenitor2=seleccionado2[1]
                            if(verificar1==0):
                                hijo1=progenitor1[0:cruza]+progenitor2[cruza:3]
                                if(hijo1=='000' or hijo1=='001' or hijo1=='010' or hijo1=='011' or hijo1=='100'):
                                    print("Hijo 1: "+str(hijo1))
                                    error+=1
                                    verificar1=1
                                else:
                                    print(hijo1)
                                    print("No manejamos ese número de posición intentaremos con otro")
                            if(verificar2==0):
                                hijo2=progenitor2[0:cruza]+progenitor1[cruza:3]
                                if(hijo2=='000' or hijo2=='001' or hijo2=='010' or hijo2=='011' or hijo2=='100'):    
                                    print("Hijo 2: "+str(hijo2))
                                    error+=1
                                    verificar2=1
                                else:
                                    print(hijo2)
                                    print("No manejamos ese número de posición intentaremos con otro")
                            
                            iteracion+=1
                            if(iteracion==10):
                                print("\nLos padres generan hijos fuera del rango, por lo tanto se escogeran otros padres")
                                
                                error=3
                        
                        if(error==3):
                            solucionado=False
                            continue;
                                
                        print("\n-------------------------MUTACIÓN-------------------------\n")
                        print("\nAntes de definir el punto de mutación daremos la probabilidad de mutación que está entre .05 y .2")
                        print("\nPara este problema se escogió la probabilidad de .15")
                        hijos=1
                        error=0
                        while(hijos<3):
                            probabilidad=random.random()
                            print("\nPara el hijo "+str(hijos)+" su probabilidad es: "+str(probabilidad))
                            if(probabilidad<=.15):
                                print("\nLa probabilidad cumple, podemos seguir")
                                while(error<1):
                                    if(hijos==1):
                                        muta=random.randrange(3)
                                        print("\nEl punto de la mutación es: "+str(muta))
                                        print(hijo1[muta])
                                        if(hijo1[muta]==0):
                                            if(muta==0):
                                                hijo1_1='1'+hijo1[1:3]
                                            elif(muta==1):
                                                hijo1_1=hijo1[0]+'1'+hijo1[2]
                                            elif(muta==2):
                                                hijo1_1=hijo1[0:2]+'1'
                                            print(hijo1_1)
                                            print("hijo1 en IF")
                                            
                                            if(hijo1_1=='000' or hijo1_1=='001' or hijo1_1=='010' or hijo1_1=='011' or hijo1_1=='100'):
                                                print("Se guarda el hijo mutado")
                                                poblacion1.append(hijo1_1)
                                                error+=1
                                                hijos+=1
                                            else:
                                                print("No manejamos ese número de posición intentaremos con otro")
                                        else:
                                            if(muta==0):
                                                hijo1_1='0'+hijo1[1:3]
                                            elif(muta==1):
                                                hijo1_1=hijo1[0]+'0'+hijo1[2]
                                            elif(muta==2):
                                                hijo1_1=hijo1[0:2]+'0'
                                            print(hijo1_1)
                                            print("hijo1 en ELSE")
                                            if(hijo1_1=='000' or hijo1_1=='001' or hijo1_1=='010' or hijo1_1=='011' or hijo1_1=='100'):
                                                print("Se guarda el hijo mutado")
                                                poblacion1.append(hijo1_1)
                                                error+=1
                                                hijos+=1
                                            else:
                                                print("No manejamos ese número de posición intentaremos con otro")
                                    else:
                                        muta=random.randrange(3)
                                        print("\nEl punto de la mutación es: "+str(muta))
                                        print(hijo2[muta])
                                        if(hijo2[muta]==0):
                                            if(muta==0):
                                                hijo2_2='1'+hijo2[1:3]
                                            elif(muta==1):
                                                hijo2_2=hijo2[0]+'1'+hijo2[2]
                                            elif(muta==2):
                                                hijo2_2=hijo2[0:2]+'1'
                                            print(hijo2_2)
                                            print("En If")
                                            
                                            if(hijo2_2=='000' or hijo2_2=='001' or hijo2_2=='010' or hijo2_2=='011' or hijo2_2=='100'):
                                                print("Se guarda el hijo mutado")
                                                poblacion1.append(hijo2_2)
                                                error+=1
                                                hijos+=1
                                            else:
                                                print("No manejamos ese número de posición intentaremos con otro")
                                            
                                        else:
                                            if(muta==0):
                                                hijo2_2='0'+hijo2[1:3]
                                            elif(muta==1):
                                                hijo2_2=hijo2[0]+'0'+hijo2[2]
                                            elif(muta==2):
                                                hijo2_2=hijo2[0:2]+'0'
                                            print(hijo2_2)
                                            print("En else")
                                            
                                            if(hijo2_2=='000' or hijo2_2=='001' or hijo2_2=='010' or hijo2_2=='011' or hijo2_2=='100'):
                                                print("Se guarda el hijo mutado")
                                                poblacion1.append(hijo2_2)
                                                error+=1
                                                hijos+=1
                                            else:
                                                print("No manejamos ese número de posición intentaremos con otro")
                            else:
                                print("\nSalió fuera de la probabilidad, el hijo se guarda tal cual")
                                if(hijos==1):
                                    poblacion1.append(hijo1)
                                else:
                                    poblacion1.append(hijo2)
                                
                                print(poblacion1)
                                hijos+=1
                    else:
                        print("\nSalió fuera de la probabilidad, los digitos se clonan tal cual")
                        poblacion1.append(seleccionado2[0])
                        poblacion1.append(seleccionado2[1])
                        print(poblacion1)
                        
                    if(len(poblacion1)==6):
                        poblacion1.pop()
                        print("\nLa nueva población queda: "+str(poblacion1))
                        if(len(poblacion1)==len(set(poblacion1))):
                            print("La solución correcta es: "+str(poblacion1))
                            solucionado=True
                            repetir=True
                        else:
                            print("\nComo no es la solución correcta volvemos a repetir el proceso pero ahora con la nueva población generada")
                            posiciones=poblacion1
                            poblacion1=[]
                            Generacion+=1
                            solucionado=True
                            repetir=False
            
                    else:
                        solucionado=False
                
        else:
            print("\nLas reinas están bien acomodadas, no chocan entre ellas, por lo tanto no es necesario hacer selección, cruza y mutación")
            repetir=True
        
print("\nDiaz Ramirez Yoeli\n\n")
print("Se acomodarán 5 reinas de manera que no choquen entre ellas, por lo tanto se trabajará con un tablero de 5x5\n")
print("\n-------------------------GENERACIÓN DE NUESTRO INDIVIDUO-------------------------\n")
print("A continuación se mostrará el acomodo de las reinas de manera aleatoria.\n")
Tablero()