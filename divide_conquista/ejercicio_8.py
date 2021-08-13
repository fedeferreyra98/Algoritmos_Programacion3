import numpy as np
def esPotencia2(x):
    while x>1:
        x=x/2
    return x==1
def fixture(matrix):
    print(matrix)
    print()
    if len(matrix[0])== 2:
        matrix[0][1]=matrix[1][0]
        matrix[1][1]=matrix[0][0]
        print(matrix)
        print()
        return matrix
    else:
        longitud=len(matrix)
        mitad=longitud//2
        matrix[0:mitad, 0:mitad]=fixture(matrix[0:mitad, 0:mitad])
        print(matrix)
        print()
        matrix[mitad:, 0:mitad]=fixture(matrix[mitad:,0:mitad])
        matrix[0:mitad, mitad:]=matrix[mitad:, 0:mitad]
        matrix[mitad:, mitad:]=matrix[:mitad, :mitad]

        return matrix
if __name__ == '__main__':
    cantidad = int(input("Introduzca la cantidad de equipos, potencia de 2: "))
    
    equipos = list(range(1, cantidad+1, 1))
    if cantidad%2 != 0:
        #Al ser impar, se necesita partidos de descanso (por eso se agrega 0)
        equipos.insert(0, 0)

    print(f"La lista de equipos es: {equipos}")
    if not esPotencia2(len(equipos)):
            print("No es potencia de 2.")
            exit()
    matriz = np.zeros([len(equipos), len(equipos)])
    for k,i in enumerate(equipos):
        matriz[k][0]=i

    print(fixture(matriz))
