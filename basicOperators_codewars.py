def basic_op(operator, value1, value2):
    if operator=='+':
        return(value1+value2)
    elif operator=='-':
        return(value1-value2)
    elif operator=='*':
        return(value1*value2)
    elif operator=='/':
        return(value1/value2)
    else:
        print('not a valid operator')

print(basic_op('/',5,3))
print(basic_op('v',5,3))
