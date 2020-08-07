def sum_two_smallest_numbers(numbers):
    for i in range(len(numbers)):
        if numbers[i]<0 or type(numbers[i])==float:
            return "floats or non-positive integers not allowed."
        i+=0
    if len(numbers)>=4:
        sortedList=sorted(numbers)
        val=sortedList[0]+sortedList[1]
        return val
    else:
        return "list needs to have atleast 4 elements"

numList=[11,2,7,43,2,9,1]
print(sum_two_smallest_numbers(numList))

numList1=[11,2,7]
print(sum_two_smallest_numbers(numList1))

numList2=[11,2,7,-2,-1]
print(sum_two_smallest_numbers(numList2))
