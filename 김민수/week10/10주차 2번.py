# 10주차 2번

N = int(input())
M = int(input())
K = list(map(int, input().split()))

K.sort()  

start = 0
end = N - 1
count = 0

while start < end:
    temp = K[start] + K[end]
    
    if temp == M:
        count += 1
        start += 1
        end -= 1
    elif temp < M:
        start += 1
    else:   
        end -= 1

print(count)
