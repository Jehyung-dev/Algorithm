# 쿼드트리


def Check(r, c, n):  # 같은지 비교하는 함수
    global ans  # 결과를 글로벌로 지정

    point = arr[r][c]  # 행열의 처음 값을 비교 값으로 설정
    error = 0  # 행열의 값이 다른 경우를 찾기 위한 플래그 변수
    half = n // 2  # n의 절반 값

    if n > 1:  # n이 1보다 큰 경우
        for i in range(n):  # 행열의 값이 같은지 확인
            for j in range(n):
                if arr[r + i][c + j] != point:
                    error = 1  # 다른 경우 에러를 표시하고 반복을 빠져나옴
                    break
        if not error:  # 행열의 값이 같은 경우
            ans += str(point)  # 값 추가
        else:  # 같지 않은 경우
            ans += "("  # 4부분으로 나누기 전 괄호 설정
            Check(r, c, half)  # 재귀
            Check(r, c + half, half)
            Check(r + half, c, half)
            Check(r + half, c + half, half)
            ans += ")"

    else:  # n이 1인 경우
        ans += str(point)  # 해당 값을 더함


N = int(input())  # 영상의 크기
arr = [list(map(int, input())) for _ in range(N)]  # 문자열을 2차원 int 리스트로 저장
ans = ""

Check(0, 0, N)
print(ans)
