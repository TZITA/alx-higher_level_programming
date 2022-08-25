#!/usr/bin/python3
import sys
if __name == "__main_":
    i = 0
    if len(sys.argv) == 2:
        print("{} argument:".format (len(sys.argv)))
        print("1: {}".format(sys.argv[1])) 
    elif sys.argv == 1:
        print("{} arguments.".format (len(sys.argv)))
    else:        
        print("{} arguments:".format (len(sys.argv)))
        while i < len(sys.argv):
            print("{}: {}".format((i + 1) ,sys.argv[i]))
            i += 1
