n = int(input())

arr = list(map(int,input().split()))

dp = [0 for i in range(n)]

for i in range(n):
    if i==0:
        dp[i] = arr[i]
    elif i==1:
        dp[i] = arr[i]
    elif i==2:
        dp[i] = arr[i-2]+arr[i]
    else:
        dp[i] = max(dp[i-2]+arr[i],dp[i-1])

print(max(dp))
