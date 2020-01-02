# Project 3 - Word Puzzle
# 
# Name: Aine Larkin and Tyra Krivonak
# Instructor: S. Einakian
# Section: 9

from funcs import *

def main():

    print('This program will read a 100 character long string and create a puzzle')

    #1) gets input for puzzle
    userWords = input("Enter words: ")
    userInput = input("Enter string: ")
    print()

    # makes user's words into list
    listW = sliceWords(userWords)

    # print puzzle
    makePuzzle(userInput)

    # makes rows of puzzle into list
    listRow = makeInputRows(userInput)

    # set default list
    newList = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    newList2 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

    # go through list of words
    for i in range(len(listW)):
        notFound = 0
        # go through rows
        for j in range(10):
            colF = checkForward(listW[i], listRow[j])
            colB = checkBackward(listW[i], listRow[j])
            checkUp(listW[i], userInput)
            checkDown(listW[i], userInput)
            ret = checkForBack(listW[i], listRow[j])

            # check if the word is found forward or backward then print
            if ret == 1:
                print (listW[i],": (FORWARD) row: ",j, "column:", colF)

            if ret == 2:
                print(listW[i],": (BACKWARD) row: ",j, "column:", colB)

            if ret == 0:
                notFound += 1

        # create new list        
        if notFound != 9:
            newList[i] = 0
    
    # create loop to go through each word            
    for x in range(len(listW)):
        up = checkUp(listW[x], userInput)
        down = checkDown(listW[x], userInput)
        ret = checkUp(listW[x], userInput)
        ret2 = checkDown(listW[x], userInput)
        # check if word is found up or down then print
        if (up):
            print(str(listW[x]),':(UP) row:',ret[0],'column:', ret[1])
        elif (down):
            print(str(listW[x]),':(DOWN) row:',ret2[0],'column:', ret2[1])
        # create list2 if not found
        else:
            newList2[x]= 0

    # go through list of words
    for z in range(len(listW)):
        # check if word is not found for forward, backward, up, or down, then print word not found
        if newList[z] == 0 and newList2[z] == 0:
            print(listW[z],': word not found')

if __name__ == '__main__':
   main()
