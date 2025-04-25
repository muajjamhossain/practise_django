from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']


        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter post title here...'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your post content here...',
                'rows': 5
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'style': 'width: 15%; height: 30px;',
            }),
        }
        labels = {
            'title': 'Blog Title',
            'content': 'Content',
            'category': 'Select Category',
        }
        