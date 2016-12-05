#Obtener, de forma recursiva, el orden del numero de ciclos hasta obtener 1
#Devuelve: numero de ciclos necesarios, -1 si entrada no es entero
def collatz(n):
    if not isinstance(n, (int,long)):
        return -1
    elif n==1:
        return 0
    else:
        if(n%2==0):
            return 1+collatz(n/2)
        else:
            return 1+ collatz(3*n+1)
#Obtener el numero que produce la secuencia de Collatz mas larga y su longitud
#Devuelve: (numero, longitud de secuencia de Collatz), -1 si la entrada no es un entero
def biggerCollatz(n):
    if not isinstance( n, ( int, long ) ):
        return -1
    
    numMax=0; 
    secMaxima=0;
    conocidos=dict()
    #Buscar la cantidad de elementos en la secuencia de cada numero
    #Usar un diccionario para recordar elementos ya conocidos
    for i in range(1, n+1):
        numActual=i
        cant=0
        primerNum=0 #primer numero de la secuencia de Collatz
        
        while numActual > 1 :
            if numActual % 2 == 0 :
                numActual/=2
            else:
                numActual=numActual * 3 + 1
            #encontrar primer numero de la secuencia de Collatz
            if primerNum == 0:
                primerNum=numActual
            #reducir calculos usando programacion dinamica (valores ya registrados)
            if numActual in conocidos:
                cant+=conocidos[numActual]
                numActual=1
            cant+=1
        #si la ultima secuencia es mas grande, registrarla como maximo    
        if cant > secMaxima:
            secMaxima=cant
            numMax=i
            
        #Almacenar la longitud de la secuencia iniciada con primerNum    
        if not(primerNum in conocidos):
            conocidos[primerNum]=cant-1
    return (numMax, secMaxima)

print biggerCollatz("a") #Devuelve -1
print biggerCollatz(10)
print collatz(100)
