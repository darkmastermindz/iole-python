
# Gets raw string from a csv format and parses it into a hash
import tree
import regression


def run(str_csv, func):
    arr = str_csv.split("\n") # this returns an array where the first column is just labels
    student_hash = {}
    index = 1 # skip first index
    while index < len(arr) - 1:
        to_hash = arr[index].split(",")
        id = to_hash[0]
        student_hash[id] = "" # hash based on student ID
        to_hash.remove(id)
        student_hash[id] = to_hash
        index += 1

    if func == '1':
        return tree.run(student_hash)
    elif func == '2':
       return regression.run(student_hash) # will later return the result from linear regression
    else:
        print("Invalid argument, expected 1(Pairing) or 2(Expected Outcome)")
        exit(1)
