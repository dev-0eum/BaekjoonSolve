import sys
# run time error
'''
import sys
getStr = sys.stdin.readline()
cnt = int(sys.stdin.readline())
string = []
answer = ''
for x in range(len(getStr)):
    string.append(getStr[x])

string.remove("\n")
string.append("")
cursor = len(getStr) -1
for _ in range(cnt):
    line = sys.stdin.readline()
    cmd = line.split()
    
    # print(cursor)
    # print("GET", cmd[0])
    if(cmd[0]=='L'):
        if(cursor > 0):
            cursor -= 1
    elif(cmd[0]=='D'):
        if(cursor < len(string)-1): # 맨 뒤가 아닐 때
            cursor += 1
    elif(cmd[0]=='B'):
        if(cursor > 0 and cursor <= len(string)-1):
            cursor -= 1
            del string[cursor]
    elif(cmd[0]=='P'):
        string.insert(cursor, cmd[1])
        if(cursor < len(string)-1):
            cursor += 1

answer = ''.join(string)
print(answer.strip())
'''
# 타인의 풀이 [Stack 활용]
import sys
st1 = list(sys.stdin.readline().rstrip())
st2 = []

for _ in range(int(sys.stdin.readline())):
	cmd = list(sys.stdin.readline().split())
	if cmd[0] == 'L':
		if st1:
			st2.append(st1.pop())
	elif cmd[0]=='D':
		if st2:
			st1.append(st2.pop())
	elif cmd[0]=='B':
		if st1:
			st1.pop()
	else:
		st1.append(cmd[1])
		
st1.extend(reversed(st2))
print(''.join(st1))