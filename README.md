# JTools
All of my usefull tools in one nice package

To install:
pip install git+https://github.com/Quiltic/JTools.git


Currently The main section is Called JTools this version is for python.
 - It contains a few things with more on the way.
    - File(PATH)
       - gives info/contents of a folder, otherwise opens it with open(FILE)
    - Save(FILE_NAME, DICTIONARY_OR_LIST) 
       - Saves a dict or list to a file to FILE_NAME
    - Load(NAME_OF_XML_FILE_FROM_SAVE)
       - Loads a file made by Save 
    - functionTimer(NAME,TURN_OFF_PRINTING)
       - Put once before a function and once after to display the amount of time a function/proccess takes (in seconds)
    - average(DATA)
       - returns the average of the list imputed (or a list of averages)
    - fileCompare(ORIGIONAL,NEW, CREATE_DIFRENCES_FILE, KILL_ON_DIFRENT)
       - This compares the contents of two files
       - They can be compleatly difrent files
    - fraction_finder(FLOAT, APROXIMATE):
       - Given a float it will give you a the 2 smallest numbers needed to get the float if divided 
    - timeDifrence(START, END)
       - Gives the difrence between two clock hours (8:30am, 12:30pm)
    - find_all(STRING, FIND)
       - Given a string this finds all FIND segments inside the string
       - Has a generator which is called find_all_generator
    - braketsSplitter(EQUATION):
       - Given equ split it into an array which contains the location of the brackets
    - Science (from JTools import Science)
       - calculateMoleculeMass(EQUATION)
           - Get the molecular mass of an equation
       - Periodic table included (not finished some elements are missing)
