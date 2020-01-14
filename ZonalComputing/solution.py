currentPosition=0
picked=0
NoOfStack,MaxHeight=list(map(int,input().split()))
stacks=list(map(int,input().split()))
instructions=list(map(int,input().split()))
for instru in instructions:
    if instru==1:
        if currentPosition!=0:
            currentPosition-=1
    elif instru==2:
        if currentPosition!=NoOfStack-1:
            currentPosition+=1
    elif instru==3:
        if picked==0 and stacks[currentPosition]!=0:
            stacks[currentPosition]-=1
            picked=1
    elif instru==4:
        if picked==1 and stacks[currentPosition]<MaxHeight:
            picked=0
            stacks[currentPosition]+=1
    elif instru==0:
        break
for i in stacks:
    print(i,end=" ")