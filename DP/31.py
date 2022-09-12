t = int(input()) #테스트케이스의 개수

dxs = [-1,0,1]
dys = [1,1,1]

def in_range(x,y,n,m):
    return x<n and y<m and x>=0 and y>=0

def move(i,j, cnt,m):
    if cnt == m:
        return

    for k in range(3):
        nx = dxs[k]+i
        ny = dys[k]+j

        if in_range(nx,ny,n,m):
            origin_value = dp[nx][ny]
            new_value = arr[i][j]+arr[nx][ny]
            arr[nx][ny] = max(arr[i][j]+arr[nx][ny],dp[nx][ny])
            if dp[nx][ny] == new_value:
                move(nx,ny,cnt+1,m)


for _ in range(t):
    n,m = map(int,input().split())
    temp_arr = list(map(int,input().split()))
    arr = [
        [0 for _ in range(m)]
        for _ in range(n)
    ]

    start,end = 0,m
    for i in range(n):
        arr[i] = temp_arr[start:end]
        start = end
        end += m

    for i in range(n):
        for j in range(m):
            start_idx = arr[i][j]
            dp = [
                [0 for _ in range(m)]
                for _ in range(n)
            ]
            move(i,j,0,m)
