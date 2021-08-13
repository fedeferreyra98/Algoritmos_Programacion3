import numpy as np
from ejercicio_8 import fixture
def imprimirFixture(matriz):
    for i in range(1, len(matriz[0]),1):
        jornada=matriz[:, i]
        print(f"Jornada {i}:")
        conjunto=set()
        #print(jornada)
        for contrario, equipo in enumerate(matriz[:, 0]):
            if (not equipo in conjunto and not jornada[contrario] in conjunto):
                if equipo== "0":
                    print(f"No juega {jornada[contrario]}.")
                else:
                    print(f"{equipo} vs {jornada[contrario]}")
                conjunto.add(equipo)
                conjunto.add(jornada[contrario])
            #print(conjunto)
        print()


if __name__ == '__main__':
    entrada = 0
    equipos=[]
    print("Introduzca el nombre de los equipos. -1 para terminar (potencia de 2).")
    numero=1
    entrada=input(f"Equipo número {numero}: ")
    while entrada!= "-1":
        equipos.append(entrada)
        numero+=1
        entrada=input(f"Equipo número {numero}: ")
        

    
    if len(equipos)%2 != 0:
        #Al ser impar, se necesita partidos de descanso (por eso se agrega 0)
        equipos.insert(0, "0")
    print(f"La lista de equipos es: {equipos}")


    matriz = np.zeros([len(equipos), len(equipos)], dtype='U100')

    for k,i in enumerate(equipos):
        matriz[k][0]=i

    matriz=fixture(matriz)
    imprimirFixture(matriz)
