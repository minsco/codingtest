# 10주차 5번

N = int(input())
L = list(map(int, input().split()))
L.sort()  

start = 0
end = N - 1
min = 2000000001
left = right = 0

while start < end:
    temp = L[start] + L[end]
    
    if abs(temp) < min:
        min = abs(temp)
        left, right = L[start], L[end]
    
    if temp < 0:
        start += 1
    else:
        end -= 1 

print(left, right)

    

    
    

