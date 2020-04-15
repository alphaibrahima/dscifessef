from django import forms
from .models import Post, Comment, Annonce,Volontaria


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "contenu",
            "thumbnail",
        ]

class AnnonceForm(forms.ModelForm):
    class Meta:
        model = Annonce
        fields = [
            "title",
            "contenu",
            "categories",
            "thumbnail",
            
        ]

class VolontariaForm(forms.ModelForm):
    class Meta:
        model = Volontaria
        fields = [
            "title",
            "contenu",
            
        ]



class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Commentairest',
        'id': 'usercomment',
        'rows': '4'
    
    }))
    class Meta:
        model = Comment
        fields = ('content', )