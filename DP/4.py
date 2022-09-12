n,m = map(int,input().split())

#n 개 / m원으로 만들기

money = [
    int(input())
    for _ in range(n)
]

dp = [1001]*(m+1)

dp[0] = 0
for i in range(n):
    for j in range(money[i], m+1):
        if dp[j - money[i]] != 1001:
            dp[j] = min(dp[j], dp[j-money[i]]+1)

print(dp[m])
