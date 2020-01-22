from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    image = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)


class EditModel(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()


class Articles(models.Model):
    title = models.CharField(max_length=200)
    desc= models.CharField(max_length=200)


class Permissions(models.Model):
    class Meta:
        permissions = [
            ('codename',''),

        ]


class Bar(models.Model):
    objects = jmodels.jManager()
    name = models.CharField(max_length=200)
    date = jmodels.jDateField()

    def __str__(self):
        return "%s, %s" % (self.name, self.date)


class BarTime(models.Model):
    objects = jmodels.jManager()
    name = models.CharField(max_length=200)
    datetime = jmodels.jDateTimeField()

    def __str__(self):
        return "%s, %s" % (self.name, self.datetime)


# class Tasks(models.Model):
#     user=models.ForeignKey(User, on_delete=models.CASCADE)


# class UserProfile(models.Model):
#     user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
#     url = models.URLField("Website", blank=True)
#     company = models.CharField(max_length=50, blank=True)


