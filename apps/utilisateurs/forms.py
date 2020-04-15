from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Profile, User, Page, Clube



class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Facultatif')
    last_name = forms.CharField(max_length=30, required=False, help_text='Facultatif')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')


    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2', 
            ]

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Profile.objects.create(user=user)
        return user


class CompanyRegistrationForm(UserCreationForm):
    name_comapny = forms.CharField(max_length=30, required=True, help_text='Obligatoir')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')
    class Meta(UserCreationForm.Meta):
        model = User
        # fields = [
        #     'username',
            
        #     'email', 
        #     'password1', 
        #     'password2', 
        #     ]
    # def save(self):
    #     user = super().save(commit=False)
    #     user.is_company = True
    #     user.save()
    #     page = Page.objects.create(user=user)
    #     return user
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_company = True
        if commit:
            user.save()
            page = Page.objects.create(user=user)
        return user



class ClubeRegistrationForm(UserCreationForm):
    club_name = forms.CharField(max_length=30, required=True, help_text='Obligatoir')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')
    class Meta(UserCreationForm.Meta):
        model = User
        # fields = [
        #     'username',
            
        #     'email', 
        #     'password1', 
        #     'password2', 
        #     ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_club = True
        if commit:
            user.save()
            club = Clube.objects.create(user=user)
        return user

    
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
        ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "bio",
            "phone_number",
            "birth_date",
            "profile_image"
        ]



class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = [
            "description",
            "company_name",
            "address",
            "phone_number",
            "date",
            "profile_image"
        ]
class ClubeForm(forms.ModelForm):
    class Meta:
        model = Clube
        fields = [
            "description",
            "club_name",
            "address",
            "phone_number",
            "date",
            "profile_image"
        ]