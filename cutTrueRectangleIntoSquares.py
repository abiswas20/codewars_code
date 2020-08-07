## This function divides the rectangle into fewest number of squares.

def sqInRect(lng,wdth):
    if lng==wdth:
        return None
    else:
        dimensions=[]
        area=lng*wdth
        intSqRoot=int((area)**0.5)
        rectSide=sorted(range(1,intSqRoot+1),reverse=True)
        for sqSide in rectSide:
            while area>=sqSide**2:
                dimensions.append(sqSide)
                area-=sqSide**2
        return dimensions

print(sqInRect(5,3))
