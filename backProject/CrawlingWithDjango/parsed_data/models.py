from django.db import models

# Create your models here.
class schoolData(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=200)
    publishedDate = models.CharField(max_length=200)
    createDate = models.DateField(auto_now_add=True)
    body = models.TextField()
    file = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    
class blogData(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=200)
    publishedDate = models.CharField(max_length=200)
    createDate = models.DateField(auto_now_add=True)
    body = models.TextField()
    
    def __str__(self):
        return self.title
    
class newsData(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=200)
    publishedDate = models.CharField(max_length=200)
    createDate = models.DateField(auto_now_add=True)
    body = models.TextField()
    
    def __str__(self):
        return self.title