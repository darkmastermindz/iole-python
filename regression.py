
# should return a hash with the average values on its first index, then individual scores on each other index


def run(student_hash):
    ids = student_hash.keys()
    num_questions = calc_num_questions(student_hash, ids)
    build = []
    avg_hash = get_avg_hash(student_hash, 1, num_questions, []) #answers should be found on odd numbers
   # print(avg_hash)


def calc_num_questions(student_hash, ids):
    return len(student_hash[ids[0]]) / 2


def get_avg_hash(student_hash, answer, num_questions, avg_hash):
    if answer <= num_questions:
        avg_hash.append(calc_avg(student_hash, answer))
        answer += 2
        get_avg_hash(student_hash, answer, num_questions, avg_hash)
    else:
        print(avg_hash)
        return avg_hash[:]


def calc_avg(student_hash, answer):
    sum = 0
    for arr in student_hash:
        sum += float(student_hash[arr][answer])

    return sum / len(student_hash)
