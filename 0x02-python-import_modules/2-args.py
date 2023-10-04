#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    for i in range(0, len(sys.argv)):
        if len(sys.argv) - 1 == 0:
            print("0 arguments.")
            break
        print("{} arguments:".format(len(sys.argv) - 1))
        if len(sys.argv) - 1 > 0 and i >= 1:
            print("{}: {}".format(i, sys.argv[i]))


