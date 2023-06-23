from django.db import models

#Serializers : to convert complex data type
#for example result of models instance,query set,filter data all these complex data convert into normal python data type.

#Deserialixers : to convert python data type value into complex data type.
 
    

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.name

