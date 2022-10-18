import lib.drills as lib
from numpy import linalg

def main():
    n = int(input("numero de columnas y filas del sistema: "))   
    
    
    opcion = 1
     
    if(opcion==0):  #1. El sistema debe calcular la probabilidad de encontrarlo en una posición en particular.
        matrizNormalize = lib.stateGenCpxNormalize(n)
        posicionElegida = matrizNormalize[int(input("que posicion desea saber la probabilidad: "))]
        print(lib.moduloCpx(posicionElegida)**2)
        
    if(opcion == 1): #2. El sistema si se le da otro vector Ket debe buscar la probabilidad de transitar del primer vector al segundo.
        print(" primer ket:")
        matriz1 = lib.stateGenCpx(n)
        print("\n segundo Ket") 
        matriz2 = lib.stateGenCpx(n)        
        print(lib.dotCpx(lib.conjugadorCpx(matriz2), matriz1), end="\n")        
        
    if(opcion==2):  #1. Amplitud de transición. El sistema puede recibir dos vectores y calcular la probabilidad de transitar de el uno al otro después de hacer la observación
        print(" primer ket:")
        matriz1 = lib.stateGenCpxNormalize(n)
        print("\n segundo Ket") 
        matriz2 = lib.stateGenCpxNormalize(n)
        bra = lib.conjugadorCpx(matriz2)
        print(lib.dotCpx(bra, matriz1))
        
    if(opcion == 3):    #2. Ahora con una matriz que describa un observable y un vector ket, el sistema revisa que la matriz sea hermitiana, y si lo es, calcula la media y la varianza del observable en el estado dado.
        print("matriz herminitana, observable:")
        obser = lib.matrizGenCpx(n)
        if(not lib.esHermitiana(obser)):            
            print("el obserbable no es una matriz hermanitiana")
        else:
            print("ket del sistema: \n")
            ket = lib.stateGenCpx(n)
            obserbableKet = lib.dotCpx(lib.productMandXCpx(obser, ket), ket)
            delta = lib.restaM(obser, lib.productCxM(obserbableKet,  lib.identityCpx(n)))
                        
            mtrxVar = lib.productMxM(delta, lib.transpose(delta))
            var_ = lib.productMandXCpx(mtrxVar, ket)
            var = lib.dotCpx(var_, ket)            
            lib.prettyMtrx(delta, "delta = ")
            lib.prettyMtrx(mtrxVar, "Matriz Varianza = ")
            print(var)
            
    if(opcion == 4): #3. El sistema calcula los valores propios del observable y la probabilidad de que el sistema transite a alguno de los vectores propios después de la observación        
        parteRyI = lib.mtrxRealesAparteImaginarios(n)    
        valoeresPropiosR = linalg.eigvals(parteRyI[0])
        valoeresPropiosI = linalg.eigvals(parteRyI[1])
        if(valoeresPropiosI[1] == 0):
            valoeresPropiosI = linalg.eigvals(parteRyI[1])[::-1]
        temp = ["" for i in range(len(valoeresPropiosI))]
        cont = 0
        for i in valoeresPropiosR:
            temp[cont] = f"{valoeresPropiosR[cont]} + ({valoeresPropiosI[cont]})i"
            cont+=1
            
        print(temp)

main()