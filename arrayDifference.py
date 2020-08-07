#This is a code for a difference function that subtracts one list from another and return the result.#

def array_diff(a,b):
    """This function subtracts one list from another and return the result."""
    c=set(b)    #creates set from list b to boil it down to unique elements
    l=len(a)    #we need to go over each element of list a
    i=0     #setting counter i to 0
    while i<len(a):     #looping through the entire list
        if a[i] in c:   #checking is ith element in list b is in set c
            a.pop(i)    #popping ith element of a if it is indeed in set c
            i=i-1       #lowering i by 1 so the i+1th element in the original list a doesn't get overlooked
        i+=1            #general counter for while loop
            
    return a            #return modified list a at the end of the function


##Tes##
f=[1,3,2,2,4,5,1,8]
g=[2,1]
print(array_diff(f,g))
