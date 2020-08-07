#As a general rule, python cannot convert special characters like '$' to float. The following code converts strings containing the '$' character to float by converting '$' to None.

str_to_float=['2.1','2.3','7.5','$12.12','^^8.9','%5','33.1']


floatConvert=[]      #creating empty list to contain the newly converted float
bad_characters=',$%^&*()!@'
for number in str_to_float:
    corrupted=False
    for bad_character in bad_characters:
        if bad_character in number:
            corrupted=True
    if corrupted:
        floatConvert.append(None)
    else:
        floatConvert.append(float(number))
print(floatConvert)
