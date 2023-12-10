from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

class Member(models.Model):
    ID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255, default='')
    password = models.CharField(max_length=255,blank=False)
    def save(self, *args):
        self.password = make_password(self.password)
        super().save(*args)

    def str(self):
        return f" {self.Username}"


class Post (models.Model):
    ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    Content = models.TextField(max_length=255)
    Category= models.CharField(max_length=255)
    Date_Published = models.DateTimeField('date published')

    def __str__(self):
        return f"{self.Title} {self.Content}"

class Comment(models.Model):
    ID = models.AutoField(primary_key=True)
    PostID= models.ForeignKey(Post, on_delete=models.CASCADE)
    UserID= models.ForeignKey(Member, on_delete=models.CASCADE)
    Content = models.TextField(max_length=255)
    Date_Posted = models.DateField()

    def __str__(self):
        return f"{self.Content} {self.Date_Posted}"

class Category (models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.Name} "



