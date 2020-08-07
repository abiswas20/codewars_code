def even_or_odd(number):
    if type(number)!=int:
        return "Not an integer. Abort"
    else:
        if number%2==0:
            return "Even"
        elif number%2!=0:
            return "Odd"


x=even_or_odd(1)
y=even_or_odd(8)
z=even_or_odd(65.7)
print(x)
print(y)
print(z)
