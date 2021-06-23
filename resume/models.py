from django.db import models

# Create your models here.

class Resume_info(models.Model):
    STATE_CHOICE = {
        ('dhaka','Dhaka'),
        ('chitfagram','Chitfagram'),
        ('khunla','Khulna'),
        ('rajshahi','Rajshahi'),
        ('borishal','Borishal'),
        ('rangpur','Rangpur')
    }
    GENDER_CHOICE = {
        ('m', 'Male'),
        ('f','Female' ),
        ('o','Others'),
    }
    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(choices=GENDER_CHOICE, max_length=8)
    locality = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    pin_code = models.PositiveIntegerField()
    state = models.CharField(choices=STATE_CHOICE, max_length=20)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=100)
    profile_img = models.ImageField(upload_to='profileimg/', blank = True)
    my_file = models.FileField(upload_to='myfile/', blank = True)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
