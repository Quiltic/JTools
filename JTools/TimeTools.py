import time
times = {}


#
def functionTimer(name='a',prnt = True):
    '''
    Name is the name of the process, its literaly just there for orginization and being able to use it for more than one case
    prnt is if you want it to print something or not
        functionTimer('printtime')
        print('sup')
        functionTimer('printtime') : gives __ time : prints 'printtime finished in ___ seconds'
        functionTimer('time')
        print('sup')
        functionTimer('time', False) : gives __ time : prints Nothing
    '''
    global times 
    if name in times:
        t = time.time() - times[name]
        if prnt:
            print('{} finished in {} seconds'.format(name,t))
        del times[name]
        return(t)
    else:
        times[name] = time.time()


#
def timeDifrence(starttime,endtime):
    '''
    Gives the difrence between two times
    timeDifrence('900am','500pm') : gives 8
    timeDifrence('9am','5pm') : gives 8
    timeDifrence('9','5') : gives 8
    timeDifrence('830','4') : gives 7.5
    timeDifrence('9am','10am') : gives 1
    timeDifrence('9pm','10pm') : gives 1
    '''

    # if am or pm in stuff
    if 'am' in starttime:
        starttime = starttime.replace('am','') # remove it
        if len(starttime) < 3:# if it is just the hour ie 9 instead of 900
            starttime += '00'
        starttime = [int(starttime[:-2]),int(starttime[-2:])] # nothing needs to be changed

    elif 'pm' in starttime:
        starttime = starttime.replace('pm','') # remove it
        if len(starttime) < 3:# if it is just the hour ie 9 instead of 900
            starttime += '00'
        starttime = [int(starttime[:-2])+12,int(starttime[-2:])] # add 12 to the hours

    else:
        if len(starttime) < 3:# if it is just the hour ie 9 instead of 900
            starttime += '00'
        starttime = [int(starttime[:-2]),int(starttime[-2:])] # Splitup 



    if 'am' in endtime:
        endtime = endtime.replace('am','') # remove it
        if len(endtime) < 3:# if it is just the hour ie 9 instead of 900
            endtime += '00'
        endtime = [int(endtime[:-2]),int(endtime[-2:])]

    elif 'pm' in endtime:
        endtime = endtime.replace('pm','') # remove it
        if len(endtime) < 3:# if it is just the hour ie 9 instead of 900
            endtime += '00'
        endtime = [int(endtime[:-2])+12,int(endtime[-2:])] # add 12 to the hours

    else:
        if len(endtime) < 3:# if it is just the hour ie 9 instead of 900
            endtime += '00'
        endtime = [int(endtime[:-2]),int(endtime[-2:])] # Splitup 
        # if the endtime is smaller than the starttime its probably in the afternoon
        if (starttime[0] > endtime[0]):
            endtime[0] = int(endtime[0])+12


    
    # hours + minutes
    endtime = endtime[0]+endtime[1]/60
    starttime = starttime[0]+starttime[1]/60 
    return(endtime-starttime) # time difrence