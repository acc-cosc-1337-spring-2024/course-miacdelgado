# Will produce set of students from both classes
prog1 = set(['Student1', 'Student2', 'Student3'])
prog2 = set(['Student3', 'Student4', 'Student5'])

def get_students_who_took_prog1_and_prog2(prog1, prog2):
    return prog1.intersection(prog2)

# Will produce set of students who took either 1 class
def get_students_who_took_prog1_or_prog2(prog1, prog2):
    return prog1.union(prog2)

# Will produce set of students from only prog1
def get_students_who_took_prog1_not_prog_2(prog1, prog2):
    return prog1.difference(prog2)

# Will produce set of students from only prog2
def get_students_who_took_prog2_not_prog_1(prog1, prog2): 
    return prog2.difference(prog1)