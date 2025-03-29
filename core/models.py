from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    roll_number = models.CharField(max_length=20, unique=True)
    enrollment_date = models.DateField()
    current_class = models.CharField(max_length=50)
    guardian_name = models.CharField(max_length=100)
    guardian_contact = models.CharField(max_length=15)
    guardian_relationship = models.CharField(max_length=50)
    emergency_contact = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def __repr__(self):
        return f"Student({self.first_name}, {self.last_name}, {self.current_class}, {self.emergency_contact})"
    
    class Meta:
        verbose_name_plural = "Students"
        ordering = ['last_name', 'first_name']
        db_table = 'student_records'
        
    

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def __repr__(self):
        return f"Teacher({self.first_name}, {self.last_name}, {self.subject}, {self.salary})"
    
    class Meta:
        verbose_name_plural = "Teachers"
        ordering = ['last_name', 'first_name']
        db_table = 'teacher_records'


class Notification(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    recipient = models.CharField(max_length=100, null=True, blank=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return f"Notification({self.title}, {self.recipient})"
    
    class Meta:
        verbose_name_plural = "Notifications"
        ordering = ['-date_created']
        db_table = 'notification_records'


class Class(models.Model):
    class_name = models.CharField(max_length=100)
    class_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name='classes')
    
    def __str__(self):
        return self.class_name
    
    class Meta:
        verbose_name_plural = "Classes"
        ordering = ['class_name']
        db_table = 'class_records'


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.BooleanField(default=False)  # True for present, False for absent
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.date}"
    
    def __repr__(self):
        return f"Attendance({self.student}, {self.date}, {self.status})"
    
    class Meta:
        verbose_name_plural = "Attendance Records"
        ordering = ['-date']
        db_table = 'attendance_records'


class Exam(models.Model):
    subject = models.CharField(max_length=100)
    date = models.DateField()
    total_marks = models.IntegerField()
    max_marks = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject} - {self.date}"
    
    class Meta:
        verbose_name_plural = "Exams"
        ordering = ['date']
        db_table = 'exam_records'


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()
    grade = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.exam.subject}"
    
    class Meta:
        verbose_name_plural = "Results"
        ordering = ['-exam__date']
        db_table = 'result_records'