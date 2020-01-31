from django.db import models

# Create your models here.
class dept_model(models.Model):
    dept_CHOICES=   [('dept', 'DEPT'),
    ('auth', 'authotiry')
    ]
    dept  = models.CharField(
        choices=dept_CHOICES,max_length=10)
    dname=models.CharField(max_length=20)
    def __str__(self):
        return self.dname
    # dept=models.ManyToManyField()
class auth_model(models.Model):
     authority_CHOICES = [('', 'DEPT'),
                     ('auth', 'authotiry')
                     ]
     Authority = models.CharField(choices=authority_CHOICES,max_length=100)
     dept  = models.ManyToManyField(dept_model)
     email=models.EmailField()

     def __str__(self):
         return self.email

