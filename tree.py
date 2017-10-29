
# This class is meant to take in a hash and perform Tree Based Modeling to split students into smaller hashes


# Will classify students  based on their topic strength
def run(student_hash):

    ids = student_hash.keys()

    build = [] # eventually should look like: [[group1, group2, group3], [...,....,....]]
    num_topics = calc_num_topics(student_hash,ids)

    tree = branch(student_hash,ids,build, num_topics)

    return tree


'''
helper method for recursion; takes in a hash of a student group
'''
'''
def branch(student_hash, ids, build, num_topics ,index = 0):
    if index >= len(ids): # should stop recursion upon reaching the last index of the student hash
        return build
    elif index == 0:
        new_group = Group()
        manage_group(group, )
    else:
        build.append[]



def manage_group(group, ):
'''

def calc_num_students(ids):
    return len(ids)

def calc_num_topics(student_hash, ids):
    return len(student_hash[ids[0]]) / 2 # number of topics should be half the array size

def get_scores(student_hash, ids):
    score_arr = []
    i = 0
    while i < calc_num_students(ids):
        score_arr.append()

    return score_arr

class Group:

    def __init__(self):
        self.__students = [] # initialize group as an empty hash

    '''
    appends a student to the end of the group
    '''
    def add(self, s_id):
        self.__students.append(s_id)

    '''
    always removes the first student, if any
    '''
    def remove(self, s_id):
        if empty(self):
            return False

        student = self.__students[0]
        self.__students.pop(0)

        return student

    def present(self):
        return self.__students

    def empty(self):
        return len(self.__students) == 0



