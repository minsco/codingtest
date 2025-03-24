# 코딩테스트 스터디

## 1주차
1. [큐2](https://www.acmicpc.net/problem/18258)
2. [스택](https://www.acmicpc.net/problem/10828)
3. [괄호](https://www.acmicpc.net/problem/9012)
4. [요세푸스 문제](https://www.acmicpc.net/problem/1158)
5. [카드 2](https://www.acmicpc.net/problem/2164)

## 2주차
1. [큰 수 구성하기](https://www.acmicpc.net/problem/18511)
2. [번데기](https://www.acmicpc.net/problem/15721)
3. [한윤정이 이탈리아에 가서 아이스크림을 사먹는데 ](https://www.acmicpc.net/problem/2422)
4. [DNA](https://www.acmicpc.net/problem/1969)
5. [카드 놓기](https://www.acmicpc.net/problem/5568)

## 3주차 

1. [거스름돈](https://www.acmicpc.net/problem/14916)
2. [로프](https://www.acmicpc.net/problem/2217)
3. [ATM](https://www.acmicpc.net/problem/11399)
4. [동전0](https://www.acmicpc.net/problem/11047)
5. [A->B](https://www.acmicpc.net/problem/16953)

```mermaid
flowchart TD
    사용자[사용자 CSV 파일 업로드]
    main_py_save[main.py: CSV 파일 저장]
    main_py_load[main.py: CSV 데이터 로딩 \(Pandas\)]
    subgraph "모델 예측 과정"
        weight_model[weight_used_model.py process()<br/>기존 학습된 LSTM 모델 로딩 및 예측 수행]
        weight_results[예측 결과 이미지 생성<br/>RMSE 계산]
        dynamic_model[model.py process()<br/>동적 로딩을 통한 모델 로딩 및 예측 수행]
        dynamic_results[예측 결과 이미지 생성<br/>RMSE 계산]

        weight_model --> weight_results
        dynamic_model --> dynamic_results
    end
    encoding[main.py: 결과 이미지 Base64 인코딩]
    json_return[main.py: JSON 형태로 결과 반환]
    사용자확인[사용자가 결과 이미지 및 RMSE 확인]

    사용자 --> main_py_save --> main_py_load
    main_py_load --> weight_model
    weight_results --> dynamic_model
    dynamic_results --> encoding --> json_return --> 사용자확인
```

