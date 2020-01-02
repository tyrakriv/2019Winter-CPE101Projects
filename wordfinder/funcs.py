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
#This function will return a value to the main function to determine if the word is forward or backward
#str and int -> int
#get return value from checkforward and checkbackward
#check if return value from forward is between 9 and 0
#- if it does, return 1
#check if return value from backward is between 9 and 0
#- if it does, return 2
#if return values don't meet anything, return 0
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

#make puzzle and print
#str -> none
#go through entire 100 letter string and increment by 10
#print each row with ten letters
def makePuzzle(userInput):
    for i in range (0, 100, 10):
        print (userInput[i:i+10])
    print()

#makes list for string
#str -> list
#create listRow list
#go through puzzle and create list
#return list
def makeInputRows(userInput):
    listRow = []
    for i in range (10):
        num = i*10
        listRow.append(userInput[num:num+10])
    return listRow
        
#splits user words into list
#str -> list
#create list
#use split function to make new list
#return list
def sliceWords(userWords):
    listW = []
    listW = userWords.split()
    return listW

#checks if word is forward in every line
#str and int -> int
#set new variable to -1 (col)
#make loop to go through every row in puzzle
#check if first letter of word is in row
#make a new string between intervals of i and i plus the length of a word
#check if word is equal to new string and if it does, return column number
#if word is not equal, return -1
def checkForward(word, row):    
    col = -1
    for i in range(10):
        if (word[0] == row[i]):
            num = len(word)
            new = row[i:i+num]
            if word == new:
                col = i
                return col
    return col         
        
#checks backward for given word
#str and int -> int
#makes two new lists
#create list for new backward word using loop
#create loop to go through each row
#if the last letter of word is found and if the length of the word plus column is less than ten:
#create a loop to make a list of all letters
#see if the two lists match and if they do, return column number. If not, return -1.
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


    
# I first set the countR and col and row, which will be used later to determine where the word is in the puzzle
#The for loop starts at the end of the puzzle and works its way up backwards
#the if statement checks if each letter in the puzzle is the same as the first letter in one of the user-inputed words
#if the letters are the same and within the range of the puzzle, it then moves up the puzzle for the length of the word
#if the length of the word in the puzzle is the same as the user-inputed word and they match, then the row and column of the first letter are returned


#4) This function checks up for given word
# str -> int
def checkUp(word, puzzle):
    countR = 9
    colU = rowU = 0

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
                    row = countR
                    col = i%10
                    row = str(row)
                    col = str(col)
                    return row, col
                    #print(word, "(UP) row:",row,"colomn:",col)


# I first set the countR and col and row, which will be used later to determine where the word is in the puzzle
#The for loop starts at the end of the puzzle and works its way up forwards
#the if statement checks if each letter in the puzzle is the same as the first letter in one of the user-inputed words
#if the letters are the same and within the range of the puzzle, it then moves down the puzzle for the length of the word
#if the length of the word in the puzzle is the same as the user-inputed word and they match, then the row and column of the first letter are returned

#5) This function checks down for given word
# str -> int
def checkDown(word,puzzle):
    countR = -1
    col = row = -1

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
                    row = countR
                    col = i%10
                    row = str(row)
                    col = str(col)
                    return row, col
              

