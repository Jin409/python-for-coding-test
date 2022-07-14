n = int(input())

# 00시 00분 00초 ~ n시 59분 59초까지

'''

'''

three_in_seconds = 10 + 5
three_in_minutes = three_in_seconds * 60 * 2 - three_in_seconds # 3이 초에 포함돼서 모든 분이 가능할 때 + 초에는 포함 안되는데 분에 포함될 때 - 둘이 겹치는 경우
print(three_in_minutes * (n+1))