from django.test import TestCase
from .models import Student, Class, Skill
from django.contrib.auth.models import User
from .templatetags.extras import common, mutual

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
        test_student = Student(name=name, bio=bio, sex=sex)
        self.assertIsInstance(test_student, (Student))

    def test_insert_student(self):
        name = "John Smith"
        bio = "hello i am a student"
        id = "js3fe"
        sex = "M"
        test_student = Student(name=name, bio=bio, sex=sex)
        create_student(name, bio, sex)
        student = Student.objects.get(name="John Smith")
        self.assertEqual(student.name, "John Smith")

    def test_search_no_case(self):
        name = "John Smith"
        bio = "hello i am a student"
        id = "js3fe"
        sex = "M"
        test_student = Student(name=name, bio=bio, sex=sex)
        create_student(name, bio, sex)
        student = Student.objects.filter(name__icontains="jOhN")
        self.assertIsNotNone(student)

    def test_good_user(self):
        user = "jjjj"
        User.objects.create(username=user)
        self.assertIsNotNone(User.objects.get(username="jjjj"))

    def test_no_user(self):
        user = ""
        User.objects.create(username=user)
        with self.assertRaises(Exception):
            User.objects.get(username="jjjj")

    def test_insert_bad_student(self):
        bio = "hello i am a student"
        id = "jf8he"
        sex = "M"
        create_student("", bio, sex)
        with self.assertRaises(Exception):
            Student.objects.get(computing_id="js3fe")

    def test_insert_bad_student2(self):
        bio = "hello i am a student"
        id = "jf8he"
        sex = "M"
        create_student("", bio, sex)
        with self.assertRaises(Exception):
            Student.objects.get(computing_id="")

    def test_insert_same_computing_id(self):
        name = "John Smith"
        bio = "hello i am a student"
        id = "jf8he"
        sex = "M"
        create_student(name, bio, sex)
        with self.assertRaises(Exception):
            create_student("Second Student", bio, id, sex)

    # def test_insert_student_same_name(self):
    #     name = "John Smith"
    #     bio = "hello i am a student"
    #     id = "jf8he"
    #     sex = "M"
    #     create_student(name, bio, sex)
    #     create_student(name, bio, sex)
    #     student = Student.objects.get(computing_id="jf8he")
    #     self.assertEqual(student.name, "John Smith")
    #     student = Student.objects.get(computing_id="aa2aa")
    #     self.assertEqual(student.name, "John Smith")

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

    def test_find_class_no_case(self):
        prefix = "CS"
        course_number = "2150"
        professor = "Aaron Bloomfield"
        semester = "F19"
        test_class = create_class(prefix=prefix, course_number=course_number, professor=professor,
                                  semester=semester)
        clas = Class.objects.filter(professor__icontains="aaron")
        self.assertNotEqual(0, len(clas))

    def test_find_class_no_case_lastname(self):
        prefix = "CS"
        course_number = "2150"
        professor = "Aaron Bloomfield"
        semester = "F19"
        test_class = create_class(prefix=prefix, course_number=course_number, professor=professor,
                                  semester=semester)
        clas = Class.objects.filter(professor__icontains="bLOOm")
        self.assertNotEqual(0, len(clas))

class SkillModelTests(TestCase):
	def test_Skill_created(self):
		name = "blob"
		test_Skill = Skill(name=name)
		self.assertIsInstance(test_Skill, (Skill))

	def test_insert_Skill(self):
		name = "blob"
		test_Skill = create_skill(name=name)
		clas = Skill.objects.get(name="blob")
		self.assertNotEqual(clas, None)

	def test_find_bad_Skill(self):
		name = "blob"
		test_Skill = create_skill(name=name)
		clas = Skill.objects.filter(name__icontains="bosadsadb")
		self.assertEqual(0, len(clas))

	def test_find_Skill_no_case(self):	
		name = "blob"
		test_Skill = create_skill(name=name)
		clas = Skill.objects.filter(name__icontains="blob")
		self.assertNotEqual(0, len(clas))

class TemplateTagsTests(TestCase):
    def test_mutual_negative(self):
        test_user_a = User.objects.create_user('john smith', '', 'jsmith1')
        test_user_b = User.objects.create_user('jane smith', '', 'jsmith2')
        self.assertEqual(0, mutual(test_user_a.student, test_user_b.student))
    def test_mutual_positive(self):
        test_user_a = User.objects.create_user('john smith', '', 'jsmith1')
        test_user_b = User.objects.create_user('jane smith', '', 'jsmith2')
        test_user_c = User.objects.create_user('joel smith', '', 'jsmith3')
        test_user_a.student.friends.add(test_user_c.student)
        test_user_b.student.friends.add(test_user_c.student)
        self.assertEqual(1, mutual(test_user_a.student, test_user_b.student))

    def test_common_negative(self):
        test_user_a = User.objects.create_user('john smith', '', 'jsmith1')
        test_user_b = User.objects.create_user('jane smith', '', 'jsmith2')
        self.assertEqual(0, common(test_user_a.student, test_user_b.student))
    def test_common_positive(self):
        test_user_a = User.objects.create_user('john smith', '', 'jsmith1')
        test_user_b = User.objects.create_user('jane smith', '', 'jsmith2')
        test_class = create_class(prefix="CS", course_number="2150", professor="Floryan", semester="F19")
        test_user_a.student.classes.add(test_class)
        test_user_b.student.classes.add(test_class)
        self.assertEqual(1, common(test_user_a.student, test_user_b.student))

def create_student(name, bio, sex):
    return Student.objects.create(name=name, bio=bio, sex=sex)

def create_skill(name):
	return Skill.objects.create(name=name)

def create_class(prefix, course_number, professor, semester):
    return Class.objects.create(prefix=prefix, course_number=course_number, professor=professor, semester=semester)