
# This file is meant take in a csv and parse it into a string
import hash_generator


def run(argv):
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

    # we need to send this back to the json
    return hash_generator.run(str_csv)


