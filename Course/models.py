from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
import datetime


class User(models.Model):
    u_id = models.CharField(max_length=20, unique=True)
    u_name = models.CharField(max_length=80, unique=True)
    u_pwdhash = models.CharField(max_length=128, editable=False)
    STUDENT = 'ST'
    TEACHER = 'TC'
    ROLE_CHOICES = [
        (STUDENT, 'student'),
        (TEACHER, 'teacher'),
    ]

    role = models.CharField(
        max_length=2,
        choices=ROLE_CHOICES,
        default=STUDENT,
    )

    BOY = 'BY'
    GIRL = 'GL'
    SEX_CHOICES = [
        (BOY, 'boy'),
        (GIRL, 'girl'),
    ]
    sex = models.CharField(
        max_length=2,
        choices=SEX_CHOICES,
        default=BOY,
    )
    email = models.EmailField()
    tel = models.CharField(max_length=11)
    birth = models.DateField()
    dept = models.CharField(max_length=80)
    #无解，怎么设置都不能为空？https://stackoverflow.com/questions/11351619/how-to-make-djangos-datetimefield-optional
    #直接改数据库
    last_login = models.DateTimeField(null=True, blank=True)
    picture = models.ImageField(null=True, upload_to='static/res')

    def __str__(self):
        return self.u_name


class Course(models.Model):
    c_id = models.CharField(max_length=20)
    c_name = models.CharField(max_length=80)
    c_teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    c_info = models.TextField()
    c_visited = models.IntegerField(default=0)
    #c_files = models.CharField(max_length=128, default="")

    def __str__(self):
        return self.c_id + "::" + self.c_name


class SC(models.Model):
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    c_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    absent_cnt = models.IntegerField(default=0, blank=True)
    grades = models.DecimalField(max_digits=4, decimal_places=1, blank=True)

    def __str__(self):
        return self.u_id.u_name + " : " + self.c_id.c_name + " : " + str(self.grades) + " : " + str(self.absent_cnt)


class Topic(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    about = models.ForeignKey(Course, on_delete=models.CASCADE)
    text = models.TextField()
    time = models.DateTimeField()

    def __str__(self):
        return self.author.u_name + ": " + self.text


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    about = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    time = models.DateTimeField()

    def __str__(self):
        return self.author.u_name + " comment: " + self.text


class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    about = models.ForeignKey(Comment, on_delete=models.CASCADE)
    text = models.TextField()
    time = models.DateTimeField()

    def __str__(self):
        return self.author.u_name + " reply: " + self.text


class Notice(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    text = models.TextField()
    HOMEWORK = "HW"
    NOTICE = "NT"
    TYPE_CHOICES = [
        (HOMEWORK, 'homework'),
        (NOTICE, 'notice'),
    ]
    type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        default=NOTICE,
    )
    time = models.DateTimeField()

    def __str__(self):
        return self.type + ": " + self.text
