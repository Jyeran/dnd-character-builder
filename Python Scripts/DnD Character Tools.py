import math
import csv
import os

class Race:
    #pass through the race name, attributes, and half elf choice list
    def __init__(self, name, s, d, c, i, w, ch, helf = [0,0]):
        self.name = name
        self.sMod = s
        self.dMod = d
        self.cMod = c
        self.iMod = i
        self.wMod = w
        self.chMod = ch
        self.helf = helf

    def applyHelf(self):
        for i in self.helf:
            
            if self.helf[i-1] == 1:
                self.sMod += 1
            elif self.helf[i-1] == 2:
                self.dMod += 1
            elif self.helf[i-1] == 3:
                self.cMod += 1
            elif self.helf[i-1] == 4:
                self.iMod += 1
            elif self.helf[i-1] == 5:
                self.wMod += 1
            elif self.helf[i-1] == 6:
                self.chMod += 1


class dndClass:
    pass

class Character:
    
    def __init__(self, cName, Race, st, de, co, inte, wi, ch):
        self.name = cName
        self.race = Race.name
        self.st = st
        self.de = de
        self.co = co
        self.int = inte
        self.wi = wi
        self.ch = ch
        self.raceClass = Race
    
    def applyRaceModifiers(self):
        self.raceClass.applyHelf()
        self.st += self.raceClass.sMod
        self.de += self.raceClass.dMod
        self.co += self.raceClass.cMod
        self.int += self.raceClass.iMod
        self.wi += self.raceClass.wMod
        self.ch += self.raceClass.chMod

#
def statPrint(attList):
    string = 'Str: '+ str(attList[0]) + '\n' + \
             'Dex: '+ str(attList[1]) + '\n' + \
             'Con: '+ str(attList[2]) + '\n' + \
             'Int: '+ str(attList[3]) + '\n' + \
             'Wis: '+ str(attList[4]) + '\n' + \
             'Cha: '+ str(attList[5]) + '\n' 
    print (string)

def whichAtt (instruct = 1):
    pass


def attDistribute(method, race = "no", st = 8, de = 8, co = 8, int = 8, wi = 8, ch = 8):
    print ("\n" * 100)
    
    #standard Score
    def standardScore():
        stop = 0
        attList = [8,8,8,8,8,8]
        attOptions = ["str", "dex", "con", "int", "wis", "cha"]
        stdList = [15,14,13,12,10,8]
        while (stop == 0):
            print ("\n" * 100)
            print ("Assign the standard set to your attributes (15,14,13,12,10,8)\n")        
            
            def inputScore():
                count = 0
                for n in attList:
                    #if count == 0:
                        #print ("Enter: str, dex, con, int, wis, cha")
                        
                       #add to input check a "have you already entered strength.. etc"
                    inputCheck = 0
                    while inputCheck == 0:    
                        inputCheck = 1
                        outString = "\nEnter: " + ', '.join(attOptions)
                        x = input(outString + "\nWhich attribute is " + str(stdList[count]) + ":")
                        
                        if x == 'str' and (x in attOptions):
                            attList[0] = stdList[count]
                            attOptions.remove(x)
                        elif x == 'dex' and (x in attOptions):
                            attList[1] = stdList[count]
                            attOptions.remove(x)
                        elif x == 'con' and (x in attOptions):
                            attList[2] = stdList[count]
                            attOptions.remove(x)
                        elif x == 'int' and (x in attOptions):
                            attList[3] = stdList[count]
                            attOptions.remove(x)
                        elif x == 'wis' and (x in attOptions):
                            attList[4] = stdList[count]
                            attOptions.remove(x)
                        elif x == 'cha' and (x in attOptions):
                            attList[5] = stdList[count]
                            attOptions.remove(x)
                        else:
                            inputCheck = 0
                            print ('\nUnrecognized input. Try again.')
                    
                    count += 1

                return attList

            attList = inputScore()
            print ("\n"*100)
            statPrint(attList)
            print ("\n")
            yn = input("Is this correct? (Y/N): ")

            if (yn.upper() == 'Y') or (yn == '1') or (yn.upper() == 'YES'):
                stop = 1

        return attList


    #Point Buy
    def pointBuy():
        pass
    
    #check method
    if method == 1:
        attList = standardScore()
    #

"""
class Attributes:

    def __init__(self, st, de, co, int, wi, ch):
        self.st = st
        self.
"""
#
#Read in CSV data and populate Race class
dirpath = os.path.realpath(__file__)
dirpath = dirpath.replace('\DnD Character Tools.py', '')
with open(dirpath + '\DnDRaces.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)

    races = []

    for row in csvReader:
        race = row[0]
        st = row[1]
        de = row[2]
        co = row[3]
        inte = row[4]
        wi = row[5]
        ch= row[6]

        races.append(Race(name=race,s=int(st),
                                    d=int(de),
                                    c=int(co),
                                    i=int(inte),
                                    w=int(wi),
                                    ch=int(ch)) )
        #races.append(Race(name=race,s=int(st),d=de,c=co,i=inte,w=wi,ch=ch) )
    q=4
#    print (type(races[q].sMod))
#    print (races[q].sMod)
#
#
"""
morton = Character("Morton", races[12], 10, 10, 10, 10, 10, 10)
horton = Character("Morton", races[11], 10, 10, 10, 10, 10, 10)

horton.raceClass.helf = [1,2]
horton.applyRaceModifiers()
morton.applyRaceModifiers()

#print (str(morton.race) + " " + str(morton.st) + " " + str(morton.de))
#print (str(horton.race) + " " + str(horton.st) + " " + str(horton.de))
"""

def menu ():
    print ('\n' * 100)
    print ("Welcome to the Character Generator. \n \n"  
           "Available Modules:\n"
           "1. Character Creator\n"
           "2. Character Leveler\n"
           "3. Spell Randomizer\n")
    menuSelect = input("Select Module: ")
    
    if menuSelect == '1':
        characterCreate()





def characterCreate ():
    print ("\n"*100)  
    print ("\n \n \nAvailable Races:")

#eventually add in race descriptions
    x = 0
    for i in races:
        print (str(x+1) + ": " + str(races[x].name))
        x += 1

    print ("\n")

    raceSelect = races[int(input("Select your race: "))-1].name

#   classSelect
    print ("\n"*100)  
    print ("You chose: " + raceSelect)
    #add number and string checker

    print ("\n\nAttribute Distributions:\n"
           "1. Standard Score\n"
           "2. Point Buy\n"
           "3. Roll Stats\n"
           "4. Limited Random\n"
           "5. Min/Max\n"
           "6. Complete Anarchy\n")

    distSelect = input('Select Distribution: ')

    attDistribute(1)


    att = [8,8,8,8,8,8]
#
#


#def statGen (method)



#Character Stat Generator



#statPrint()


#print ('Int: '+ str(intel) + '\n' +
#        'Test')



menu()