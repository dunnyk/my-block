from .models import Comment
from django import forms
from .models import Image

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class ImageForm(forms.ModelForm):
    #form for the image models
    class Meta:
        model = Image
        fields = ('title', 'image')