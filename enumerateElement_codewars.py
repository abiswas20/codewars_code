haystack=['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk']
def find_needle(arr):
    for index,element in enumerate(arr):
        if element=='needle':
            return ("found the needle at position {}".format(index))

print(find_needle(haystack))
