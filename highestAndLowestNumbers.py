def high_and_low(numbers):
    numList=[]
    strList=list(numbers.split(' '))
    for i in strList:
        i=int(i)
        numList.append(i)
    maximum=max(numList)
    minimum=min(numList)
    return ("{} {}".format(maximum,minimum))

print(high_and_low('1 5 1 3 6'))
