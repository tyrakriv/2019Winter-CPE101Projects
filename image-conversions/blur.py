# PROJECT 5
#
# Name: Tyra Krivonak
# Instructor: S. Einakian

import sys, math

# This function will take any given image and blur the image given parameters into a file named blur.ppm
def blur():

    # Try opening file. If no file exists, print error message
    # Open blur file to write into
    # Set blur to 4 if no argument is provided
    try:
        fin = open(sys.argv[1])
        fout = open('blur.ppm','w')
        if len(sys.argv) == 3:
            blur = int(sys.argv[2])
        else:
            blur = 4
 
    except IOError:
        print('Unable to open', sys.argv[1])
        sys.exit()

    # Create new list and initialize
    # Read every line in file and append every line to new list
    # Write header for file
    # Set width and height to an integer instead of string

    lis = []

    for line in fin:
            lis.append(line)

    p = lis[0]
    widandhei = lis[1].split()
    wid = widandhei[0]
    hei = widandhei[1]
    mx = lis[2]

    fout.write(p)
    fout.write(wid+' '+hei + '\n')
    fout.write(mx)

    wid = int(wid)
    hei = int(hei)

    # Create new list to go through groups of three
    # Go through entire list of file lines and create a list that stores the red, green, and blue components
    # If the the length of previous list is not 3, append the end components
    L = []
    for i in range(1,len(lis)//3+1):
        if i*3+3 <= len(lis):
            L.append(lis[i*3:i*3+3])
        
        elif len(lis) % 3 > 0:        
            L.append(lis[i*3:len(lis)])

    # Create a list that has elements with the length of the width and as long as the height

    colL = []
    for j in range(hei):
        colL.append(L[j*wid:j*wid+wid])

    # Go through every coordinate in list L
    # Set all variables to zero
    # Create a start variable that takes the index of the first coordinate to start at
    # If start is greater than zero, test if start is on correct row
    # If not, make start start on next row
    # If start is less than zero, make start equal to the coor%wid
    # Make startrow equal to the row the start begins at
    for coor in range(1,len(L)):
        red = gre = blu = avgred = avggre = avgblu = start = startrow= 0
        start = coor - wid*blur - blur

        if start > 0:
            if (start // wid) + 2 != (coor //wid):
               start =  coor - blur*wid  
        
        if start < 0:
            start = coor% wid

        startrow = start//wid

    # Create a for loop to go through every row based on blur*2+1
    # Set row equal to the start // wid and increment by one each time the for loop completes
    # Create a second for loop to go through every column based on blur*2+1
    # Make column equal to the start - (wid*startrow) and increment every time the for loop is executed
    # Check if row is greater than the height. If it is, set row to start// wid
    # Check if col is greater than the width. If it is, set col equal to wid - 1 - y
    # Increment the red, green, blue, values by every points red, green, blue values
    # After every value is added, divide every color component by (2*blur+1)**2
    # Write the final color components to outfile
    # Close all files
        for x in range(blur*2+1):
            row = start//wid + x
            for y in range(blur*2+1):
                col = start-(wid*startrow)+ y
                if row >= hei:
                    row = start//wid
                if col >= wid:
                    col = wid - 1 - y

                red+=int(colL[row][col][0])
                gre+=int(colL[row][col][1])
                blu+=int(colL[row][col][2])

        avgred = red / (2*blur+1)**2
        avggre = gre / (2*blur+1)**2
        avgblu = blu / (2*blur+1)**2

        fout.write(str(int(avgred))+'\n')
        fout.write(str(int(avggre))+'\n')
        fout.write(str(int(avgblu))+'\n')

    fin.close()
    fout.close()    

blur()
