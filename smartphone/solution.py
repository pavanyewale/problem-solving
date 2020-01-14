n=int(input())
budgets=[]
for _ in range(n):
    budgets.append(int(input()))
budgets.sort()
ans=0
for i in range(n):
    k=(n-i)*budgets[i]
    if ans<k:
        ans=k
print(ans)
