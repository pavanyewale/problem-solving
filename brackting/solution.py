n=int(input())
brackets=list(map(int,input().split()))
brack=0
position=0
lastMax=0
maxSequenceStart=1
maxSequence=0
currentCount=0
currentStart=1
for b in range(n):
    currentCount+=1
    if brackets[b]==1:
        brack+=1
        if brack>lastMax:
            position=b+1
            lastMax=brack
    else:
        brack-=1
        if brack==0:
            if currentCount>maxSequence:
                maxSequence=currentCount
                maxSequenceStart=currentStart
            currentStart=b+2
            currentCount=0
                
print(lastMax,end=" ")
print(position,end=" ")
print(maxSequence,end=" ")
print(maxSequenceStart)