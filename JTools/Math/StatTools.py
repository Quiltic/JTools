import math

def option_adder(num):
    '''
    Takes a number and removes 1 then at end adds all together
    option_adder(num)
    option_adder(4) : gives 10 (4+3+2+1+0)
    '''
    if num == 0:
        return(num)
    return(num+option_adder(num-1))

def number_of_combinations(startingNum, segments = 2, includeSelf = True):
    # doesent WORK PAST 2 SEGMENTS!
    '''
    Gives the number of posable combonations givin some things
    number_of_combinations(startingNum, segments = 2, includeSelf = True)
    number_of_combinations(4) : gives 10 : idea ([a,b,c,d] = [aa,ab,ac,ad,bb,bc,bd,cc,cd,dd])
    number_of_combinations(4,3) : gives 36 ([a,b,c,d] = [aaa,aab,aac,aad,aba,abb,abc,abd...])
    number_of_combinations(4,2,False) : gives 6
    '''
    newnum = int(startingNum) # keep starting num
    if not includeSelf:
        startingNum -= 1

    startingNum = startingNum**(segments-1)
    
    return(option_adder(startingNum)/2)


def posabilitys(lst, segments = 2, orderMatters = True , includeSelf = True):
    '''
    combines lists
    '''
    newlst = list(lst)
    for _ in range(segments-1):
        for a in list(newlst):
            newerList = []
            for b in lst:
                if a+b not in newlst:
                    if (b+a in newlst) and (not orderMatters): # basicly if order doesent matter (ab == ba)
                        pass#newerList.append(a+b)
                    else: # basicly if order matters (ab != ba)
                        newerList.append(a+b) 
            newlst += newerList

    return(newlst)


if __name__ == "__main__":
    num = 4
    freinds = 3
    print(number_of_combinations(num,freinds))
    print(posabilitys(['a','b','c','d'],freinds))
    print(len(posabilitys(['a','b','c','d'],freinds)))

    print(((num*4)-1)*4)