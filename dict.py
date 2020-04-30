N=int(input())
l={}
ans =[]
 
"""for i in range(N):
  s=input()
  if s in l:
    l[s]+=1
  else:
    l[s]=1
print(l)"""
for i in range(N):
    s=input()
    if s in l:
        l[s]+=1
    else:
        l[s]=1
#print(l)
max = max(l.values())
print(max)
for i in l:
    #print(l[i])
    if l[i]==max:
      ans.append(i)
b = sorted(ans)
for i in b:
    print(i)

