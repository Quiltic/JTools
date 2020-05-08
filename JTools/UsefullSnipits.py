capaalfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # capitals for use in knowing what is a element
loweralfabet = 'abcdefghijklmnopqrstuvwxyz' # lowers for use in knowing what is a element
alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
numbers = '1234567890' # numbers

# Use this for find_all
def find_all(string,find):
    '''
    Given a string this finds all FIND segments inside the string
    find_all('(H2O)10(H3B)12','(') : gives [0, 7]
    '''
    return(list(find_all_generator(string,find))) # makes it into a list insted of a generator


# mainbody for findall
def find_all_generator(a_str, sub):
    '''
    Yoinked and modifyed from https://stackoverflow.com/questions/4664850/how-to-find-all-occurrences-of-a-substring
    '''
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches


#
def braketsSplitter(equ):
    '''
    Given equ split it into an array which contains the location of the brackets
    (H2O(H3B)2)3 : gives [(4, 8), (0, 10)]
    '''
    out = [] # the ouputed list
    start = find_all(equ,'(')
    end = find_all(equ,')')
    pairs = [] # the list of pairs

    while len(start):
        # I do start[-1] because that should be the largest number
        # if i know the largest number i can find the smallest number in end which is stil greater than the start val
        # in thory this is its pair
        #print(start[-1],end) 
        for a in range(len(end)): # iterate through all the elements in the end bar
            if start[-1] < end[a]: # if the element is greater then its this pair
                pairs.append((start[-1],end[a]))
                del end[a] # removes the element from the list
                del start[-1] # removes the element from the list
                break # no need to iterate further
        
    return(pairs)


#
def flattenList(lst):
    '''
    Given lst flatten it into one array
    flattenList([12,[4,3],[[1,2],1]]) : gives [12, 4, 3, 1, 2, 1]
    '''
    out = []
    for a in lst:
        if type(a) == list:
            out += flattenList(a)
        else:
            out.append(a)
    return(out)


#
def cutUpString(string, lst):
    '''
    Givin a string cut it up at locations in lst
    cutUp('hi',[1]) : gives ['h','i']
    '''
    lst = [0] + lst + [len(string)] # to get the begining and end
    new = [string[lst[a-1]:lst[a]] for a in range(1,len(lst))] # split it up

    if new[0] == '': # when the first val of lst was also a 0 (lst origin == [0,3] then it would be [0,0,...])
        new = new[1:] # remove '' made by this

    if new[-1] == '': # when the last val of lst was also a max len (lst origin == [0,3] then it would be [...,3,3])
        new = new[:-1] # remove '' made by this

    return(new)