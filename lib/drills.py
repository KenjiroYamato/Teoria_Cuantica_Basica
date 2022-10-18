nRnC = 0
m = None
x = None

def prettyMtrx(m, text):
    print(f"{text} \n")
    for i in range(len(m)):
        print(f"    |{m[i]}|")
    print("\n")

def identityCpx(n):
    """
        Recibe un tamaño y crea una matriz identidad del tamaño dado
        @Return Matriz
    """
    matriz =[[[0,0] for x in range(n)] for x in range(n)] 
    for i in range(n):
        for j in range(n):
            if(i==j):
                matriz[i][j] = [1,0]       
    return matriz 

def matrizGen(n):
    """genera una matriz de n x n lados vacia"""
    matriz = [[0 for x in range(n)] for x in range(n)] 
    return matriz

def matrizGenCpx(n):    
    """genera una matriz de n x n lados Con tuplas (a, b) con a parte real = 0 y b parte imaginaria = 0"""
    matriz = [[[float(input(f"      estado Real en row: ({c}) - col: ({f}) <- ")), float(input(f"estado Imaginario en row: ({c}) - col: ({f}) <- "))] for f in range(n)] for c in range(n)] 
    return matriz

def stateGen(n):
    """Genera un vector de n x 1 lados vacio"""
    matriz = [(float(input(f"estado Real número {x}: \n")), float(input(f"estado Real número {x}: \n"))) for x in range(n)]
    return matriz

def mtrxRealesAparteImaginarios(n):
    """Genera un vector con vector con dos pociciones una que tiene los numeros reales y 
    otra que tiene los numeros imaginarios de tal manera que si se suman las dos posiciones del vector respectivamente
    da como resultado una matriz con elementos complejos deseada
    @Return Vector
    """    
    matriz = [[[float(input(f"estado Real en row: ({c}) - col: ({f}) <- ")) for f in range(n)] for c in range(n)], [[float(input(f"estado Imaginario en row: ({c}) - col: ({f}) <- ")) for f in range(n)] for c in range(n)]]
    return [matriz[0], matriz[1]]

def stateGenCpx(n):
    """genera un vector de n x 1 lados Con tuplas (a, b) con a parte real = 0 y b parte imaginaria = 0"""
    matriz = [[float(input(f"estado Real número {x}: ")), float(input(f"estado Imaginario número {x}: "))] for x in range(n)]
    return matriz 

def stateGenCpxNormalize(n):
    """genera un vector de n x 1 lados Con tuplas (a, b) con a parte real = 0 y b parte imaginaria = 0 normalizado"""
    matriz = [(int(input(f"estado Real número {x}: ")), int(input(f"estado Imaginario número {x}: "))) for x in range(n)] 
    matrizModulos = [moduloCpx(x) for x in matriz] 
    resp = 0
    for i in matrizModulos:
        resp += i**2
    resp = resp**(1/2)
    matrizR = [(0,0) for x in range(len(matriz))]
    for i in range(len(matrizR)):
        matrizR[i] = (matriz[i][0]/resp, matriz[i][1]/resp)
    return matrizR

def moduloCpx(a):    
    """retorna el modulo de un número complejo"""    
    return (a[0]**2 + a[1]**2)**(1/2)

def transpose(m):  
    """Hace la Traspuesta de de una matriz"""      
    return list(list(x) for x in zip(*m))

def hermitianas(m):
    """genera una matriz a la que se le conjugan sus elementos y se hace su traspuesta"""
    a = list(map(lambda n: (conjugadoCpx(n[0]), conjugadoCpx(n[1])), m))
    return transpose(a)

def hermitianas_(m):
    """genera una matriz a la que se le conjugan sus elementos y se hace su traspuesta"""
    a = list(map(lambda n: conjugadoCpx(n), m))
    return transpose(a)

def esHermitiana(m):
    """Dice si una matriz es hermitiana
    @Return Boolean
    """
    if(hermitianas(m) == m):
        return True
    return False

def conjugadoCpx(a):
    """retorna el conjugado de un número complejo a"""
    conjugado = list(a)
    conjugado[1] *= -1
    return conjugado

def conjugadorCpx(mtrx):
    """Conjuga lso elementos de una matriz"""
    return [conjugadoCpx(x) for x in mtrx]    
 
def directionMarbles(mtrx):
    """
    Recibe una matriz que llenara cumpliendo la condicion de que sea doblemente estocastica.
    pedira el numero de la fila a la que quiere asignarle una entrada
    """
    m = mtrx  
    to = 0
    for i in range(len(m)):                
        to = int(input(f"Canica en posición {i} hacia -> \n"))        
        m[to][i] = 1        
    return mtrx

def directionMarblesProb(mtrx):
    """
    Recibe una matriz que llenara cumpliendo la condicion de que sea doblemente estocastica.
    pedira el numero de la fila a la que quiere asignarle una entrada y ademas el numero de posibles salidas de la canica.
    (importante: si se escogio salidas multiples todas deben apuntar hacia entradas diferentes)
    """
    m = mtrx  
    to = 0
    cont = 0
    for i in range(len(mtrx)):      
        cont = 0    
        nSalidas = int(input(f"Numero de posibles salidas de la posición {i}:  \n"))        
        while(cont != nSalidas):                  
            to = int(input(f"canica en posicion {i} hacia -> \n"))        
            m[to][i] = 1/nSalidas  #no se pueden repetir las salidas porque se genera un bug, si hay 3 salidas y 3 posiciónes no puede quedar una posición sin entrada
            cont += 1
    return mtrx

def directionMarblesQuantum(mtrx):
    """
    Recibe una matriz que llenara cumpliendo la condicion de que sea doblemente estocastica.
    pedira el numero de la fila a la que quiere asignarle una entrada y ademas el numero de posibles salidas de la canica.
    (importante: si se escogio salidas multiples todas deben apuntar hacia entradas diferentes)
    """
    m = mtrx  
    to = 0
    cont = 0
    for i in range(len(mtrx)):      
        cont = 0
        nSalidas = int(input(f"Numero de posibles salidas de la posición {i}:  \n"))   

        while(cont != nSalidas):   

            to = int(input(f"canica en posicion {i} hacia -> \n")) 

            if (input("**¿El Numero es Negativo?** :: Si -> (Any Charater), No -> Enter ::  \n") == ""):     
                m[to][i] = (0, ((1/(nSalidas))**(1/2))) #no se pueden repetir las salidas porque se genera un bug, si hay 3 salidas y 3 posiciónes no puede quedar una posición sin entrada
                cont += 1  
                continue

            m[to][i] = (0, -((1/(nSalidas))**(1/2)))
            cont += 1
    return mtrx

def dot(v1, v2):
    """producto punto entre dos vectores"""
    if not v1:       
        return 0        
    return v1[0] * v2[0] + dot(v1[1:],v2[1:])

def dotCpx(v1, v2):
    """producto punto entre dos vectores con elementos complejos como tuplas"""
    acumR = 0
    acumI = 0
    for i in range(len(v1)):
        acumR += productoCpx(v1[i], v2[i])[0]
        acumI += productoCpx(v1[i], v2[i])[1]
    return [acumR, acumI]


def productMandX(M, x):
    """Realiza la multiplicacion entre una matriz y un vector"""
    result = [0 for x in range(len(x))]
    for i in range(len(M)):
        result[i] = round(dot(M[i], x), 4)
    return result      

def productMandXCpx(M, x):
    """Realiza la multiplicacion entre una matriz y un vector con elementos complejos como tuplas"""
    result = [[0, 0] for i in range(len(x))]
    for i in range(len(x)):
        result[i] = dotCpx(M[i], x)
    return result 


def productMxM(M, M_): 
    """Realiza la multiplicacion entre una matriz y otra matriz con elementos complejos como listas"""
    result = [[[0,0] for x in range(len(M[0]))] for x in range(len(M_[0]))] 
    for i in range(len(M_[0])):
        for j in range(len(M_[0])):
            result[i][j] = dotCpx(M[i], M_[j])
    return result 

def productCxM(c, M):
    """Realiza la multiplicacion entre una costrante y un vector con elementos complejos como listas"""
 
    result = [[(0,0) for x in range(len(M))] for x in range(len(M))] 
    for i in range(len(M[0])):
        for j in range(len(M[0])):
            result[i][j] = productoCpx(c, M[i][j])
    return result 

def restaMtrx(M, M_):
    """Resta dos matrices de igual tamaño"""
    result = [[(0,0) for x in range(len(M))] for x in range(len(M_))] 
    for i in range(len(M)):
        for j in range(len(M_)):
            result[i][j] = restaCpx(M[i][j], M_[i][j])
    return result 

def restaCpx(a, b):
    """Recibe dos nuemros complejos a, b y le resta b a a"""
    result = [(a[0] - b[0]), (a[1] - b[1])]
    return result

def productoCpx(a, b):
    """Realiza el producto de dos numeros complejos a y b"""
    result =  [((a[0] * b[0]) - (a[1]) * b[1]), (a[0] * b[1] + a[1] * b[0])]
    return result    

def restaM(a, b):
    result = [[[0,0] for x in range(len(a))] for x in range(len(b))] 
    for i in range(len(a)):
        for j in range(len(b)):
            result[i][j] = restaCpx(a[i][j], b[i][j])
    return result 
    






   