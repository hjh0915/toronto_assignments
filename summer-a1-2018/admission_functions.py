"""Starter code for Assignment 1 CSC108 Summer 2018"""

SPECIAL_CASE_SCHOOL_1 = 'Fort McMurray Composite High'
SPECIAL_CASE_SCHOOL_2 = 'Father Mercredi High School'
SPECIAL_CASE_YEAR = '2017'
# Add other constants here
NE = 'NE'
SCHOLARSHIP = 88.0

def is_special_case(record: str) -> bool:
    """Return True iff the student represented by record is 
    a special case.

    >>> is_special_case('Jacqueline Smith,Fort McMurray Composite High,2017,MAT,90,94,ENG,92,88,CHM,80,85,BArts')
    True
    >>> is_special_case('Jacqueline Smith,Father Something High School,2017,MAT,90,94,ENG,92,88,CHM,80,85,BArts')
    False
    >>> is_special_case('Jacqueline Smith,Fort McMurray Composite High,2015,MAT,90,94,ENG,92,88,CHM,80,85,BArts')
    False
    """
    
    x = record.split(',')
    school = (SPECIAL_CASE_SCHOOL_1, SPECIAL_CASE_SCHOOL_2)
    return x[1] in school and x[2] == SPECIAL_CASE_YEAR

def get_final_mark(record: str, course_mark: str, exam_mark: str) -> float:
    """Return the student's final mark in the course.

    >>> get_final_mark('Jacqueline Smith,Fort McMurray Composite High,2017,MAT,90,94,ENG,92,88,CHM,80,85,BArts', 'MAT,90', 'MAT,94')
    92.0
    >>> get_final_mark('Jacqueline Smith,Fort McMurray Composite High,2017,MAT,90,94,ENG,92,87,CHM,80,NE,BArts', 'ENG,92', 'ENG,87')
    89.5
    """
    
    if exam_mark == NE:
        return float(course_mark)
    else:
        return (float(course_mark) + float(exam_mark)) / 2

def get_both_marks(record: str, course_code: str) -> str:
    """Return the coursework mark and the exam mark separated
    by a single space.

    >>> get_both_marks('Jacqueline Smith,Fort McMurray Composite High,2017,MAT,90,94,ENG,92,88,CHM,80,85,BArts', 'MAT')
    '90 94'
    >>> get_both_marks('Tom,Fort McMurray Composite High,2017,MAT,90,94,ENG,92,88,CHM,90,NE,BArts', 'CHM')
    '90 NE'
    """

    if course_code in record:
        x = record.split(',')
        start = x.index(course_code) + 1
        end = x.index(course_code) + 2
        return x[start] + ' ' + x[end] 
    else:
        return ''

def extract_course(transcrip: str, course: int) -> str:
    """Return one course in the transcrip.

    >>> extract_course('MAT,90,94,ENG,92,88,CHM,80,85', 1)
    'MAT,90,94'
    >>> extract_course('MAT,90,94,ENG,92,88,CHM,80,NE', 3)
    'CHM,80,NE'
    """

    x1 = transcrip[0:9]
    x2 = transcrip[10:19]
    x3 = transcrip[20:]
    if course == 1:
        return x1
    elif course == 2:
        return x2
    else:
        return x3

def applied_to_degree(record: str, degree: str) -> bool:
    """ Return True if and only if th student represented by 
    the first parameter applied to the degree represented by 
    the second parameter.

    >>> applied_to_degree('Jacqueline Smith,Fort McMurray Composite High,2017,MAT,90,94,ENG,92,88,CHM,80,85,BArts', 'BArts')
    True
    >>> applied_to_degree('Tom,Fort McMurray Composite High,2017,MAT,90,94,ENG,92,88,CHM,90,NE,BArts', 'Bsci')
    False
    """

    return record.split(',')[-1] == degree
    
def decide_admission(average: float, cutoff: float) -> str:
    """Return 'accept' if the average is at least the cutoff 
    but below the threshold for a scholarship, and 'reject'
    if the average is below the cutoff.

    >>> decide_admission(84.5, 80.0)
    'accept'
    >>> decide_admission(90.5, 80.0)
    'accept with scholarship'
    >>> decide_admission(79.5, 80.0)
    'reject'
    """

    if average < cutoff:
        return 'reject'
    elif average >= SCHOLARSHIP:
        return 'accept with scholarship'
    else:
        return 'accept'