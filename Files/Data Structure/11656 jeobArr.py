word = input()
words = []

cnt = 0
while cnt != len(word):
    words.append(word[cnt:])
    cnt += 1

words.sort()
for x in words:
    print(x)