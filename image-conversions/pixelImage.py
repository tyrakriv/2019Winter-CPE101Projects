# PROJECT 5
#
# Name: Tyra Krivonak
# Instructor: S. Einakian

import sys, blur, fade, puzzle

# This main function will execute the blur, fade, or puzzle files depending on the length of the given command
def main():

    length = len(sys.argv)

    if length == 2:
        puzzle.puzzle()

    elif length == 5:
        fade.fade()
        
    elif length == 3:
        blur.blur()

    else:
        print('Wrong number of arguments')
        sys.exit()

main()
