from django.db import models

# Create your models here.

class Registration(models.Model):
      Registration_ID = models.IntegerField(auto_created=True, primary_key=True)
      FirstName = models.CharField(max_length = 20)
      MiddelName = models.CharField(max_length = 20)
      LastName= models.CharField(max_length = 20)
      Age = models.IntegerField()
      Gender = models.CharField(max_length=10)
      MobileNo = models.IntegerField()
      Qualification = models.CharField(max_length=20)
      Reason_For_Visite = models.CharField(max_length=100)

      class Meta:
          db_table = 'Registration'