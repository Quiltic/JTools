# made posable by https://pymotw.com/2/xml/etree/ElementTree/create.html

#import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment, ElementTree, tostring, parse
from xml.dom import minidom
import os


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Save eather a list or a dic
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# Makes it look goood : helper for Save
def prettify(elem):
    """
    Return a pretty-printed XML string for the Element.
    """
    rough_string = tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="    ")


# turns it into usable xml stuffs : helper for Save
def CompressList(lst):
    '''
    Makes a list into a thing of xml elements for use of saving to a file
    '''
    child = Element('list') # base thing to state that the folowing is a list
    liststuff = [] 
    for a in lst: 
        if type(a) == dict: # makes a new compression for this type
            liststuff.append(CompressDict(a))
        elif type(a) != list:
            liststuff.append(Element(str(type(a)).replace("<class '",'').replace("'>",''), val=str(a))) # Basicly this just gets the type for its name and makes an element with it
        else: # makes a new compression for this type
            liststuff.append(CompressList(a))
    child.extend(liststuff) # adds the list to the base thing

    return(child)


# turns it into usable xml stuffs : helper for Save
def CompressDict(dic):
    '''
    Makes a dict into a thing of xml elements for use of saving to a file
    '''
    top = Element('dict') # base thing to state that the folowing is a list
    #comment = Comment('Generated for PyMOTW')
    #top.append(comment)

    for part in dic:
        #print(part)
        if type(dic[part]) == list: # makes a new compression for this type
            child = SubElement(top, 'list', name = part)
            child.extend(CompressList(dic[part]))
        elif type(dic[part]) != dict:
            child = SubElement(top, str(type(dic[part])).replace("<class '",'').replace("'>",''), name = part,  val = str(dic[part])) # Basicly this just gets the type for its name and makes an element with it
        else: # makes a new compression for this type
            child = SubElement(top, 'dict', name = part)
            child.extend(CompressDict(dic[part]))

    return(top)


# main for saving
def Save(name,data):
    '''
    Saves a dict/list to a file called name
    Save('hello',{'Stuff': [1,2,3]}) : gives None : Makes hello.xml
    '''
    F = open('{}.xml'.format(name),'w+')
    if type(data) == dict: # starts with a dict for ease
        F.write(prettify(CompressDict(data)))
    elif type(data) == list: # starts with a dict for ease
        F.write(prettify(CompressList(data)))
    F.close() # save
#'''


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Load eather a list or a dic
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# preps an xml file to be turned into a dict or list : helper for Load
def LoadXML(NAME):
    """
    >>> f = openXMLFiles(".\\Testfiles\\patch.xml")
    >>> type(f)
    <class 'xml.etree.ElementTree.Element'>
    """
    '''
    Loads an xml file to be turned into a dict or list
    '''
    # Basics snaged from https://docs.python.org/2/library/xml.etree.elementtree.html
    Tree = parse(NAME) # opens and turns the xml file into a tree
    Root = Tree.getroot()
    return(Root)


# gets type foe multi use : helper for Load
def typer(tipe,data):
    '''
    Main body for the load function
    '''
    if tipe == 'int': # make into int
        return(int(data.attrib['val']))
    elif tipe == 'float': # make into float
        return(float(data.attrib['val']))
    elif tipe == 'bool': # make into bool
        if (data.attrib['val'] == 'False') or (data.attrib['val'] == '0'):
            return(False)
        else:
            return(True) 
    #elif a.tag == 'char':
    #    returnDict[a.attrib['name']] = char(a.attrib['val'])
    elif tipe == 'list': # make into list
        return(DecompressList(data))
    elif tipe == 'dict': # make into dict
        return(DecompressDict(data))
    else: # make into string
        return(data.attrib['val'])


# makes a list from data : helper for Load
def DecompressList(tree):
    '''
    Loads an xml segment to be turned into a list
    '''
    """
    returnList = []
    for a in tree:
        returnList.append(typer(a.tag,a))
    """

    returnList = [typer(a.tag,a) for a in tree] # yep
    return(returnList)


# makes a dict from data : helper for Load
def DecompressDict(tree):
    '''
    Loads an xml segment to be turned into a dict
    '''
    returnDict = {}
    for a in tree:
        returnDict[a.attrib['name']] = typer(a.tag,a)
        

    return(returnDict)

# Load data
def Load(fileName):
    '''
    Loads an xml file to be turned into a dict or list
    d = Load('hello') : gives {'Stuff': [1,2,3]} : requires file made by Save()
    '''
    fileName = fileName+'.xml'
    xml = LoadXML(fileName)
    if xml.tag == 'list': # load proper type
        return(DecompressList(xml))
    else:
        return(DecompressDict(xml))


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Get a listing of files/subfolders
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


#
class File:
    '''
    Basicly this gives info about folders and files.
    Both - Path(given to it), name, type (FOLDER if its a folder)
    Folders - dirs (folders), files, filepaths (for files), allfilepaths (all filepaths for all files inside of this folder & subfolders), 
            - subdir (all folders inside of this one), contents (strings with paths of surface files/folders), data (class File versions of contents) 
    Files - data (raw data from open(path, 'r')), contents (data.read())

    File('C:\\users\\bla\\foldername') : gives a listing of all subfolders/files
    File('.\\Mysc') : gives a listing of all subfolders/files for the mysc folder
    File('.\\Mysc',True) : gives a listing of surface subfolders/files for the mysc folder
    '''

    """
    Based on:
    for subdir, dirs, files in os.walk(path):
        for file in files:
            print(os.path.join(subdir, file))
    """
    def __init__(self,path = '.\\', quick=False):

        #print(path)
        self.path = path # the given path
        #self.rootpath = os.getcwd()+path # core path?
        self.name = path.split('\\')[-1]

        tp = (path.split('.'))
        if len(tp) == 1: # split will make a len 1 list if theres no .
            self.type = 'FOLDER'
        elif ((len(tp) == 2) and (tp[0] == '')) or ('\\' in tp[-1]): # because if you do ".\\Mysc" it makes ['',"\Mysc"]
            self.type = 'FOLDER'
        else:
            self.type = path.split('.')[-1]

        # iteration files
        try:
            if int(tp[-1]) != str: # files typicly dont end in a number (i like this being janky ok?)
                self.type = 'FOLDER'
        except:
            pass

        if self.type == 'FOLDER':

            if not quick: 
                tmp = [(subdir, dirs, files) for subdir, dirs, files in os.walk(path)] # for speed
                if tmp == []:
                    print("Not a valid FOLDER.")
                    tmp = [([],[],[])]
                #print(tmp)
                self.dirs = tmp[0][1] # sub directorys
                self.files = tmp[0][2] # files
                self.subdir = [sub[0] for sub in tmp] # all sub directorys, and this one for some reason

                ''' # this is realy slow but i want it incase i need it
                self.subdir = [subdir for subdir, dirs, files in os.walk(path)] # folderpaths inside this folder
                self.dirs = [dirs for subdir, dirs, files in os.walk(path)][0] # folders inside this folder
                self.files = [files for subdir, dirs, files in os.walk(path)][0] # files inside this folder
                #self.allfilepaths = [os.path.join(subdir, file) for subdir, dirs, files in os.walk(path) for file in files] 
                #self.data = [File(self.subdir[0]+'\\'+sub) for sub in self.dirs] # not a file
                '''
                self.filepaths = [os.path.join(path, file) for file in self.files] # filepaths inside this folder if it is a folder otherwise its empty
                self.allfilepaths = [os.path.join(b[0], file) for b in tmp for file in b[2]] # filepaths inside this folder if it is a folder otherwise its empty

                self.contents = self.filepaths + [os.path.join(path, folder) for folder in self.dirs] # all the filepaths/names for the contens
                self.data = [File(p) for p in self.contents]
            else:
                # gets only the first layer which speeds things up drimaticly
                try:
                    tmp = next(os.walk(path)) # for speed
                except:
                    print("Not a valid FOLDER.")
                    tmp = [[],[],[]]

                self.dirs = tmp[1] # sub directorys
                self.files = tmp[2] # files
                self.subdir = tmp[0] # this folder for some reason

                self.filepaths = [os.path.join(path, file) for file in self.files] # filepaths inside this folder if it is a folder otherwise its empty
                self.allfilepaths = self.filepaths # filepaths inside this folder if it is a folder otherwise its empty

                self.contents = self.filepaths + [os.path.join(path, folder) for folder in self.dirs] # all the filepaths/names for the contens
                self.data = None 
                
        else:
            # if its a file none of thease should hold anything
            self.subdir = None
            self.dirs = None   
            self.files = None
            self.filepaths = None
            self.allfilepaths = None
            # if its not able to get the info, mostly a problem with .lnk files (link files)
            try:
                self.data = open(path,'r') # a file
                self.contents = self.data.read()
            except: # cant read file
                print("Cant read file: {}".format(self.path))
                self.data = None 
                self.contents = None


    def isDirectory(self): # is it a directory
        if self.name == 'FOLDER':
            return(True)
        return(False)

    def help(self): # HELP
        print("Contains path, name, type, subdir, dirs, files, filepaths, allfilepaths, data, and contents.")
        print("Has a faster verson if you do File(path,True). This version misses subdir and data")


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Compare files
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


#
def fileCompare(fileorig,filenew, makefile = True, killondif = False):
    '''
    This compares the contents of two files
        They can be compleatly difrent files
    fileCompare(fileorig,filenew) : gives the lines that are difrent : makes 2 files that show what isent the same
    fileCompare(fileorig,filenew, False) : gives the lines that are difrent : makes nothing
    fileCompare(fileorig,filenew, True, True) : gives true/false as to weather they are the same (file == file) : makes 2 files that show what isent the same
    fileCompare(fileorig,filenew, Flase, True) : gives true/false as to weather they are the same (file == file) : makes nothing
    '''
    f1 = open(fileorig,'r').readlines() # main file
    f2 = open(filenew,'r').read() # file to be compared too

    if makefile: # makes a difreces file
        changed = open('ChangedOrig','w+')

    for a in f1: # iterate through main
        if a in f2: # basicly if it is inside the file
            f2 = f2.replace(a,'\n') # remove it from list

            if makefile: # add to the difreces file
                changed.write('\n')
            if killondif: # files are difrent
                return(False)
        else:
            if makefile: # lines that are difrent
                changed.write(a)
    
    if makefile: # add the lines that are difrent from between them
        changed.close()
        changed = open('ChangedNew','w+')
        changed.writelines(f2)
        changed.close()
    
    if killondif:
        return(True) # same files

    return(f2.split('\n')) # lines that are difrent and location



"""
# for testing use not needed in end result 
if __name__ == "__main__":
    pass

    path = ".\\Mysc"
    #path = "Maze.py"
    print(File(path).subdir) 
    File()
    #""
    d = {"&": '&','Name': "Bob", "age": 35, "height": 6.3, "home": False, "mysc": [True,2,3.1,"four",[5,6,7.3,'nine'],'t',['sup'],{'a':'B'}],"D": {'oh':'no','two': 2, "THREE": 3.3, "Working?": True, "mysc":[1,False,5.5,'6']}}
    l = [[1,2,3],{"a":'A','b':'B','c':'C'}]
    Save('d',d)
    Save('l',l)
    v = Load('d')
    b = Load('l')

    print(d == v)
    print(l == b)
    #print(v)
#"""