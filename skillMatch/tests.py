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


def create_student(name, bio, id, sex):
    return Student.objects.create(name=name, bio=bio, computing_id=id, sex=sex)
