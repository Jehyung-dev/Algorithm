# 초심자의 회문 검사

T = int(input())
for t in range(T):
    word = input()
    result = 1
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - 1 - i]:
            result = 0
            break

    print(f'#{t + 1} {result}')
