N,K = map(int,input().split())
def kitai(num):
    return (1+int(num)/2)
P = list(map(kitai,input().split()))	  

S = [0]*(N+1)
ans = 0
for i in range(N):
    S[i+1]=S[i]+P[i]
for i in range(N-K+1):
    ans = max(ans,S[i+K]-S[i])
print(S[i])

