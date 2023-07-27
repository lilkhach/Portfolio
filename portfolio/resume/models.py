from datetime import datetime
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.

class SkillManager(models.Manager):
    pass

class PersonalInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    birth_year = models.PositiveIntegerField()
    city = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    quote = models.CharField(max_length=200, blank=True, null=True)
    birthday = models.CharField(max_length=50, blank=True, null=True)
    degree = models.CharField(max_length=50, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)

    def age(self):
        current_year = datetime.now().year
        return current_year - self.birth_year



    objects = SkillManager() 


class Skill(models.Model):
    name = models.TextField(max_length=30)
    value = models.PositiveIntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)], default=1)
    created_on = models.DateTimeField(auto_now=True)

    objects = SkillManager() 

    def __str__(self) -> str:
        return f"{self.name} skill value is {self.value}"


class Education(models.Model):
    university_name = models.TextField(max_length=200)
    start_date = models.PositiveIntegerField(validators=[MaxValueValidator(2023), MinValueValidator(1900)])
    end_date = models.PositiveIntegerField(validators=[MaxValueValidator(2023), MinValueValidator(1900)], blank=True, null=True)
    is_current = models.BooleanField()
    degree = models.TextField(max_length=40, blank=True, null=True)
    thesis_title = models.TextField(blank=True, null=True)

    objects = SkillManager() 

    def __str__(self) -> str:
        return f"{self.university_name} with {self.degree} degree"
    

class WorkExperience(models.Model):
    company_name = models.TextField(max_length=150)
    position = models.TextField(max_length=100)
    start_date = models.PositiveIntegerField(validators=[MaxValueValidator(2023), MinValueValidator(1900)])
    end_date = models.PositiveIntegerField(validators=[MaxValueValidator(2023), MinValueValidator(1900)], blank=True, null=True)
    is_current = models.BooleanField()

    objects = SkillManager() 


    def __str__(self) -> str:
        return f"{self.company_name} with {self.position} position"
    

class Languages(models.Model):
    name = models.TextField(max_length=30)
    value = models.PositiveIntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)], default=1)
    

    objects = SkillManager() 

    def __str__(self) -> str:
        return f"{self.name} language value is {self.value}"
    
class Photo(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='portfolio/')

    objects = SkillManager()

    def __str__(self) -> str:
        return f"{self.title}"
    
class Service(models.Model):
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    icon = models.TextField(max_length=200, blank=True, null=True)

    objects = SkillManager()

    def __str__(self) -> str:
        return f"{self.title}"
    
class SocialLink(models.Model):
    link = models.URLField()
    class_name = models.CharField(max_length=100, blank=True, null=True)
    icon_name = models.CharField(max_length=100, blank=True, null=True)

    objects = SkillManager()

    def __str__(self) -> str:
        return f"{self.class_name}"
    
class Navbar(models.Model):
    href = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100, blank=True, null=True)
    icon_class = models.CharField(max_length=100, blank=True, null=True)
    section_name = models.CharField(max_length=100, blank=True, null=True)

    objects = SkillManager()

    def __str__(self) -> str:
        return f"{self.section_name}"

class Message(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField(max_length=1000)
    created_on = models.DateTimeField(auto_now=True)

    objects = SkillManager()

