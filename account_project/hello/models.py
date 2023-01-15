from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CARD_TYPE = [('credit card', 'Credit Card'), ('debit card', 'Debit Card')]


class ClubName(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="clubname", null=True)
    name = models.CharField(max_length=100)#, related_name="clubname", null=True)

    def __str__(self):
        return self.name

class ClubRep(models.Model):
    
    firstName = models.CharField(max_length=300)
    lastName = models.CharField(max_length=1)
    clubName = models.ForeignKey(ClubName, blank=True, null=True, on_delete=models.CASCADE)
    cardType = models.CharField(max_length=100)
    cardNumber = models.CharField(max_length=19) # card number 19 degits
    expiryDate = models.CharField(max_length=8)


    def __str__(self):
        return self.firstName + ' ' + self.lastName #+ ' '  +self.clubName

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     club= models.IntegerField()
# # 


# class MyModel(models.Model):
#     color = models.CharField(max_length=30, choices=CARD_TYPE, default='green')