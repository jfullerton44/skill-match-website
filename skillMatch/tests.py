from django.test import TestCase
from .models import Student, Class, Skill


class TestTest(TestCase):
    def test_easy(self):
        self.assertEqual(1, 1)
    # def test_false(self):
    #     self.assertEqual(1,2)


class StudentModelTests(TestCase):
    def test_student_created(self):
        name = "John Smith"
        bio = "hello i am a student"
        id = "js3fe"
        sex = "M"
        test_student = Student(name=name, bio=bio, computing_id=id, sex=sex)
        self.assertIsInstance(test_student, (Student))

    def test_insert_student(self):
        name = "John Smith"
        bio = "hello i am a student"
        id = "js3fe"
        sex = "M"
        test_student = Student(name=name, bio=bio, computing_id=id, sex=sex)
        create_student(name, bio, id, sex)
        student = Student.objects.get(computing_id="js3fe")
        self.assertEqual(student.name, "John Smith")

    def test_insert_bad_student(self):
        bio = "hello i am a student"
        id = "jf8he"
        sex = "M"
        create_student("", bio, id, sex)
        with self.assertRaises(Exception):
            Student.objects.get(computing_id="js3fe")

    def test_insert_same_computing_id(self):
        name = "John Smith"
        bio = "hello i am a student"
        id = "jf8he"
        sex = "M"
        create_student(name, bio, id, sex)
        with self.assertRaises(Exception):
            create_student("Second Student", bio, id, sex)

    def test_insert_student_same_name(self):
        name = "John Smith"
        bio = "hello i am a student"
        id = "jf8he"
        sex = "M"
        create_student(name, bio, id, sex)
        create_student(name, bio, "aa2aa", sex)
        student = Student.objects.get(computing_id="jf8he")
        self.assertEqual(student.name, "John Smith")
        student = Student.objects.get(computing_id="aa2aa")
        self.assertEqual(student.name, "John Smith")

class ClassModelTests(TestCase):
    def test_class_created(self):
        prefix = "CS"
        course_number = "2150"
        professor = "Aaron Bloomfield"
        semester = "F19"
        test_class = Class(prefix=prefix, course_number=course_number, professor=professor, semester=semester)
        self.assertIsInstance(test_class, (Class))

    def test_insert_class(self):
        prefix = "CS"
        course_number = "2150"
        professor = "Aaron Bloomfield"
        semester = "F19"
        test_class = create_class(prefix=prefix, course_number=course_number, professor=professor, semester=semester)
        clas = Class.objects.get(professor="Aaron Bloomfield")
        self.assertEqual(clas.semester, "F19")

    def test_find_bad_class(self):
        prefix = "CS"
        course_number = "2150"
        professor = "Aaron Bloomfield"
        semester = "F19"
        test_class = create_class(prefix=prefix, course_number=course_number, professor=professor, semester=semester)
        clas = Class.objects.filter(professor__icontains="bob")
        self.assertEqual(0, len(clas))

def create_student(name, bio, id, sex):
    return Student.objects.create(name=name, bio=bio, computing_id=id, sex=sex)

def create_class(prefix, course_number, professor, semester):
    return Class.objects.create(prefix=prefix, course_number=course_number, professor=professor, semester=semester)