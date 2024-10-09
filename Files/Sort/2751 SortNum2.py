import sys

N = int(sys.stdin.readline())
num=[]
ans=[]
cur=0
for _ in range(N):
    num.append(int(sys.stdin.readline()))

for i in range(N):
    min_= num[i]
    for j in range(i+1, N):
        if(num[i]>num[j]):
            min_=num[j]
            temp = num[i]
            num[i] = num[j]
            num[j] = temp
    ans.append(min_)
#num.sort()
for x in ans:
    print(x)