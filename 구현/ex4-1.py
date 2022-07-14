n = int(input())
moves = list(input().split())
x,y = 0,0

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

move_dict = {
    "L":(0,-1),
    "R":(0,1),
    "U":(-1,0),
    "D":(1,0)
}

def in_range(x,y):
    return x>=0 and y>=0 and x<n and y<n

for move in moves:
    move_x, move_y = move_dict[move]
    new_x, new_y = x+move_x, y+move_y
    if in_range(new_x,new_y):
        x,y = new_x, new_y

print(x+1,y+1)