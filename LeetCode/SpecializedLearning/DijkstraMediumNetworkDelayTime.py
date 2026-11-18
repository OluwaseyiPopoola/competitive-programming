"""
https://leetcode.com/problems/network-delay-time/description/
"""

import heapq
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:

        ady = [[] for _ in range(n + 1)]
        
        for u, v, w in times:
            ady[u].append((w, v))

        dist = [float("inf")]*(n + 1)
        dist[k] = 0
        dist[0] = 0

        pq = []
        heapq.heappush(pq, (0, k))

        while pq:
            dFS, u = heapq.heappop(pq)

            if dFS > dist[u]:
                continue

            for w, nU in ady[u]:
                
                if dFS + w < dist[nU]:
                    dist[nU] = dFS + w
                    heapq.heappush(pq, (dist[nU], nU))

        print(dist)
        
        return -1 if float("inf") in dist else max((dist[1:k] + dist[k + 1:]))