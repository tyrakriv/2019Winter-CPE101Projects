# PROJECT 5
#
# Name: Tyra Krivonak
# Instructor: S. Einakian

import sys

# This function will decode a given puzzle.ppm file into a new hidden.ppm file
def puzzle():

    # Try opening file. If no file exists, print error message
    # Open hidden file to write into
    try:
        fin = open(sys.argv[1])
        fout = open('hidden.ppm','w')

    except IOError:
        print('Unable to open', sys.argv[1])
        sys.exit()

    # Create new list and initialize
    # Read every line in file and append every line to new list
    # Write header for file
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

    # Create new list to go through groups of three
    # Go through entire list of file lines and create a list that stores the red, green, and blue components
    # If the the length of previous list is not 3, append the end components
    L = []   
    for i in range(1,len(lis)//3+1):
        if i*3+3 <= len(lis):
            L.append(lis[i*3:i*3+3])
        
        elif len(lis) % 3 > 0:        
            L.append(lis[i*3:len(lis)])

    # Create a for loop to go through every component in L list
    # Test if the red component of the point multiplied by ten is less than the maximum that the user provided
    # If it is, set all color components to the red component of the point multiplied by ten
    # If not, set all color components to the maximum value
    # Write each color component to the outfile
    # Close all open files
    for x in range(len(L)):
        
        if int(L[x][0]) * 10 <= int(mx):
            L[x][0] = L[x][1] = L[x][2] = int(L[x][0])*10
            
        else:
            L[x][0] = L[x][1] = L[x][2] = int(mx)
                
        fout.write(str(L[x][0])+'\n')
        fout.write(str(L[x][1])+'\n')
        fout.write(str(L[x][2])+'\n')

    fin.close()
    fout.close()


puzzle()
