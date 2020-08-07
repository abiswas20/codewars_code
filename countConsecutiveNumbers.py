def pairs(ar):
    i=0
    count=0
    for i in range(int(len(ar)/2)):     #each pair starts with an even index
        if abs(ar[2*i]-ar[2*i+1])==1:   #direction agnostic
            count+=1
    return count


numList=[1,2,3,5,6,7,8,8,9,10]
print(pairs(numList))
