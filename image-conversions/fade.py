# PROJECT 5
#
# Name: Tyra Krivonak
# Instructor: S. Einakian

import sys, math

# This function will return an output file called faded.ppm that fades a given image
def fade():

    # Try opening file. If no file exists, print error message
    # If provided last three arguments are not integers, raise an exception and print error message
    # Open faded file to write into    
    try:
        fin = open(sys.argv[1])
        fout = open('faded.ppm','w')
        row = int(sys.argv[2])
        col = int(sys.argv[3])
        rad = int(sys.argv[4])

        if sys.argv[2].isdigit() == False:
            raise exception

        if sys.argv[3].isdigit() == False:
            raise exception

        if sys.argv[4].isdigit() == False:
            raise exception
        
    except IOError:
        print('Unable to open', sys.argv[1])
        sys.exit()
        
    except:
##        print('Usage python3 fade.py', sys.argv[1], sys.argv[2], sys.argv[3])
        sys.exit()

    # Create new list and initialize
    # Read every line in file and append every line to new list
    # Write header for file
    lis = []
    for line in fin:
            lis.append(line)

    p = lis[0]
    widandhei = lis[1].split()
    wid = (widandhei[0])
    hei = (widandhei[1])
    mx = (lis[2])

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

    # Initialize scale, pixelcntx, and pixelcnty variables
    # Create a for loop to go through every element in L
    # Set pixelcntx to x%int(wid)
    # Set pixelcnty to x//int(wid)
    # Call scale function to determine fade number component using the row, col, rad, pixelcntx, and pixelcnty variables
    # Set scale variable to the result of the scale function that was called
    # Multiply every color component according to the scale that was found
    # Write to the outfile to record the color components of each point
    # Close all open files
    pixelcntx = pixelcnty = scale = 0 
    for x in range(len(L)):
        pixelcntx = x%int(wid)
        pixelcnty = x//int(wid)

        scale = scalefunc(row,col,rad,pixelcntx,pixelcnty)

        L[x][0] = int(L[x][0])*scale
        L[x][1] = int(L[x][1])*scale
        L[x][2] = int(L[x][2])*scale
                
        fout.write(str(L[x][0])+'\n')
        fout.write(str(L[x][1])+'\n')
        fout.write(str(L[x][2])+'\n')

    fin.close()
    fout.close()

# This function will calculate the scale factor of every pixel based on the distance from the point to the given center
# int -> float

# Calculate the distance by finding the difference of the each x and y components from the pixels and the given center and square it
# Calculate scale using the provided formula
# Determine if the scale is less than or equal to 0.2. If it is, set scale to 0.2 to determine the minimum and return
# If the scale is not less than 0.2, return the scale
def scalefunc(row,col,rad,pixelx,pixely):
    dist = math.sqrt(((pixelx - col)**2) + ((pixely - row)**2))
    scale = (rad - dist) / rad
    
    if scale <= 0.2:
        scale = 0.2
        return scale
    else:
        return scale

fade()
