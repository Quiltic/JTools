capaalfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # capitals for use in knowing what is a element
loweralfabet = 'abcdefghijklmnopqrstuvwxyz' # lowers for use in knowing what is a element
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
numbers = '1234567890' # numbers


""" This is to know if I am on the pi or laptop """
from sys import platform
if platform == "linux" or platform == "linux2":
    # linux
    #print('Using Linux')
    FilesType = '//'
elif platform == "darwin":
    # OS X
    # OS! OS! WHAT THE HELL!
    #print('OS! OS! WHAT!?')
    pass
elif platform == "win32":
    # Windows
    #print('Using Windows')
    FilesType = '\\'



import pathlib
place = pathlib.Path(__file__).parent.absolute()


# this is a faster way to use the dictionary
dictionary = {}
for a in open(f'{place}{FilesType}DictionaryLines.txt','r').readlines(): # main list
    lst = a.split(':!!:') # achual stuffs
    if len(lst) > 1:
        dictionary[lst[0]] = [lst[1],lst[2][:-1]] # this overrights iself alot 
#dictionary = Load('Dictionary')



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


def spell_check_helper(word):
    ''' 
    This is used to help the achual spell check. 
    Gives a list of posable words that could be the word.
    Shamelessy stolen from http://norvig.com/spell-correct.html
    '''
    splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes    = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
    replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
    inserts    = [a + c + b     for a, b in splits for c in alphabet]
    return set(deletes + transposes + replaces + inserts)



def spellCheck(word, dictionary = dictionary):
    '''
    This is used to give the spell checked word.
    Literaly a spell checker
    '''
    #stuff = spell_check_helper(word)
    for pos in spell_check_helper(word):
        try:
            dictionary[pos.capitalize()] # we have a match
            return(pos.lower())
        except:
            pass