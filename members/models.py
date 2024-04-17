from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Member(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    
    O_POSITIVE = 'O+'
    O_NEGATIVE = 'O-'
    A_POSITIVE = 'A+'
    A_NEGATIVE = 'A-'
    AB_POSITIVE = 'AB+'
    AB_NEGATIVE = 'AB-'
    B_POSITIVE = 'B+'
    B_NEGATIVE = 'B-'
    BLOOD_GROUP_CHOICES = [
        (O_POSITIVE, 'O+'),
        (O_NEGATIVE, 'O-'),
        (A_POSITIVE, 'A+'),
        (A_NEGATIVE, 'A-'),
        (AB_POSITIVE, 'AB+'),
        (AB_NEGATIVE, 'AB-'),
        (B_POSITIVE, 'B+'),
        (B_NEGATIVE, 'B-'),
    ]

    # Personal info
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    avatar = models.ImageField(upload_to='member_images/', null=True, blank=True)
    cover_photo = models.ImageField(upload_to='member_images/', null=True, blank=True)
    father_name = models.CharField(max_length=50, null=True, blank=True)
    mother_name = models.CharField(max_length=50, null=True, blank=True)
    religion = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True, blank=True)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, null=True, blank=True)
    nid_no = models.CharField(max_length=20, null=True, blank=True)
    mobile_no = models.CharField(max_length=50, null=True, blank=True)
    present_address = models.TextField(null=True, blank=True)
    permanent_address = models.TextField(null=True, blank=True)
    
    # Organizational info
    membership_no = models.CharField(max_length=20, null=True, blank=True)
    membership_date = models.CharField(max_length=20, null=True, blank=True)
    membership_category = models.CharField(max_length=100, null=True, blank=True)
    nominee_name = models.CharField(max_length=50, null=True, blank=True)
    nominee_relation = models.CharField(max_length=50, null=True, blank=True)
    nominee_dob = models.DateField(blank=True, null=True)
    present_job = models.CharField(max_length=100, null=True, blank=True)
    professional_skills = models.TextField(null=True, blank=True)
    chamber_address = models.CharField(max_length=100, null=True, blank=True)
    
    
    def __str__(self):
        return self.name


class Slider(models.Model):
    image = models.ImageField(upload_to='slider_images/', null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    
class Event(models.Model):
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateField(blank=True, null=True)
    updated_at = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    

class Media(models.Model):
    image = models.ImageField(upload_to='media_images/', null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateField(blank=True, null=True)
    updated_at = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class Activities(models.Model):
    image = models.ImageField(upload_to='activites_images/', null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateField(blank=True, null=True)
    updated_at = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class PhotoGallary(models.Model):
    image = models.ImageField(upload_to='photo_gallary/', null=True, blank=True)

    def __str__(self):
        return f"PhotoGallary Image: {self.image.name}" if self.image else "PhotoGallary (No Image)"
