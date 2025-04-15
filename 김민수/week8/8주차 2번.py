# 8주차 2번

K, N = map(int, input().split())  # 가지고 있는 랜선 수, 필요한 랜선 수
lines = [int(input()) for _ in range(K)]  # 가지고 있는 각 랜선 길이

start = 1  # 자를 수 있는 최소 길이
end = max(lines)  # 자를 수 있는 최대 길이 (제일 긴 랜선 길이)
answer = 0

while start <= end:
    mid = (start + end) // 2  # 중간 길이로 잘라보기
    count = 0  # 랜선 개수 세기

    for line in lines:
        count += line // mid  # 각 랜선을 mid 길이로 자르면 몇 개 나오는지

    if count >= N:
        # mid 길이로 자르면 N개 이상 만들 수 있음 → 길이 늘려도 될지 확인
        answer = mid  # 일단 저장
        start = mid + 1
    else:
        # mid 길이로 자르면 N개 못 만듦 → 길이 줄여야 함
        end = mid - 1

print(answer)
