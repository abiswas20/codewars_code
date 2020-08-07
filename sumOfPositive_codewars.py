def positive_sum(arr):
    sum=0
    for element in arr:
        if element>0:
            sum+=element
    return sum


print(positive_sum([3,2,1,0,-4,-5]))
