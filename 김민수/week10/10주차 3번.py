from collections import Counter

N, X = map(int, input().split())
V = list(map(int, input().split()))

sum_V = sum(V[:X])
results = [sum_V]

for i in range(X, N):
    sum_V += V[i] - V[i - X]
    results.append(sum_V)

max_V = max(results)

if max_V == 0:
    print("SAD")
else:
    print(max_V)
    count = Counter(results)
    print(count[max_V])
