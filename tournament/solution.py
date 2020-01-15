teams=int(input())
strengths=list(map(int,input().split()))
strengths.sort(reverse=True)
sumStrngths=[]
sum=0
for i in strengths:
    sum+=i
    sumStrngths.append(sum)
j=1
revenue=0
while(j<teams):
    revenue+=sumStrngths[j-1]-strengths[j]*j
    j+=1
print(revenue)