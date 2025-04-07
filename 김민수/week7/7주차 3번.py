# 7주차 3번

text = input()

def reverse_words_with_tags(text):
    result = []
    word = ''
    inside_tag = False

    for ch in text:
        if ch == '<':
            # 단어가 있다면 먼저 뒤집어서 결과에 추가
            if word:
                result.append(word[::-1])
                word = ''
            inside_tag = True
            result.append(ch)
        elif ch == '>':
            inside_tag = False
            result.append(ch)
        elif inside_tag:
            result.append(ch)
        elif ch == ' ':
            if word:
                result.append(word[::-1])  # 단어 뒤집어서 추가
                word = ''
            result.append(' ')  # 공백 그대로 유지
        else:
            word += ch  # 단어 계속 쌓기

    # 마지막에 남은 단어 처리
    if word:
        result.append(word[::-1])

    return ''.join(result)

print(reverse_words_with_tags(text))

