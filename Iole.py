#!/usr/bin/env/python


# This file is meant to start execution, and perform the necessary tasks only if the parameter is a csv file
import json
import sys
import tree_init


def main(argv, func):
    output = ""

    if func == '1':
        output = tree_init.run(argv)
    elif func == '2':
        print("Not yet")
    else:
        print("Invalid argument, expected 1(Pairing) or 2(Expected Outcome)")
        exit(1)

# Execution start

main(sys.argv[1], sys.argv[2])






