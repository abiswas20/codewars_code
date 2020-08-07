#This is a code for a difference function that subtracts one list from another and return the result.#

def array_diff(a,b):
    """This function subtracts one list from another and return the result."""
    c=set(b)
    l=len(a)
    i=0
    while i<len(a):
        if a[i] in c:
            print(i)
            a.pop(i)
            i=i-1
        i+=1
            
    return a


##Tes##
f=[1,3,2,2,4,5,1,8]
g=[2,1]
print(array_diff(f,g))
