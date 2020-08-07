def is_prime(num):
    if num<=3:
        if num<=1:
            return False
        elif num==2 or 3:
            return True
    elif num%2==0:
        return False
    else:
        i=3
        while i<=(num+1)/2:
            remainder=num%i
            if remainder==0 and i!=num:
                return False
            elif (remainder!=0 and i==((num+1)/2)):
                return True
            i+=1

import threading
threading.Thread(target=is_prime,args=(479001599,)).start()
