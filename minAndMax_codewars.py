def minimum(arr):
    minimum=arr[0]
    for i in range(0,len(arr)):
        if arr[i]<minimum:
            minimum=arr[i]
    return minimum

print(minimum([0,-1,-13,-5.7,3,1,2,3,4,5,-47]))

def maximum(arr):
    maximum=arr[0]
    for i in range(0,len(arr)):
        if arr[i]>maximum:
            maximum=arr[i]
    return maximum


print(maximum([0,-1,-13,-5.7,3,1,2,3,4,5,-47,48]))
