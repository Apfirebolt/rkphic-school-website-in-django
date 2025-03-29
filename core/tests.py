from django.test import TestCase
from .models import Student, Teacher

class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            first_name="John",
            last_name="Doe",
            age=20,
            email="john.doe@example.com",
            phone_number="1234567890",
            address="123 Main St",
            roll_number="R001",
            enrollment_date="2023-01-01",
            current_class="10th Grade",
            guardian_name="Jane Doe",
            guardian_contact="0987654321",
            guardian_relationship="Mother",
            emergency_contact="1122334455"
        )
        Student.objects.create(
            first_name="Jane",
            last_name="Smith",
            age=22,
            email="jane.smith@example.com",
            phone_number="9876543210",
            address="456 Elm St",
            roll_number="R002",
            enrollment_date="2023-01-02",
            current_class="12th Grade",
            guardian_name="John Smith",
            guardian_contact="1231231234",
            guardian_relationship="Father",
            emergency_contact="5566778899"
        )

    def test_student_creation(self):
        student = Student.objects.get(roll_number="R001")
        self.assertEqual(student.first_name, "John")
        self.assertEqual(student.age, 20)
        self.assertEqual(student.current_class, "10th Grade")

    def test_student_update(self):
        student = Student.objects.get(roll_number="R002")
        student.age = 23
        student.save()
        updated_student = Student.objects.get(roll_number="R002")
        self.assertEqual(updated_student.age, 23)

    def test_student_deletion(self):
        student = Student.objects.get(roll_number="R001")
        student.delete()
        with self.assertRaises(Student.DoesNotExist):
            Student.objects.get(roll_number="R001")

    def test_student_list(self):
        students = Student.objects.all()
        self.assertEqual(students.count(), 2)


class TeacherTestCase(TestCase):
    def setUp(self):
        Teacher.objects.create(
            first_name="John",
            last_name="Doe",
            subject="Mathematics",
            email="john.doe@example.com",
            phone_number="1234567890",
            address="123 Main St",
            hire_date="2022-01-01",
            salary=50000.00
        )
        Teacher.objects.create(
            first_name="Jane",
            last_name="Smith",
            subject="Science",
            email="jane.smith.example.com",
            phone_number="9876543210",
            address="456 Elm St",
            hire_date="2022-01-02",
            salary=60000.00
        )

    def test_teacher_creation(self):
        teacher = Teacher.objects.get(email="john.doe@example.com")
        self.assertEqual(teacher.first_name, "John")
        self.assertEqual(teacher.subject, "Mathematics")
        self.assertEqual(teacher.salary, 50000.00)

    def test_teacher_update(self):
        teacher = Teacher.objects.get(email="jane.smith.example.com")
        teacher.salary = 65000.00
        teacher.save()
        updated_teacher = Teacher.objects.get(email="jane.smith.example.com")
        self.assertEqual(updated_teacher.salary, 65000.00)

    def test_teacher_deletion(self):
        teacher = Teacher.objects.get(email="john.doe@example.com")
        teacher.delete()
        with self.assertRaises(Teacher.DoesNotExist):
            Teacher.objects.get(email="john.doe@example.com")

    def test_teacher_list(self):
        teachers = Teacher.objects.all()
        self.assertEqual(teachers.count(), 2)


