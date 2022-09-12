'''
X가 5로 나눠 떨어지면 5로 나누기
X가 3으로 나눠 떨어지면 3으로 나누기
X가 2로 나눠 떨어지면 2로 나누기
X에서 1을 빼기
'''
import sys

x = int(input())

arr = [sys.maxsize for _ in range(x+1)]
arr[1] = 0

for i in range(2,x+1):
    if i%5==0:
        arr[i] = min(arr[i//5]+1,arr[i])
    elif i%3==0:
        arr[i] = min(arr[i//3]+1,arr[i])
    elif i%2==0:
        arr[i] = min(arr[i//2]+1,arr[i])
    arr[i] = min(arr[i-1]+1, arr[i])

print(arr[x])