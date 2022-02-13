'''
while len(word) < len(text):
    if text[0:len(word)] == word:
        cnt += 1
        for i in text:
            a = list(i)
        for j in word:
            b = list(j)
        c = a - b
        text = map(str, c)

        실패...
'''

text = input()
word = input()
cnt = 0
i = 0
while len(text) - len(word) >= i:
    if text[i:i+len(word)] == word:
        cnt += 1
        i += len(word)  # 단어의 길이만큼 인덱스에 더해주기 -> 해당 부분 이후부터 if문 수행
    else:
        i += 1 # 찾지 못하면 1만큼 인덱스를 더하고 다시 if문 수행

print(cnt)
