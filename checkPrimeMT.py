import threading
def primeList(upperLimit):
    num=6
    primeList=[]
    while num<upperLimit:
        i=2
        j=2
        while j<((num/2)):  
            while i<((num/2)):
                remainder=num%i
                if remainder>0 and i>((num/2)-1):
                    primeList.append(num)
                    primeCount=len(primeList)
                    print(primeList)
                elif remainder==0:
                    num=num+1
                    i=1
                else:
                    num=num
                i+=1
            j+=1
        num+=1


            
                
    print(primeList,primeCount)
        

threading.Thread(target=primeList,args=(100000,)).start()
#primeList(10000)
#f=open('primeCalc.txt','a')
#f.write(primeList(7900))
#f.close()
