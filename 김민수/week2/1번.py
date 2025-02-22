#2주차 1번

N, K = map(int, input().split())  # N과 K 입력 받기
digits = list(map(int, input().split()))  # 사용할 숫자 리스트

digits.sort(reverse=True)  # 큰 숫자부터 정렬

N = str(N)  # N을 문자열로 변환
result = 0  # 최종 결과 값 저장

# N과 같은 자리수부터 점점 줄여가며 탐색
for length in range(len(N), 0, -1):
    from itertools import product  # 중복 순열을 위한 라이브러리 사용
    
    # 가능한 숫자 조합을 생성
    for num_tuple in product(digits, repeat=length):
        num = int("".join(map(str, num_tuple)))  # 숫자 리스트를 정수로 변환
        if num <= int(N):  # N 이하인 가장 큰 수 찾기
            result = max(result, num)

print(result)  # 결과 출력