from django.db import models

# Create your models here.
class Companys(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=None)
    company = models.ForeignKey(Companys, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')
    resume = models.FileField(upload_to='resumes/')