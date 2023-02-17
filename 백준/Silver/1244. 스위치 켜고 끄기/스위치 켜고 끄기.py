# 스위치 켜고 끄기

def Man(arr, card):
    temp = card - 1
    while temp < len(arr):
        if arr[temp]:
            arr[temp] = 0
        else:
            arr[temp] = 1
        temp += card


def Woman(arr, card):
    start = card - 2
    end = card
    cnt = 0
    while start >= 0 and end < len(arr):
        if arr[start] == arr[end]:
            start -= 1
            end += 1
            cnt += 1
        else:
            break
    for i in range(card - 1 - cnt, card + cnt):
        if arr[i]:
            arr[i] = 0
        else:
            arr[i] = 1


switch = int(input())
arr = list(map(int, input().split()))
people = int(input())
i, line = 0, 20
for _ in range(people):
    gender, card = map(int, input().split())
    if gender == 1:
        Man(arr, card)
    else:
        Woman(arr, card)


while i < len(arr):
    print(arr[i], end=' ')
    i += 1
    if i == line:
        print()
        line+=20