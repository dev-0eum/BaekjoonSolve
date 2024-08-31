import sys
cnt = int(sys.stdin.readline())

for _ in range(cnt):
    line = sys.stdin.readline()
    correct = 0
    flag = 0
    #make token array
    token = []
    for x in range(len(line.strip())):
        token.append(line[x])

# ( = +1 
# ) = -1
# 단, 음수로 내려가면 안됨.

    #lexical analyze
    for x in token:
        if(x=="("):
            correct += 1
        elif(x==")"):
            correct -= 1
        
        if(correct<0):
            print("NO")
            flag = 1
            break

    if(correct == 0):
        print("YES")
    elif (correct != 0 and flag != 1):
        print("NO")
        
    #init token array
    token = []
    correct = 0
    flag = 0