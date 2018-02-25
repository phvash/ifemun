from django.db import models

class Applicant(models.Model):
    # author = models.ForeignKey('settings.AUTH_USER_MODEL')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.CharField(max_length=200)
    part = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + " " + self.last_name