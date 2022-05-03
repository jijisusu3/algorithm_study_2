def solution(n, k):
    word = ''
    while n:
        word = str(n % k) + word
        n = n // k

    word = word.split("0")

    cnt = 0
    breaker = True  # 플래그이자 소수인지 확인하는 것,
    for i in word:
        if len(i) == 0: continue

        num = int(i)

        if num == 1: continue

        for j in range(2, int(num**0.5)+1):
            if num % j == 0:
                breaker = False
                break

        if breaker:
            cnt += 1

    return cnt


print(solution(110011, 10))
