# 초심자의 회문 검사

T = int(input())
for t in range(T):
    word = list(input())
    reversed_word = [0]*len(word)
    for i in range(len(word)):
        reversed_word[i] = word[len(word)-1-i]

    if word == reversed_word:
        print(f'#{t+1} 1')
    else:
        print(f'#{t + 1} 0')
