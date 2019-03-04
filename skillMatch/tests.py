from django.test import TestCase
from .models import Student, Class,Skill

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
        sex ="M"
        test_student= Student(name=name,bio=bio,computing_id=id,sex=sex)
        self.assertIsInstance(test_student,(Student))

    def test_insert_student(self):
        name = "John Smith"
        bio = "hello i am a student"
        id = "js3fe"
        sex = "M"
        test_student= Student(name=name,bio=bio,computing_id=id,sex=sex)
        create_student(name,bio,id,sex)
        student = Student.objects.get(computing_id="js3fe")
        self.assertEqual(student.name,"John Smith")

    def test_insert_bad_student(self):
        bio = "hello i am a student"
        id = "jf8he"
        sex = "M"
        test_student= Student(bio=bio,computing_id=id,sex=sex)
        create_student("",bio,id,sex)
        #self.assertRaises(Student.objects.get(computing_id="js3fe"))

def create_student(name,bio,id,sex):
    return Student.objects.create(name=name,bio=bio,computing_id=id,sex=sex)

