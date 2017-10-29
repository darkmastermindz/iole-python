
# This file is meant take in a csv and parse it into a string
import hash_generator


def run(argv, func):
    address = argv  # set address to be the first parameter
    # should not execute if file address is not a valid one
    valid = False
    try:
        csv = open(address, 'r')
        valid = True
    except IOError:
        print("File does not exist; ")
        valid = False

    if not valid or not address.endswith(".csv"):
        print("Invalid file")
        exit(1)

    str_csv = ""

    for line in csv:
        str_csv += line

    # check which operation was selected
   # if func == '1':
    return hash_generator.run(str_csv, func)
    # elif func == '2':
       # print("Not yet") # will later return the result from linear regression
    # else:
       # print("Invalid argument, expected 1(Pairing) or 2(Expected Outcome)")
      #  exit(1)


