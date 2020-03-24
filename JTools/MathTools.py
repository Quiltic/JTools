
def average(data):
    '''
    Literaly just gets the average of whatever list you put inside this
    average([1,2,3,4]) : gives 2.5
    average([[1,2,3],[1,2,3,4]]) : gives [2,2.5]
    '''
    try: 
        if (type(data[0]) == list) or (type(data[0]) == tuple): # get data for lists inside this one
            out = [average(d) for d in data] # averaged list of lists
            return(out) 
        else: # no lists
            return(sum(data)/len(data)) # typical average equation
    except:
        return(None) # some failure happened usualy because the list is 0 long


def fraction_finder(num, aprox = 20):
    '''
    Given a float it will give you a the 2 smallest numbers needed to get the float if divided 
    top, bottom = fraction_finder(0.0335) : gives 67, 2000
    top, bottom = fraction_finder(0.0335,6) : gives 5, 149
    aprox is how acurate you want it to be, for instance fraction_finder(0.0335,6) gives 5/149 (0.33557...) but the exact number is 67/2000 
        20 is aprox's default number
    '''
    top = 1 # top number
    bottom = 1 # bottom number
    for a in range(10000): # dont like while loops for this
        result = float(top/bottom) # quick way to look at end result
        if str(result)[:aprox] == str(num)[:aprox]: # compare the result with what is wanted with aprox
            return(top,bottom) # got it
        if (result < num): # number too low
            top += 1
        else: # too high
            bottom += 1
    return(top,bottom) # Closest it came typicly never gets here
