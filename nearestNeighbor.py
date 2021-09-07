from inputs.readFile import readFile
import sys
from timeit import default_timer as timer


def nearestNeighbor(matrix, source):
    # 1. escolha um vértice arbitrário como vértice atual.
    currentVertex = source

    # 2. descubra a aresta de menor peso que seja conectada ao vértice atual e a um vértice não visitado V.
    distanceNext = sys.maxsize
    nextVertex = 0
    visitedVertex = []
    lenPath = 0
    arrayDistances = []

    while lenPath < len(matrix[0])-1:
        for i in range(len(matrix[0])):
            if currentVertex != i and i not in visitedVertex:
                if distanceNext > float(matrix[currentVertex][i]):
                    distanceNext = float(matrix[currentVertex][i])
                    nextVertex = i

        # 3. faça o vértice atual ser V.
        V = currentVertex
        currentVertex = nextVertex

        # 4. marque V como visitado.
        visitedVertex.append(V)

        # 5. se todos os vértices no domínio estiverem visitados, encerre o algoritmo.
        if lenPath == len(matrix[0]):

            break
        # 6. Se não vá para o passo 2.
        else:
            lenPath += 1
            arrayDistances.append(distanceNext)
            distanceNext = sys.maxsize

    distanceLastToSource = float(matrix[visitedVertex[0]][nextVertex])
                                  
    arrayDistances.append(distanceLastToSource)
    visitedVertex.append(nextVertex)                             
    visitedVertex.append(visitedVertex[0])

    print('Menor custo =>', sum(arrayDistances), '\n')
    print('Melhor caminho =>', visitedVertex)


# matrix = [[0.0,  39.3,  37.2,  65.9,  56.3, 33.0, 51.0],
#           [39.0,  0.0,  38.9,  49.2,  79.4, 53.7, 68.2],
#           [37.2,  38.9,  0.0,  30.9,  43.0, 21.2, 30.4],
#           [65.9,  49.2,  30.9,  0.0,  64.1, 50.0, 50.6],
#           [56.5,  79.4,  43.0, 64.1, 0.0, 26.1, 13.6],
#           [33.0, 53.7, 21.2, 50.0, 26.1, 0.0, 18.0],
#           [51.0, 68.2, 30.4, 50.6, 13.6, 18.0, 0.0]]

matrix = readFile('inputs/five_dist.txt')

start = timer()
nearestNeighbor(matrix, 0)
end = timer()

print(f'{end - start}s')
