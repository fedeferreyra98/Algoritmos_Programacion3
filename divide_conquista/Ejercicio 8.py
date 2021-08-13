import numpy as np

def fixture(matrix):
    print()
    print(matrix)
    if len(matrix[0])== 2:
        matrix[0][1]=matrix[1][0]
        matrix[1][1]=matrix[0][0]
        print(matrix)
        return matrix
    else:
        longitud=len(matrix)
        mitad=longitud//2
        matrix[0:mitad, 0:mitad]=fixture(matrix[0:mitad, 0:mitad])
        print(matrix)
        matrix[mitad:, 0:mitad]=fixture(matrix[mitad:,0:mitad])
        matrix[0:mitad, mitad:]=matrix[mitad:, 0:mitad]
        matrix[mitad:, mitad:]=matrix[:mitad, :mitad]

        return matrix
    
    pass
if __name__ == '__main__':
    equipos = [1,2,3,4,5,6,7,8]
    matriz = np.zeros([len(equipos), len(equipos)])
    for k,i in enumerate(equipos):
        matriz[k][0]=i

    print(fixture(matriz))
