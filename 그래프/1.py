# p.298 팀 결성

def find_parent(parent, x):
    if parent[x]!= x:
        find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
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

for _ in range(m):
    cal, a, b = map(int,input().split())
    if cal == 0:
        union(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")