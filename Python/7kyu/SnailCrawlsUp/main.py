def snail(column, day, night):
    i = 1
    height = 0
    while column >= height:
        height +=day
        
        if column <= height:
            return i
        else:
            height -=night            
        i+=1
        
    return i
    