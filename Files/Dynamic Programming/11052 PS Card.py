import sys
num = int(sys.stdin.readline())
price = [0] + list(map(int,sys.stdin.readline().split()))
dp = [0 for _ in range(num+1)]

for i in range(1,num+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i],dp[i-j]+price[j])
print(dp[num])