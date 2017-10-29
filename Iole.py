#!/usr/bin/env/python


# This file is meant to start execution, and perform the necessary tasks only if the parameter is a csv file
import json
import sys
import file_init


def main(argv, func):
    output = file_init.run(argv, func)
    # output will be sent to the framework here


# Execution start
main(sys.argv[1], sys.argv[2])






