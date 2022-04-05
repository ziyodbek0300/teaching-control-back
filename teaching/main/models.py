from django.db import models

# Create your models here.
class Users(models.Model):
    sts = (
        (1, 'Administrator'),
        (2, 'Teacher'),
        (3, 'Cleaner'),
        (4, 'Sales Asistant'),
        (5, 'SMM manager'),
        (6, 'Designer'),
        (7, 'Internship'),
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    password = models.CharField(max_length=255, unique=True)
    position = models.IntegerField(choices=sts, default=2)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'Users'



class Jobs(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='pictures/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Jobs'

class Section(models.Model):
    title = models.CharField(max_length=255)
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Section'

class Theme(models.Model):
    title = models.CharField(max_length=255)
    link = models.TextField()
    files = models.FileField(upload_to='uploads/')
    yt_video = models.TextField()
    lesson_status = models.BooleanField(default=True)
    sections = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name_plural = 'Theme'

