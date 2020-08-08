def int32_to_zip(int32):
    """Complete the function that takes an unsigned 32 bit number and returns a string representation of its IPv4 address"""
    ipv4_str="" 
    ipv4_bin=""
    ipv4_list=[]
    ipv4=""
    ####algorith to convert decimal to binary. divide by 2 and enter 0 if remainder is 0 else 1. reverse string to get binary representation.####
    while int32!=0:
        if int32%2==0:
            ipv4_str=ipv4_str+'0'
        else:
            ipv4_str=ipv4_str+'1'
        int32=int32//2      #floor division
    ipv4_bin=ipv4_str[::-1] #reversing string
    if len(ipv4_bin)<32:   #convert unsigned binary to signed binary
        while len(ipv4_bin)<32:
            ipv4_bin='0'+ipv4_bin
    print('ipv4_bin',ipv4_bin)

###Take chunks of 8 bits and convert to decimal###
    octets=[]   #list to contain octets
    for i in range(0,4):
        octets.append(ipv4_bin[8*i:8*i+8])
    #return octets
###Convert octets to decimal and put a period in between###
    for i in octets: #going through all the octets in the list
        j=0
        x=0
        while j<len(i): #going through each digit in an octet
            x=x+int(i[-(j+1)])*(2**j) #converting binary to decimal by multiplying by power of 2. going from right to left.
            if (j-7)%8==0: #append to list only when an octet is completely deciphered
                ipv4_list.append(x)
            j+=1
###Convert ipv4 given as a list to conventional form with periods###
    for k in ipv4_list:
        ipv4=ipv4+'.'+str(k)
    ipv4=ipv4[1::]  #removing the period in the front of the first number

    return ipv4


print(int32_to_zip(0))
