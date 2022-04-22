#!/usr/bin/env python

import random

import pickle

colordic = {1:'[1]red',2:'[2]blue',3:'[3]yellow',4:'[4]green',5:'[5]purple',6:'[6]orange',7:'[7]pink',8:'[8]indigo'}

userDocument = {'T':0,'currentTrails':0,'secret':[],'color':0,'pegs':0,'history':{},'BaW':{},'colorprint':{},'colornumber':0}

userinputhistory = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[]}                                             # Those are dictionaries, colordic is the color whith it's corresponding number, so user don't need to enter color name,every time.
                                                                                                                                # userDocument will save what user has enterd and some game information, so it can be saved.
BaWhistory = {1:[0,0],2:[0,0],3:[0,0],4:[0,0],5:[0,0],6:[0,0],7:[0,0],8:[0,0],9:[0,0],10:[0,0],11:[0,0],12:[0,0]}               # userinputhistory and BaWhistory are two dictionaries which will saved the output of user and output of computer, like colors and the number of black and white 

colorprint = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[]}

trails = 0                      
Sure = False
Running = True                         # Some original value which will keep funcions runs well.
colorsingle = False
AIgameplay = False
secret = []
buff = []
userinput = []


def start():   # start fuction will ask you read the README or not and print greeting() , it also consists other function setting()
    greetingprint()
    askuser = raw_input("Would you need any help? \n (press 'y' for help, or press any key to skip) ")
    if askuser.lower() == 'y':
        f = open('README.txt','r')
        text = f.read()
        cleanscreen()
        print text
        x = raw_input('Continue[Enter]')
        cleanscreen()   # Cleanscreen()  will print 70 speace line,so it looks like the screen has been cleared.
    else:
        cleanscreen()
        pass
    print ''
    print '####################################################################################################'
    print ''
    askuseragain = raw_input('Your can change game setting here[c] or skip[Enter]\n(the default value of trails is 12 | number repeats is (on)) \n####################################################################################################\n')
    cleanscreen()                    
    if askuseragain.lower() == 'c':          # With raw_input() user can customise the game. Based on setting() 
        setting()
        cleanscreen()
        return start()
    else:
        cleanscreen()
        pass
    
def greetingprint():           # Print the title
    print 'HELLO:'
    print 'Welocom to: '
    print ''
    print ''
    print '###  ###       #       ########    ########   #######    ######  '        
    print '#  ##  #      ##      #               ##      #         #      # '
    print '#  ##  #     #  #      #######        ##      #######   #######   '
    print '#      #    ######            #       ##      #         #      #  '
    print '#      #   #      #   ########        ##      #######   #      #  '
    print '                                                                 '
    print '###  ###   ########   #       #    #######        '
    print '#  ##  #      ##      # #     #    #      #    '
    print '#  ##  #      ##      #   #   #    #      #    '              
    print '#      #      ##      #     # #    #      #      '
    print '#      #   ########   #       #    #######      '
    print ''
    print ''
    print ''

def winprint():      # When you win the game. Print congratulation.
    print ''
    print ''
    print ' ######      ######    #       #    ######    ######        #      ########    #       #    ##             #    ########   ########    ######     #       #           ##   '
    print '#      #    #      #   # #     #   #         #      #      ##         ##       #       #    ##            ##       ##         ##      #      #    # #     #           ## '
    print '#           #      #   #   #   #   #   ###   #######      #  #        ##       #       #    ##           #  #      ##         ##      #      #    #   #   #           ##' 
    print '#      #    #      #   #     # #   #      #  #      #    ######       ##       #       #    ##          ######     ##         ##      #      #    #     # #                 '
    print ' ######      ######    #       #    ######   #      #   #      #      ##        #######     ########   #      #    ##      ########    ######     #       #           ##    '
    print ''
    print ''



def gameboard():     # This will print out the user interface.
    syscolor(colordic)
    if colorsingle == False:    # Check whether the colorsingle is on or off.
        single = 'Color [Repeat]'
    elif colorsingle == True:
        single = 'Color [Single]'
    print''
    print '####################################################################################################'
    print '                                      Game information:'                                                # This include game information. Total trail, pegs, and single color allowed or not.
    
    print ''                                        
    print '    Total Trails: ' + str(t) +'        ' +'Pegs: ' + str(pegs)  + '       ' +  single                    # All variables can be set by user through the next function.
    print '    Color: ' + str(colorprint1)
    print ''
    print '####################################################################################################'
    print ''
    print '===================================================================================================='
    print ''
    print 'Game Start,GOOD LUCK:)'
    print ''
    if int(t) == 12:
        print 'Trail: 12  ' + str(colorprint[12]) + '          Hint:'  + BaWhistory[12][0]*'b ' + BaWhistory[12][1]*'w ' + (pegs - (BaWhistory[12][0]+BaWhistory[12][1]))*'_'
        print ''
        print 'Trail: 11  ' + str(colorprint[11]) + '          Hint:' + BaWhistory[11][0]*'b ' + BaWhistory[11][1]*'w '  + (pegs - (BaWhistory[11][0]+BaWhistory[11][1]))*'_'
        print ''
        print 'Trail: 10  ' + str(colorprint[10]) + '          Hint:' + BaWhistory[10][0]*'b ' + BaWhistory[10][1]*'w ' + (pegs - (BaWhistory[10][0]+BaWhistory[10][1]))*'_' 
        print ''
        print 'Trail: 09  '  + str(colorprint[9]) + '          Hint:' + BaWhistory[9][0]*'b ' + BaWhistory[9][1]*'w ' + (pegs - (BaWhistory[9][0]+BaWhistory[9][1]))*'_' 
        print ''
        print 'Trail: 08  '  + str(colorprint[8]) + '          Hint:' + BaWhistory[8][0]*'b ' + BaWhistory[8][1]*'w ' + (pegs - (BaWhistory[8][0]+BaWhistory[8][1]))*'_' 
        print ''
        print 'Trail: 07  '   + str(colorprint[7]) + '          Hint:' + BaWhistory[7][0]*'b ' + BaWhistory[7][1]*'w ' + (pegs - (BaWhistory[7][0]+BaWhistory[7][1]))*'_'        # This will print out what the user enterd and hints. In three different cases.
        print ''
        print 'Trail: 06  '   + str(colorprint[6]) + '          Hint:' + BaWhistory[6][0]*'b ' + BaWhistory[6][1]*'w ' + (pegs - (BaWhistory[6][0]+BaWhistory[6][1]))*'_' 
        print ''
        print 'Trail: 05  '   + str(colorprint[5]) + '          Hint:' + BaWhistory[5][0]*'b ' + BaWhistory[5][1]*'w ' + (pegs - (BaWhistory[5][0]+BaWhistory[5][1]))*'_' 
        print ''
        print 'Trail: 04  '  + str(colorprint[4]) + '          Hint:' + BaWhistory[4][0]*'b ' + BaWhistory[4][1]*'w ' + (pegs - (BaWhistory[4][0]+BaWhistory[4][1]))*'_' 
        print ''
        print 'Trail: 03  '   + str(colorprint[3]) + '          Hint:' + BaWhistory[3][0]*'b ' + BaWhistory[3][1]*'w ' + (pegs - (BaWhistory[3][0]+BaWhistory[3][1]))*'_' 
        print ''
        print 'Trail: 02  '  + str(colorprint[2]) + '          Hint:' + BaWhistory[2][0]*'b ' + BaWhistory[2][1]*'w ' + (pegs - (BaWhistory[2][0]+BaWhistory[2][1]))*'_' 
        print ''
        print 'Trail: 01  '   + str(colorprint[1]) + '          Hint:' + BaWhistory[1][0]*'b ' + BaWhistory[1][1]*'w ' + (pegs - (BaWhistory[1][0]+BaWhistory[1][1]))*'_' 
        print ''
        print '===================================================================================================='
    elif int(t) == 10 :
        print 'Trail: 10  ' + str(colorprint[10]) + '          Hint:' + BaWhistory[10][0]*'b ' + BaWhistory[10][1]*'w ' + (pegs - (BaWhistory[10][0]+BaWhistory[10][1]))*'_' 
        print ''
        print 'Trail: 09  '  + str(colorprint[9]) + '          Hint:' + BaWhistory[9][0]*'b ' + BaWhistory[9][1]*'w ' + (pegs - (BaWhistory[9][0]+BaWhistory[9][1]))*'_' 
        print ''
        print 'Trail: 08  '  + str(colorprint[8]) + '          Hint:' + BaWhistory[8][0]*'b ' + BaWhistory[8][1]*'w ' + (pegs - (BaWhistory[8][0]+BaWhistory[8][1]))*'_' 
        print ''
        print 'Trail: 07  '   + str(colorprint[7]) + '          Hint:' + BaWhistory[7][0]*'b ' + BaWhistory[7][1]*'w ' + (pegs - (BaWhistory[7][0]+BaWhistory[7][1]))*'_' 
        print ''
        print 'Trail: 06  '   + str(colorprint[6]) + '          Hint:' + BaWhistory[6][0]*'b ' + BaWhistory[6][1]*'w ' + (pegs - (BaWhistory[6][0]+BaWhistory[6][1]))*'_'       # All variables are refer to the dictionary .
        print ''
        print 'Trail: 05  '   + str(colorprint[5]) + '          Hint:' + BaWhistory[5][0]*'b ' + BaWhistory[5][1]*'w ' + (pegs - (BaWhistory[5][0]+BaWhistory[5][1]))*'_' 
        print ''
        print 'Trail: 04  '  + str(colorprint[4]) + '          Hint:' + BaWhistory[4][0]*'b ' + BaWhistory[4][1]*'w ' + (pegs - (BaWhistory[4][0]+BaWhistory[4][1]))*'_' 
        print ''
        print 'Trail: 03  '   + str(colorprint[3]) + '          Hint:' + BaWhistory[3][0]*'b ' + BaWhistory[3][1]*'w ' + (pegs - (BaWhistory[3][0]+BaWhistory[3][1]))*'_' 
        print ''
        print 'Trail: 02  '  + str(colorprint[2]) + '          Hint:' + BaWhistory[2][0]*'b ' + BaWhistory[2][1]*'w ' + (pegs - (BaWhistory[2][0]+BaWhistory[2][1]))*'_' 
        print ''
        print 'Trail: 01  '   + str(colorprint[1]) + '          Hint:' + BaWhistory[1][0]*'b ' + BaWhistory[1][1]*'w ' + (pegs - (BaWhistory[1][0]+BaWhistory[1][1]))*'_' 
        print ''
        print '===================================================================================================='

    elif int(t) == 8 :
        print 'Trail: 08  '  + str(colorprint[8]) + '          Hint:' + BaWhistory[8][0]*'b ' + BaWhistory[8][1]*'w ' + (pegs - (BaWhistory[8][0]+BaWhistory[8][1]))*'_' 
        print ''
        print 'Trail: 07  '   + str(colorprint[7]) + '          Hint:' + BaWhistory[7][0]*'b ' + BaWhistory[7][1]*'w ' + (pegs - (BaWhistory[7][0]+BaWhistory[7][1]))*'_' 
        print ''
        print 'Trail: 06  '   + str(colorprint[6]) + '          Hint:' + BaWhistory[6][0]*'b ' + BaWhistory[6][1]*'w ' + (pegs - (BaWhistory[6][0]+BaWhistory[6][1]))*'_' 
        print ''
        print 'Trail: 05  '   + str(colorprint[5]) + '          Hint:' + BaWhistory[5][0]*'b ' + BaWhistory[5][1]*'w ' + (pegs - (BaWhistory[5][0]+BaWhistory[5][1]))*'_' 
        print ''
        print 'Trail: 04  '  + str(colorprint[4]) + '          Hint:' + BaWhistory[4][0]*'b ' + BaWhistory[4][1]*'w ' + (pegs - (BaWhistory[4][0]+BaWhistory[4][1]))*'_' 
        print ''
        print 'Trail: 03  '   + str(colorprint[3]) + '          Hint:' + BaWhistory[3][0]*'b ' + BaWhistory[3][1]*'w ' + (pegs - (BaWhistory[3][0]+BaWhistory[3][1]))*'_' 
        print ''
        print 'Trail: 02  '  + str(colorprint[2]) + '          Hint:' + BaWhistory[2][0]*'b ' + BaWhistory[2][1]*'w ' + (pegs - (BaWhistory[2][0]+BaWhistory[2][1]))*'_' 
        print ''
        print 'Trail: 01  '   + str(colorprint[1]) + '          Hint:' + BaWhistory[1][0]*'b ' + BaWhistory[1][1]*'w ' + (pegs - (BaWhistory[1][0]+BaWhistory[1][1]))*'_'
        print ''
        print '===================================================================================================='
        print ''
        print ''

def cleanscreen():
    print 70*'\n'    
    
def save(userDocument):
    s = open('Document.txt','w').close()       # Clean the save file.
    s = open('Document.txt','w')
    userDocument['history'] = userinputhistory  
    userDocument['BaW'] = BaWhistory
    userDocument['colorprint'] = colorprint
    pickle.dump(userDocument,s)                # Using pickle module to save dictionary into document.txt
    s.close()

def load():
    global trails,secret,pegs,t,BaWhistory,colorprint1,colorprint2,colorprint,color,userinputhistory
    try:
        l = open('Document.txt','r')
        userDocument = pickle.load(l)
        t = int(userDocument['T'])              # Refer to dictionary saved in document.txt   set game value.
        pegs = int(userDocument['pegs'])
        trails = int(userDocument['currentTrails'])
        secret = userDocument['secret']
        BaWhistory = userDocument['BaW']
        colorprint1 = userDocument['color']
        userinputhistory = userDocument['history']
        colorprint = userDocument['colorprint']
        color = userDocument['colornumber']
        l.close()
    except:
        print 'Please make sure you have saved before'
        return MasterMind()
    

def Color():
    global color
    print ''
    print'####################################################################################################'
    color = raw_input('Enter the number of colors(3-8): \n####################################################################################################\n')
    try:
        int(color)
        if int(color) > 8 or int(color) < 3:
            print 'The number of color is wrong, do it again please. '     # using raw_input ask user to choose the numer of color in the game.
            return Color()
        else:
            color = int(color)
            userDocument['colornumber'] = color
    except:
        print 'please enter a valid number'
        return Color()
    cleanscreen()


def Pegs():
    global pegs
    print'####################################################################################################'    # '####' forms framwork
    pegs = raw_input('Enter the number of pegs(3-8)\nthis should also less than ' + str(color) + ' :  \n####################################################################################################\n')
    try:
        int(pegs)
        if int(pegs) > color or int(pegs) < 3:
            print 'The number of pegs is wrong, do it again please. '   # Similar to Color(). Ask user to input number of pegs
            return Pegs()
        else:
            userDocument['pegs'] = int(pegs)
            pegs = int(pegs)
            cleanscreen()
            return pegs
            
    except:
        print 'please enter a valid number'
        return Pegs()
    

    
def Codemaker():
    global secret,colorsingle              # In codemaker() there are two cases, single color and not single.
    Color()
    Pegs()
    colorsingleL = []                     # When colorsingle == True   using for loop and random.choice to append color into 'secret' list ,and delete that color so it won't repeat.
    if colorsingle == True:
        for x in range(1,int(color)+1):
            colorsingleL.append(colordic[x])
        for x in range(pegs):
            a = str(random.choice(colorsingleL))
            secret.append(a)
            colorsingle.remove(a)
    elif colorsingle == False:          # When colorsingle == False    using for loop and append random.randint(1,color) to append a particular number of   color in secret list.
        for x in range(pegs):
            secret.append(random.randint(1,color))
    userDocument['secret'] = secret      # Save to document
    colorsingleL = []

    

def Entered(Sure):
    global userinput,guess
    print '####################################################################################################'
    print ''
    print 'Trail: ' + str(trails)
    userinput = []
    guess = []
    if Sure == False:       
        inputNumber = raw_input("'Try, it's your turn' (using comma to seperate them): \n\n####################################################################################################\n ")
        guess = inputNumber.split(',')                              # raw_input ask user enter their answers.
        Asking()
        if len(guess) > pegs:
            print 'Please enter a valid number\n it should looks like n,n,n,n... \n####################################################################################################\n'
            return Entered(Sure)
        for x in guess:
            if x == '':
                check = raw_input('Are you sure you want to enter a empty value?(y/n) \n####################################################################################################\n\n')
                if check.lower() == 'y':
                    x = 0
                else:
                    guess = []
                    return Entered(Sure)
            elif int(x) > color:
                print 'The number you entered is out of range,check and enter again. \n####################################################################################################\n\n'
                
                return Entered(Sure)
            elif int(x) < 0:
                print 'The number you entered should greater than 0, check and enter again. \n####################################################################################################\n\n'
            try:
                int(x)
                if int(x) > color or int(x) < 0 :
                    print 'Please enter a valid number\n it should looks like n,n,n,n...!!!\n####################################################################################################\n\n'
                    return Entered(Sure)
            except:
                print 'Please enter a valid number. Try again'
                return Entered(Sure)                           # using Condition make sure user enterd in the right form, then append the value into 'userinput' list
        for char in guess:
            userinput.append(int(char))
        guess = []    
        if len(userinput) != pegs:
            print "If you want to input empty value, using '' stands for it.(like n,'',n....)\n####################################################################################################\n\n"
            Sure = False
            guess = []
            userinput = []
            return Entered(Sure)
        print ''
        print ''
    cleanscreen()

        
def Asking():
    global userinput
    print ''
    a = raw_input(' Confirm your answer[AnyKey]  Save[s]  Restart the game[r] Save and Quit[q]  See the Hidden Answer[cheat]  Redo[n]  ')
    if a.lower() == 's':
        save(userDocument)               # This works as 'actionbar' every time user entered their answer , it will appeared.
    elif a.lower() == 'r':
        return MasterMind()              # Asking user what they want . confirm answer save resart and see the answer, just type the letter in the '[]'
    elif a.lower() == 'q':
        save(userDocument)              # And if conditon will check what user want.
        quit()
    elif a.lower() == 'n':
        userinput = []
        return Entered(Sure)
    
    elif a.lower() == 'cheat':
        print 'The answer is:'
        print '################'
        print  str(secret)         # Print answer   str(secret)      secret is a list
        print  ':)'
        print '################'
        x = raw_input('Press [Enter] to continue.')
        
    
    else:
        pass    
       
def saveInput(trails):
    if AIgameplay == False:
        if int(t) == 12:
            userinputhistory[13-trails] = userinput        # This will save total trails into document dictionary
        elif int(t) == 10:
            userinputhistory[11-trails] = userinput
        elif int(t) == 8:
            userinputhistory[9-trails] = userinput
    elif AIgameplay == True:
        if int(t) == 12:
            userinputhistory[trails] = userinput        
        elif int(t) == 10:
            userinputhistory[trails] = userinput
        elif int(t) == 8:
            userinputhistory[trails] = userinput

def saveBaW(black,white):
    if AIgameplay == False:
        if int(t) == 12:
            BaWhistory[13-trails] = [black,white]       # This saved the black and white history into the dictionary   using dic[key] = value.
        elif int(t) == 10:
            BaWhistory[11-trails] = [black,white]
        elif int(t) == 8:
            BaWhistory[9-trails] = [black,white]
        
    elif AIgameplay == True:
        if int(t) == 12:
            BaWhistory[trails] = [black,white]       # The case for AI playing
        elif int(t) == 10:
            BaWhistory[trails] = [black,white]
        elif int(t) == 8:
            BaWhistory[trails] = [black,white]

            
def colorPrint2():
    if AIgameplay == False:
        if int(t) == 12:
            colorprint[13-trails] = colorprint2       # This saved the user answer history using "dic[key] =value"
        elif int(t) == 10:
            colorprint[11-trails] = colorprint2
        elif int(t) == 8:
            colorprint[9-trails] = colorprint2
    elif AIgameplay == False:
        if int(t) == 12:
            colorprint[trails] = colorprint2       
        elif int(t) == 10:
            colorprint[trails] = colorprint2
        elif int(t) == 8:
            colorprint[trails] = colorprint2    

            
def Hintmaker():
    global white,black
    white = 0
    black = 0
    positionblack = []
    positionwhite = []          # For hintmaker, it first creat two empty boolean list for black and white and two 0 value for black and white.
    for x in secret:
        positionblack.append(x)  
        positionwhite.append(x)

    for n in range(len(positionblack)):
        positionblack[n] = False
    for n in range(len(positionwhite)):   # Set boolean to black and white list
        positionwhite[n] = False
    for x in range(len(secret)):            # Check for black
        if secret[x] == userinput[x]:       
            black += 1
            positionblack[x] = True      # If meet the condition, black + 1 and in that position for two boolean list will be true 
            positionwhite[x] = True
            
    for x in range(len(secret)):         # Only when position is not true , it start to count the white number.
        if positionblack[x] == False:
            for y in range(len(secret)):   
                if secret[x] == userinput[y] and positionwhite[y] == False :  # In this case , when two value are the same , they must in different position because the boolean value is false
                            white += 1                   # So white +1 and then, in that position,  both set to True
                            positionwhite[y] = True
                            positionblack[x] = True   
def syscolor(colordic):
    global color,colorprint1
    try:
        if printcolor == True:          # Refer to colordic dictionary and the value of color , print what color could be in the secret list.
            colorprint1 = []
            for x in range(1,int(color)+1):
                    colorprint1.append(colordic[x])
            userDocument['color'] = colorprint1

    except:
        pass

def usercolor(colordic):             # This will print out the user's color after they enterd thier answer. It look up to colordic dictionary.
    global userinput,colorprint2
    colorprint2 = []
    for x in userinput:
            colorprint2.append(colordic[x])

def trail():
    global trails,t
    print '####################################################################################################'
    t = raw_input('How many trails would you prefer, 8 10 or 12 ?  \n####################################################################################################\n\n')
    if t == '8':
        trails = 8
        userDocument['T'] = 8            # Ask for user to set the number of trails 8, 10 or 12. using raw_input and condition.
    elif t == '10':
        trails = 10
        userDocument['T'] = 10
    elif t == '12':
        trails = 12
        userDocument['T'] = 12
    else:
        print 'Enter a valid number. '
        return trail()

    
def mode():
    question = raw_input('')

    
def setting():
    global question,colorsingle,AIgameplay
    print '####################################################################################################'
    print ''
    question = raw_input('This Is Game Setting: Changing Trails[c]  Changing To COM vs COM[v] Allow Repeats[y/n]  Skip[Enter] :  \n####################################################################################################\n\n')
    print ''
    print ''
    if question.lower() == 'c':                # Allowed user to change the parameter of the game by using raw_input and if condition.
        return trail()
    elif question.lower() == 'y':
        singlecolor = True
    elif question.lower() == 'n':
        singlecolor = False
    elif question.lower() == 'v':
        AIgameplay = True
    else:
        pass

def AI():
    global userinput,AIn,AIo
    userinput = []
    templist =[]
    userinput = templist
    if int(trails) < int(t):     # This is AI , it first will find out what color might be by using while loop, each time , it will check the black and white value and save the color that makes black and white change.
        while black + white == 0:
            for x in range(len(secret)):    # How it works:  first [1,1,1,1]   by analysing b,w  [1,2,2,2] ......to make sure what color in secret
                userinput.append(AIn)
                templist.append(AIn)
            AIn += 1
            
            return userinput
                
        AIn += 1
        if black > 0 or white > 0:
            userinput[:(black+white)-1] = AIn
            templisr.append(AIn)
            
            while black + white < int(len(secret)):
                for x in range(secret-(black+white)):
                    userinput[(black+white)+AIo] = AIn
                    templist[(black+white)+AIo] = AIn
                    AIo += 1
                return userinput
                
        while black + white == int(color):
            random.shuffle(userinput)       # When find out the color , rearrange it untill reach the answer
            userinput = templist
            return userinput
            
            
        
                
def AIgame():
    global trails,userinput,black,white,printcolor          # This AIgame fuction is similar t game() but something has changed in order to run AI game
    gameboard()
    while trails > 0:
        if trails == 0:
            if black == int(pegs):          
                winprint()
                print 'Opps, you have run out of your trails, you loss.'
                res = raw_input('Do you want to restart the game[r]?, or the game will finish')
                if res.lower() == 'r':
                    return MasterMind()
                else:
                    pass
            else:
                print 'Opps, you have run out of your trails, you loss.'
                res = raw_input('Do you want to restart the game[r]?, or the game will finish')
                if res.lower() == 'r':
                    return MasterMind()
                else:
                    pass
        syscolor(colordic)      
        AI()
        cleanscreen()
        trails += 1
        saveInput(trails)
        usercolor(colordic)
        trails -= 1
        colorPrint2()
        
        Hintmaker()
        saveBaW(black,white)
        gameboard()
        trails += 1

        if black == int(pegs) :
            winprint()
            break           
        userinput = []
        userDocument['currentTrails'] = trails

    if trails == 0:         # The case when user used up trails 
        if black == int(pegs):   # Win
            winprint()
            res = raw_input('Do you want to restart the game[r]?, or the game will finish')
            if res.lower() == 'r':
                return MasterMind()
            else:
                pass
        else:     # Lose condition.
            print 'Opps, you have run out of your trails, you loss. :( '
            print 'The real answer is: ' + str(secret)
            res = raw_input('Do you want to restart the game[r]?, or the game will finish')    # After finish game , using raw_input ask user to play again.
            if res.lower() == 'r':
                return MasterMind()
            else:
                pass
            


    

def game():
    global trails,userinput,black,white,printcolor          # This is main function, it put all function together.
    gameboard()
    while trails > 0:
        if trails == 0:
            if black == int(pegs):              # check win condition
                winprint()
                print 'Opps, you have run out of your trails, you loss.'
                res = raw_input('Do you want to restart the game[r]?, or the game will finish')
                if res.lower() == 'r':
                    return MasterMind()
                else:
                    pass
            else:
                print 'Opps, you have run out of your trails, you loss.'
                res = raw_input('Do you want to restart the game[r]?, or the game will finish')
                if res.lower() == 'r':
                    return MasterMind()
                else:
                    pass
        syscolor(colordic)      # Start to run function one by one.
        Entered(Sure)
        cleanscreen()
        trails -= 1
        saveInput(trails)
        usercolor(colordic)
        trails += 1
        colorPrint2()
        Hintmaker()
        saveBaW(black,white)
        gameboard()
        trails -= 1

        if black == int(pegs) :
            winprint()
            res = raw_input('Do you want to restart the game[r]?, or the game will finish')
            if res.lower() == 'r':
                cleanscreen()
                return MasterMind()
            else:
                pass
            break           
        userinput = []
        userDocument['currentTrails'] = trails

    if trails == 0:         # The case when user used up trails 
        if black == int(pegs):   # Win
            winprint()
            res = raw_input('Do you want to restart the game[r]?, or the game will finish')
            if res.lower() == 'r':
                return MasterMind()
            else:
                pass
        else:     # Lose condition.
            print 'Opps, you have run out of your trails, you loss. :( '
            print 'The real answer is: ' + str(secret)
            res = raw_input('Do you want to restart the game[r]?, or the game will finish')    # After finish game , using raw_input ask user to play again.
            if res.lower() == 'r':
                return MasterMind()
            else:
                pass
            
def MasterMind():
    global trails,userinput,black,white,printcolor,secret,t,colorsingle,AIn,AIo,templist    # running this function will Set default value . And ask user to load game.
    pegs = 0
    color = 0
    t = 12
    userDocument['T'] = t
    trails = 12
    secret = []
    userinput = []
    templist = []
    black = 0
    white = 0
    AIn = 1
    AIo = 0
    printcolor = True
    colorsingle = False
    start()
    print'####################################################################################################'
    askload = raw_input("Do you want to load the game? [y]\nSkip[Any KEY]) \n####################################################################################################\n")
    if askload == 'y':
        cleanscreen()
        load()
        printcolor = False
        game()
    cleanscreen()
    Codemaker()
    if AIgameplay == True:
        trails = 1
        return AIgame()
    elif AIgameplay == False:
        return game()

MasterMind()

