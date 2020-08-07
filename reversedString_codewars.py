def solution(string):
    newString=''
    for i in range(1,len(string)+1):
        newString=newString+string[-i]
#        print(newString)
    return newString


print(solution('hello world'))
    
