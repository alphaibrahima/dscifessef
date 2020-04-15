from django.db import models
from ..utilisateurs.models import User
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length = 20)

    def __str__(self):
        return self.title



class Post(models.Model):
    contenu = models.TextField()
    thumbnail = models.ImageField()
    timestamp = models.DateTimeField(auto_now_add=True)
    author    = models.ForeignKey(User, on_delete=models.CASCADE)
    # Le default 2 c a enlever en production
    comment_count = models.IntegerField(default=2)
    archive = models.BooleanField(default=False)
    
    #fonction str
    def __str__(self):
        return f"{self.author } -- {self.timestamp}"
    
    def get_absolute_url(self):
        return reverse('details', kwargs={
            'pk': self.pk
            })
    def get_update_url(self):
        return reverse('update', kwargs={
            'pk': self.pk
            })
    
    def get_delete_url(self):
        return reverse('delete', kwargs={
            'pk': self.pk
            })
            

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username


class Annonce(models.Model):
    title = models.CharField(max_length = 100)
    contenu = models.TextField()
    thumbnail = models.ImageField()
    timestamp = models.DateTimeField(auto_now_add=True)
    author    = models.ForeignKey(User, on_delete=models.CASCADE)
    # Le default 2 c a enlever en production
    interet_count = models.IntegerField(default=2)
    archive = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category)
    
    #fonction str
    def __str__(self):
        return f"{self.author } -- {self.timestamp} -- {self.title}"

        def get_absolute_url(self):
            return reverse('details', kwargs={
            'pk': self.pk
            })
    def get_update_url(self):
        return reverse('update', kwargs={
            'pk': self.pk
            })
    
    def get_delete_url(self):
        return reverse('delete', kwargs={
            'pk': self.pk
            })
            

    @property
    def get_interets(self):
        return self.interets.all().order_by('-timestamp')


class Interet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Annonce, related_name='interets', on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username

#Association   
class Volontaria(models.Model):
    title = models.CharField(max_length = 100)
    contenu = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    author    = models.ForeignKey(User, on_delete=models.CASCADE)
    # Le default 2 c a enlever en production
    interet_count = models.IntegerField(default=2)
    archive = models.BooleanField(default=False)
    #categories = models.ManyToManyField(Category)
    
    #fonction str
    def __str__(self):
        return f"{self.author } -- {self.title}"

    def get_absolute_url(self):
        return reverse('details', kwargs={
            'pk': self.pk
            })
    def get_update_url(self):
        return reverse('update', kwargs={
            'pk': self.pk
            })
    
    def get_delete_url(self):
        return reverse('delete', kwargs={
            'pk': self.pk
            })
            

    @property
    def get_volontaires(self):
        return self.volontaire.all().order_by('-timestamp')


class Volontaire(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Volontaria, related_name='volontaires', on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username

