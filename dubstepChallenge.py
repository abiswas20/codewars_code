dubstepLyrics='WUBAWUBBWUBCWUB'

def song_decoder(song):
    strList=''  #starting out with empty list
    for i in range(len(song)): #going through the entire string
        strList=strList+str(song[i]) #adding one character at a time
        if len(strList)>=3:     #start checking only when length of strList is >3 because 'WUB' is 3 characters long
            if strList[-3:]=='WUB':         #checking if the last 3 characters make up 'WUB'
                strList=strList[:-3]        #deleting 'WUB' from the end if the last 3 characters are truly 'WUB'
                if strList[-1:]!=' ' and i<len(song): #adding space between words as long as there isn't a space from before
                    strList=strList+' '     
                    if strList[0]==' ':  #if 1st character is ' ' remove it
                        strList=strList[1:]
    if strList[-1:]==' ':   #if the last character is ' ' remove it
        strList=strList[:-1]
            
    return strList  #return cleaned string





print(song_decoder(dubstepLyrics))
