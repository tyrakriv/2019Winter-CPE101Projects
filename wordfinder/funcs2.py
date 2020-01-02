# Project 3 - Word Puzzle
# 
# Name: Aine Larkin and Tyra Krivonak
# Instructor: S. Einakian
# Section: 9

'''
Some of the suggested functions are shown bellow.
You can create as many functions as you need. 
You can even ignore the suggested functions.
But you are not allow to write the whole project in One Function!
'''
def main():

    print('This program will read a 100 character long string and create a puzzle')

    #1) gets input for puzzle
    userWords = input("Enter words: ")
    userInput = input("Enter string: ")

    # makes user's words into list
    listW = sliceWords(userWords)

    # print puzzle
    makePuzzle(userInput)

    # makes rows of puzzle into list
    listRow = makeInputRows(userInput)

    ######CHANGED#######
    for i in range(len(listW)):
        notFound = 0
        for j in range(10):
            colF = checkForward(listW[i], listRow[j])
            colB = checkBackward(listW[i], listRow[j])
            ret = checkForBack(listW[i], listRow[j])
    
            if ret == 1:
                print (listW[i],": (FORWARD) row: ",j, "column:", colF)

            if ret == 2:
                print(listW[i],": (BACKWARD) row: ",j, "column:", colB)

            if ret == 0:
                notFound += 1
                
        if notFound != 9:
            print(listW[i],': word not found')
    ######UPTOHERE########
            
    for i in range(len(listW)):
        up = checkUp(listW[i], userInput)
        down = checkDown(listW[i], userInput)
        if(up):
            print(str(listW[i]),'Up')
        elif(down):
            print(str(listW[i]),'Down')
        else:
            print(str(listW[i]),'None')

######CHANGED#######
def checkForBack(word, row):
    # check if word is forward for each
    forward = checkForward(word, row)
    backward = checkBackward(word, row)
    if forward <= 9 and forward >= 0:
        r = 1
        return r
    if backward <= 9 and backward >= 0:
        r = 2
        return r
    r = 0
    return r
######UPTOHERE#######

def makePuzzle(userInput):
    for i in range (0, 100, 10):
        print (userInput[i:i+10])

def makeInputRows(userInput):
    listRow = []
    for i in range (10):
        num = i*10
        listRow.append(userInput[num:num+10])
    return listRow
        
    
def sliceWords(userWords):
    #splits given words into separate strings in a list
    listW = []
    listW = userWords.split()
    return listW

######CHANGED#######
#2) checks forward for given word        
def checkForward(word, row):    
    #checks if word is in input
    col = -1
    for i in range(10):
        if (word[0] == row[i]):
            num = len(word)
            new = row[i:i+num]
            if word == new:
                col = i
                return col
    return col         
        
#3) checks backward for given word
def checkBackward(word, row):
    listW = []
    listC = []
    for j in range(len(word)-1,-1,-1):
        listW.append(word[j])
    for i in range(10):
        if (word[-1] == row[i]):
            if len(word)+i < 10:
                col = i + len(word) -1
                for j in range (len(word)):
                    if (word[-(j+1)] == row[i+j]):
                        listC.append(row[i+j])
    if listW == listC:
        return col
    else:
        col = -1
        return col
######UPTOHERE#######

    
# I first set the countR and col and row, whcih will be used later to determine where the word is in the puzzle
#The for loop starts at the end of the puzzle and works its way up backwards
#the if statement checks if each letter in the puzzle is the same as the first letter in one of the words
#4) checks up for given word
def checkUp(word, puzzle):
    countR = 9
    col = row = 0

    for i in range(99,-1,-1):
        if (i%10 ==0):
            countR -= 1
        if (word[0] == puzzle[i]):
            l = 0
            count = 0
            if (i - (len(word)*10) > -10):
                for i in range (i, i - (len(word)*10), -10):
                    if (word[l] == puzzle[i]):
                        count += 1
                        l += 1
                if (count == len(word)):
                    return True
                    row = countR
                    col = i%10
                    #print (row, col)

#5) checks down for given word
def checkDown(word,puzzle):
    countR = -1
    col = row = 0

    for i in range(99):
        if (i%10 == 0):
            countR +=1
        if (word[0] == puzzle[i]):
            l = 0
            count = 0
            if (i + len(word)*10 < 110):
                for i in range(i,i+(len(word)*10), 10):
                    if word[l] == puzzle[i]:
                        count += 1
                        l += 1
                if (count == len(word)):
                    return True
                    row = countR
                    col = i%10
                    #print (row, col)
                else:
                    return False
        
            

if __name__ == '__main__':
   main()
