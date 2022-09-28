# p.300 도시 분할 계획

'''
n개의 집과 m개의 길
2개로 분할하기
'''

def find_parent(parent, x):
    if parent[x] != x:
        find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int,input().split())
parent = [0 for _ in range(n+1)]

for i in range(n+1):
    parent[i] = i

edges = []

for _ in range(m):
    a, b, c = map(int,input().split())
    edges.append(c, a, b)

edges.sort()
last = 0
result = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result - last)

