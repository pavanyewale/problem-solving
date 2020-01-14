n,k=list(map(int,input().split()))
sequence=list(map(int,input().split()))
sequence.sort()
pair_count=0
i=0
j=1
while(j<n):
    if sequence[j]-sequence[i]>=k:
        pair_count+=n-j
        i+=1
    else:
        j+=1
print(pair_count)