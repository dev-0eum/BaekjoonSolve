word = input()

a = 97
answer = [-1 for _ in range(26)]
ans = ''

for x in enumerate(word):
    # x[0] = index / x[1] = alphabet
    num = ord(x[1]) #ASCII num
    if(answer[num - a] == -1):
        answer[num - a] = x[0]

for x in answer:
    ans += str(x) + " "
print(ans)