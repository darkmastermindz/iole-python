
# Gets raw string from a csv format and parses it into a hash

def run(str_csv):
    arr = str_csv.split("\n") # this returns an array where the first column is just labels
    student_hash = {}
    index = 1 # skip first index
    while index < len(arr) - 1:
        to_hash = arr[index].split("\t")
        id = to_hash[0]
        student_hash[id] = "" # hash based on student ID
        to_hash.remove(id)
        student_hash[id] = to_hash
        index += 1

    print(student_hash)