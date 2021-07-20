import unittest
import admission_functions

class TestAdmission(unittest.TestCase):
    def test_01(self):
        record = 'Jacqueline Smith,Fort McMurray Composite High,2017,MAT,90,94,ENG,92,88,CHM,80,85,BArts'
        print(admission_functions.is_special_case(record))
        record = 'Jacqueline Smith,Father Something High School,2017,MAT,90,94,ENG,92,88,CHM,80,85,BArts'
        print(admission_functions.is_special_case(record))

    def test_02(self):
        record = 'Jacqueline Smith,Fort McMurray Composite High,2017,MAT,90,94,ENG,92,88,CHM,80,85,BArts'
        work_mark = '90'
        exam_work = '94'
        x = 92.0
        self.assertEqual(admission_functions.get_final_mark(record,work_mark,exam_work), x)
 
    def test_03(self):
        record = 'Jacqueline Smith,Fort McMurray Composite High,2017,MAT,90,94,ENG,92,88,CHM,80,85,BArts'
        course_code = 'MAT'
        x = '90 94'
        self.assertEqual(admission_functions.get_both_marks(record,course_code), x)
        record = 'Tom,Fort McMurray Composite High,2017,MAT,90,94,ENG,92,88,CHM,90,NE,BArts'
        course_code = 'CHM'
        y = '90 0'
        self.assertEqual(admission_functions.get_both_marks(record,course_code), y)

    def test_04(self):
        transcrip = 'MAT,90,94,ENG,92,88,CHM,80,85'
        course = 1
        x = 'MAT,90,94'
        self.assertEqual(admission_functions.extract_course(transcrip,course), x)
        transcrip = 'MAT,90,94,ENG,92,88,CHM,80,NE'
        course = 3
        y = 'CHM,80,NE'
        self.assertEqual(admission_functions.extract_course(transcrip,course), y)

    def test_05(self):
        record = 'Tom,Fort McMurray Composite High,2017,MAT,90,94,ENG,92,88,CHM,90,NE,BSci'
        degree = 'BArts'
        x = False
        self.assertEqual(admission_functions.applied_to_degree(record,degree), x)
        record = 'Tom,Fort McMurray Composite High,2017,MAT,90,94,ENG,92,88,CHM,90,NE,BSci'
        degree = 'BArts'
        y = True
        self.assertEqual(admission_functions.applied_to_degree(record,degree), x)

    def test_06(self):
        average = 264.5
        cutoff = 200.0
        x = 'accept'
        self.assertEqual(admission_functions.decide_admission(average,cutoff), x)
        average = 350.5
        cutoff = 200.0
        y = 'accept with scholarship'
        self.assertEqual(admission_functions.decide_admission(average,cutoff), y)
        average = 179.5
        cutoff = 210.0
        z = 'reject'
        self.assertEqual(admission_functions.decide_admission(average,cutoff), z)

unittest.main()