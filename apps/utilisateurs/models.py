from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
    is_club    = models.BooleanField(default=False)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    birth_date = models.DateField( null=True, blank=True)
    profile_image = models.ImageField(default='profile_default.jpg', upload_to='users_profile/', null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)

# @receiver(post_save, sender=User)        
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)     

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

class Page(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    description = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    company_name = models.CharField(max_length=50, blank=True)
    address = models.TextField(max_length=500, blank=True)
    date = models.DateField(null=True, blank=True )
    profile_image = models.ImageField(default='profile_default.jpg', upload_to='page_logo/', null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.user.username, self.user.username)




class Clube(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    description = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    club_name = models.CharField(max_length=50, blank=True)
    address = models.TextField(max_length=500, blank=True)
    date = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(default='profile_default.jpg', upload_to='clubs_logo/', null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.user.last_name, self.user.last_name)