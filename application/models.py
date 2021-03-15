from django.db import models

# Create your models here.

class Site(models.Model):
    siteName = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/")
    def __str__(self):
        return self.siteName

class Fields(models.Model):
    name = models.CharField(max_length=200)
    siteID = models.ForeignKey('Site',on_delete=models.CASCADE,
    related_name='Site')
    empID = models.IntegerField()
    certificates = models.CharField(max_length=200)
    yearOfCompletion = models.CharField(max_length=200)
    def __str__(self):
        return str(self.siteID)
