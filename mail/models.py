from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return "{} => {}".format(self.name,self.message)
    
    class Meta:
        verbose_name_plural = "Inquires"
        verbose_name = "Inquires" # 1 space


class Injection_Booking(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=200)
    message = models.TextField()
    STATUS_CHOICES = (
        ('pending','Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')


    def __str__(self):
        return "{} => {}".format(self.name,self.phone,self.email)
    

    
