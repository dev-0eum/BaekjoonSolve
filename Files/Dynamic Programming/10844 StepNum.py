import sys

memo=[0 for _ in range(1000)]

def answer(n):
    global memo
    temp=[]
    # n은 자릿수
    if n==1:
        memo = [x for x in range(10**n)] #10**n = 10
    else:
        plus = 0
        minus = 0

    for i in memo:
        if i/10**n != 0:
            pass

    temp = [x for x in range(10**n)]

    return temp

print(answer(int(sys.stdin.readline())))
print(10**0)

'''
N = int(input())

dp = [[0]*10 for _ in range(N+1)]
for i in range(1, 10):
    dp[1][i] = 1

MOD = 1000000000

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] 

print(sum(dp[N]) % MOD)
'''