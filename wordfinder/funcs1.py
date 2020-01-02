# Project 3 - Word Puzzle
# 
# Name: Tyra Krivonak and Aine Larkin
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

    # check if word is forward for each
    for i in range(len(listW)):
        for j in range(10):
            forward = checkForward(listW[i], listRow[j])
            backward = checkBackward(listW[i], listRow[j])
            if (forward):
                print(str(listW[i]),'Forward')
            elif backward:
                print(str(listW[i]),'Backward')
            else:
                print(str(listW[i]),'None')
            

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

#2) checks forward for given word        
def checkForward(word, row):
    #checks if word is in input
    for i in range(10):
        if (word[0] == row[i]):
            num = len(word)
            new = row[i:i+num]
            if word == new:
                return True
        
#3) checks backward for given word
def checkBackward(word, row):
    listW = []
    listC = []
    for j in range(len(word)-1,-1,-1):
        listW.append(word[j])
    for i in range(10):
        if (word[-1] == row[i]):
            if len(word)+i < 10:
                for j in range (len(word)):
                    if (word[-(j+1)] == row[i+j]):
                        listC.append(row[i+j])
    if listW == listC:
        return True
        

#4) checks up for given word

#5) checks down for given word

if __name__ == '__main__':
   main()
