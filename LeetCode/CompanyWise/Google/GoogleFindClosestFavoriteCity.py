from typing import List
import heapq

def main():
    n, m, l, s = list(map(int, input().split()))
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))

    favoriteCities = list(map(int, input().split()))

    # print(n, l, m, s)
    # print(edges)
    # print(favoriteCities)

    print(findClosesFavoriteCity(n, m, edges, favoriteCities, s))



"""
4 4 2 1
1 2 2
1 3 5
2 3 1
3 4 3
2 4

edges = [
        #u  v  w
        [1, 2, 2]
        [1, 3, 5],
        [2, 3, 1],
        [3, 4, 3]
        ]

favoriteCities= [2, 4]

fun(4, 4, e, fc, 1)
    ady = [
            [],
            [[2, 2], [5, 3]],
            [[1, 3]],
            [[4, 3]],
            [],
        ]

    dist = [inf, 0, 2, 5, inf]
    pq = [

            (5, 3),    
        ]
    fcs = {2, 4}

    pq true:
        dFS = 2
        c = 2

        w = 5, nC = 3:






"""   


# Dijkstra


def findClosesFavoriteCity(
        n: int,
        m: int,
        edges: List[List[int]], 
        favoriteCities: List[int],
        sourceCity: int) -> int:


    ady = [[] for _ in range(n + 1)] 

    for i in range(m):
        u, v, w = edges[i]
        ady[u].append([w, v])
        ady[v].append([w, u])

    dist = [float("inf")]*(n + 1)
    dist[sourceCity] = 0

    priorityQueue = []
    heapq.heappush(priorityQueue, (0, sourceCity))
    favoriteCitiesSet = set(favoriteCities)

    # print(priorityQueue)
    
    while priorityQueue:
        # print(priorityQueue)
        distFromSource, city = heapq.heappop(priorityQueue)

        if distFromSource > dist[city]:
            continue

        if city in favoriteCitiesSet:
            return city

        for weight, neighCity in ady[city]:

            if distFromSource + weight < dist[neighCity]:
                dist[neighCity] = distFromSource + weight
                heapq.heappush(priorityQueue, (dist[neighCity], neighCity))

    return 0
              



            


    
    
    


if  __name__ == "__main__":
    main()