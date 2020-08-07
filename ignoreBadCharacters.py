#As a general rule, python cannot convert special characters like '$' to float. The following code converts strings containing the '$' character to float by converting '$' to None.

str_to_float=['2.1','2.3','7.5','$12.12','^^8.9','%5','33.1']   #list containing strings that need to converted to float


floatConvert=[]      #creating empty list to contain the newly converted float
bad_characters=['$','^','%']    #list of bad characters
for number in str_to_float:     #looping through list str_to_float
    corrupted=False             #setting default value of corrupted to False
    for bad_character in bad_characters:    #checking for each character in bad_characters
        if bad_character in number:         #checking if charater present in string 'number'
            corrupted=True      #setting corrupted to True if a bad character is present
    if corrupted==True:         #appending NoneType for bad character
        floatConvert.append(None)
    else:                       #number converted to float and appended to the list    
        floatConvert.append(float(number))

print(floatConvert) #printing new created floatConvert list
