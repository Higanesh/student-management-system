from django.db import models

# Create your models here.

class StudentClass(models.Model):
    name = models.CharField(max_length=50) 
    section = models.CharField(max_length=1, blank=True, null=True) 
    class_teacher = models.CharField(max_length=100, blank=True)  
    academic_year = models.CharField(max_length=9) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - Section {self.section}"


class Student(models.Model):
    GENDER_CHOICES = [
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other'),
        ]

    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.CharField()
    email = models.EmailField(unique=True,blank=False)
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    address = models.TextField()
    roll_number = models.CharField(max_length=10,unique=True)
    class_name = models.ForeignKey(StudentClass,on_delete=models.CASCADE)
    admission_date = models.DateField()
    profile_pic = models.ImageField(upload_to='stud_images/',null=True,blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    

