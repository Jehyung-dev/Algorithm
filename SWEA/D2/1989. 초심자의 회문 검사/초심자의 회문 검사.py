# 초심자의 회문 검사

T = int(input())
for t in range(T):
    word = list(input())

    for i in range(len(word)//2):
        if word[i] != word[len(word)-1-i]:
            print(f'#{t + 1} 0')
            break
    else:
        print(f'#{t + 1} 1')
