import sys
word = sys.stdin.readline()

answer = [0 for _ in range(26)]
for x in word:
    num = ord(x)
    num -= 97
    answer[num] += 1

ans = ''
for x in answer:
    ans += str(x) + " "
print(ans.rstrip())