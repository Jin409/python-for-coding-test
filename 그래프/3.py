# p.303 커리큘럼

from collections import deque
from copy import deepcopy

n = int(input()) #듣고자 하는 강의의 수
indegree = [0 for _ in range(n+1)]
time = [0 for _ in range(n+1)]
graph = [
    []
    for _ in range(n+1)
]

for i in range(1,n+1):
    ans_arr = list(map(int,input().split()))
    time[i] = ans_arr[0] #들어야 하는 강의 시간
    for x in ans_arr[1:-1]:
        indegree[i]+=1
        graph[x].append(i)

def sol():
    q = deque()
    result = deepcopy(time)
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        idx = q.popleft()
        for data in graph[idx]:
            result[data] = max(result[data], result[idx]+time[data])
            indegree[data] -=1
            if indegree[data] == 0:
                q.append(i)

    for i in range(1, n+1):
        print(result[i])

sol()