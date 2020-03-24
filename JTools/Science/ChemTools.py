Table = open(__file__[:-12]+'ptable.txt','r').readlines()
from JTools import find_all, functionTimer, capaalfabet, numbers

'''
MAIN ChemTools file
'''

# add up the stragilers
def brotheradder(equ,values):
    newval = [] # the new values 
    values += [0] # this is so that it looks at the last line in the list safely
    point = find_all(equ,'+^')+[0] # this is so that it looks at the last line in the list safely
    nxt = 0 # current point inside values
    beside = None # if its beside any number or not / placement for it
    for a in range(len(point)-1):
        if (beside!=None) and (point[a+1]-point[a] == 2): # continuation for a tail
            newval[beside]+=values[nxt]
            nxt+=1
        elif (beside!=None): # end of a tail
            newval[beside]+=values[nxt]
            nxt+=1
            beside = None

        elif point[a+1]-point[a] == 2: # the value has a tail to another value
            beside = len(newval)
            newval.append(values[nxt])
            nxt+=1
        else:
            newval.append(values[nxt]) # the value is by itself and cant be reduced
            nxt+=1
            beside = None

    #cleanup
    while '+^+^' in equ:
        equ = equ.replace('+^+^','+^')

    return(equ,newval)


def bracketmult(equ,values):
    '''
    this section is insanely ugly im sorry
    '''
    # so it can see the final number in the list
    if equ[-1] != '=': 
        equ += '=='

    for _ in range(len(find_all(equ,'(+^)'))): # we know there are x times that this value shows up and we remove it so this is needed kinda.
        p = equ.index('(+^)') # get first time it shows up
        for a in range(p+4,len(equ)-1): # iterate through the equ
            if (equ[a] not in numbers): # find the ()
                #print(equ[p:a])
                values[find_all(equ,'+^').index(p+1)] *= int(equ[p+4:a]) # get the mult value 
                equ = equ.replace(equ[p:a],'+^') # Cleanup
                break 
    return(equ,values)
    

def calculateMoleculeMass(equ):
    '''
    Get the molecular mass of an equation
    calculateMoleculeMass('H2O') : gives 18.015
    BrK3 : gives 197.19799999999998
    (BrH2O(H3Br(HAu)3)2(H)4)3 : gives 4367.025
    (NaCl)20 : gives 1168.8

    YES I KNOW ITS MESSY ITS REALY KINDA HARD TO DO THIS WITH () BEING A THING
    '''
    equ = '('+equ+')1' # it is basicly to make the end result same as mult by 1 
    # get elements
    places = [] # locations and combos for Equations 
    place = None # starting point for an Element
    point = None # starting point for a number if there is one
    for a in range(len(equ)):
        if (equ[a] == ')') or (equ[a] == '('): 
            if place != None: # if there has been an Element at this point
                if point != None: # sometimes there isent a number after the element
                    places.append((place,a-1,point))
                else:
                    places.append((place,a-1,a))
                place = None
                point = None
        elif equ[a] in capaalfabet: # see if its an element
            if place != None:
                if point != None:
                    places.append((place,a-1,point))
                else:
                    places.append((place,a-1,a))
                place = a
                point = None
            else:
                place = a
                point = None
        elif equ[a] in numbers:
            point = a # a number is found
    

    # turn it into a string of numbers for ease of acsess kinda
    add = 0 # when you swap over to numbers more numbers get added
    values = [] # the values
    for p in places:
        for a in Table: # find the element
            a = a.split(' ')
            #print(equ[p[0]+add:p[2]+add])
            if a[1] == equ[p[0]+add:p[2]+add]: 
                if len(a) > 3:
                    num = float(a[3].replace('\n','')) # get the elements mass
                    if equ[p[2]+add:p[1]+1+add]!='': # get the multiply number if avalable
                        num *= float(equ[p[2]+add:p[1]+add+1])
                    values.append(num)
                    break
        
        point = len(equ[p[0]+add:p[1]+add+1]) # point is used to say how many leters are being overwritten
        equ = equ[:p[0]+add]+'+^'+equ[p[1]+add+1:]

        add += (2-point)



    # all the cleanup and math
    equ, newval = brotheradder(equ,values)
    while equ != '+^==':
        equ, newval = bracketmult(equ,newval)
        equ, newval = brotheradder(equ,newval)

    return(newval[0])



if __name__ == "__main__":
    equ = '(H2O)10(H3B)12'
    equ = '(BrH2O(H3Br(HAu)3)2(H)4)3'
    masses = ['H2O','BrK3','(BrH2O(H3Br(HAu)3)2(H)4)3','(NaCl)20']
    functionTimer()
    for equ in masses:
        print(equ)
        p = calculateMoleculeMass(equ)
        print(p)
    functionTimer()
     #Decahydrate 180.15