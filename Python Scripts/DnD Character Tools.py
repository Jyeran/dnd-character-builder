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
        self.attributes = {'str':s, 'dex':d, 'con':c, 'int':i, 'wis':w, 'cha':ch}

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
        self.attributes = {'str':s, 'dex':d, 'con':c, 'int':i, 'wis':w, 'cha':ch}
    
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


def attDistribute(method, myRace, st = 8, de = 8, co = 8, int = 8, wi = 8, ch = 8):
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

                attributes = {'str':attList[0], 'dex':attList[1], 'con':attList[2], 'int':attList[3], 'wis':attList[4], 'cha':attList[5]}
                return attributes

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
        
        def printStat(attributes, budget):
            idx = 0
            print ('\nUse < or > to toggle increase or decrease\nEnter "done" when finished\n')
            print ('Points Remaining to Distribute: ' + str(budget))
            for att, val in attributes.items():
                print (att.title() +': ' + str(val + myRace.attributes[att]))
                idx += 1


        mode = 'Increase'
        budget = 27
        restricted = True
        attList = [8,8,8,8,8,8]
        attOptions = ["str", "dex", "con", "int", "wis", "cha"]
        attributes = {'str':8, 'dex':8, 'con':8, 'int':8, 'wis':8, 'cha':8}
        for att, val in attributes.items():
                print (att.title() +': ' + str(val))

        keepGoing = True

        while keepGoing:
            print ('\n'*100)
            
            if restricted:
                for att, val in attributes.items():
                    if val < 8:
                        attributes[att] = 8
                        budget -= 1
                    elif val > 15:
                        attributes[att] = 15
                        budget += 2
            
            printStat(attributes, budget)
            sel = input (mode + ': ')         

            if sel.lower() == 'reset':
                for att, val in attributes.items():
                    attributes[att] = 8        

            if mode == 'Increase':
                if (sel.upper() == 'STR' or sel == '1' or sel.upper() == 'STRENGTH' or sel.upper() == 'S') and budget > 0:
                                      
                    if attributes['str'] < 14 and restricted:
                        budget -= 1
                        attributes['str'] = attributes['str'] + 1
                    elif attributes['str'] >= 14 and budget > 1:
                        budget -= 2
                        attributes['str'] = attributes['str'] + 1
                
                elif (sel.upper() == 'DEX' or sel == '2' or sel.upper() == 'DEXTERITY' or sel.upper() == 'D') and budget > 0:
                                        
                    if attributes['dex'] < 14 and restricted:
                        budget -= 1
                        attributes['dex'] = attributes['dex'] + 1
                    elif attributes['dex'] >= 14 and budget > 1:
                        budget -= 2
                        attributes['dex'] = attributes['dex'] + 1
                
                elif (sel.upper() == 'CON' or sel == '3' or sel.upper() == 'CONSTITUTION' or sel.upper() == 'CO') and budget > 0:
                                        
                    if attributes['con'] < 14 and restricted:
                        budget -= 1
                        attributes['con'] = attributes['con'] + 1
                    elif attributes['con'] >= 14 and budget > 1:
                        budget -= 2
                        attributes['con'] = attributes['con'] + 1
                
                elif (sel.upper() == 'INT' or sel == '4' or sel.upper() == 'INTELLIGENCE' or sel.upper() == 'I') and budget > 0:
                                        
                    if attributes['int'] < 14 and restricted:
                        budget -= 1
                        attributes['int'] = attributes['int'] + 1
                    elif attributes['int'] >= 14 and budget > 1:
                        budget -= 2
                        attributes['int'] = attributes['int'] + 1

                elif (sel.upper() == 'WIS' or sel == '5' or sel.upper() == 'WISDOM' or sel.upper() == 'W') and budget > 0:
                                        
                    if attributes['wis'] < 14 and restricted:
                        budget -= 1
                        attributes['wis'] = attributes['wis'] + 1
                    elif attributes['wis'] >= 14 and budget > 1:
                        budget -= 2
                        attributes['wis'] = attributes['wis'] + 1

                elif (sel.upper() == 'CHA' or sel == '6' or sel.upper() == 'CHARISMA' or sel.upper() == 'CH') and budget > 0:
                                        
                    if attributes['cha'] < 14 and restricted:
                        budget -= 1
                        attributes['cha'] = attributes['cha'] + 1
                    elif attributes['cha'] >= 14 and budget > 1:
                        budget -= 2
                        attributes['cha'] = attributes['cha'] + 1

                elif sel == 'done':
                    keepGoing = False    

                elif sel == '<' or sel.lower() == 'decrease':
                    mode = 'Decrease'     


            ####

            elif mode == 'Decrease':
                if (sel.upper() == 'STR' or sel == '1' or sel.upper() == 'STRENGTH' or sel.upper() == 'S'):
                    attributes['str'] = attributes['str'] - 1
                    
                    if attributes['str'] < 14 and restricted:
                        budget += 1
                    elif attributes['str'] >= 14:
                        budget += 2
                
                elif (sel.upper() == 'DEX' or sel == '2' or sel.upper() == 'DEXTERITY' or sel.upper() == 'D'):
                    attributes['dex'] = attributes['dex'] - 1
                    
                    if attributes['dex'] < 14 and restricted:
                        budget += 1
                    elif attributes['dex'] >= 14:
                        budget += 2
                
                elif (sel.upper() == 'CON' or sel == '3' or sel.upper() == 'CONSTITUTION' or sel.upper() == 'CO'):
                    attributes['con'] = attributes['con'] - 1
                    
                    if attributes['con'] < 14 and restricted:
                        budget += 1
                    elif attributes['con'] >= 14:
                        budget += 2
                
                elif (sel.upper() == 'INT' or sel == '4' or sel.upper() == 'INTELLIGENCE' or sel.upper() == 'I'):
                    attributes['int'] = attributes['int'] - 1
                    
                    if attributes['int'] < 14 and restricted:
                        budget += 1
                    elif attributes['int'] >= 14:
                        budget += 2

                elif (sel.upper() == 'WIS' or sel == '5' or sel.upper() == 'WISDOM' or sel.upper() == 'W'):
                    attributes['wis'] = attributes['wis'] - 1
                    
                    if attributes['wis'] < 14 and restricted:
                        budget += 1
                    elif attributes['wis'] >= 14:
                        budget += 2

                elif (sel.upper() == 'CHA' or sel == '6' or sel.upper() == 'CHARISMA' or sel.upper() == 'CH'):
                    attributes['cha'] = attributes['cha'] - 1
                    
                    if attributes['cha'] < 14 and restricted:
                        budget += 1
                    elif attributes['cha'] >= 14:
                        budget += 2

                elif sel == 'done':
                    keepGoing = False

                elif sel == '>' or sel.lower() == 'increase':
                    mode = 'Increase'  

        ####

        return attributes
    #check method
    if method == '1':
        attributes = standardScore()
    elif method == '2':
        attributes = pointBuy()
    
    return attributes
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
           "3. Character Generator\n"
           "4. Spell Randomizer\n")
    menuSelect = input("Select Module: ")
    
    if menuSelect == '1':
        characterCreate()



def selectRace ():
    print ("\n \n \nAvailable Races:")

    #eventually add in race descriptions
    x = 0
    for i in races:
        print (str(x+1) + ": " + str(races[x].name))
        x += 1

    print ("\n")

    raceSelect = races[int(input("Select your race: "))-1]

    #   classSelect
    print ("\n"*100)  
    print ("You chose: " + raceSelect.name)

    return raceSelect
    #add number and string checker

def characterCreate ():
    print ("\n"*100)  
    
    selectedRace = selectRace()

    print ("\n\nAttribute Distributions:\n"
           "1. Standard Score\n"
           "2. Point Buy\n"
           "3. Roll Stats\n"
           "4. Limited Random\n"
           "5. Min/Max\n"
           "6. Complete Anarchy\n")

    distSelect = input('Select Distribution: ')

    selectedAttributes = attDistribute(distSelect, selectedRace)

    ####
    
    #Chose Allignment
    #Chose Sex
    #Chose Height
    #Choose Wight
    #Chose Ideals
    #Chose Bonds
    #Flaws
    #Choose Background and Skill Proficiencies
    #Choose Name
    #Choose Equipment



#
#


#def statGen (method)



#Character Stat Generator



#statPrint()


#print ('Int: '+ str(intel) + '\n' +
#        'Test')



menu()
