from django import forms
from .models import Post, Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'title', 'content']


        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter post title here...',
                'style': 'color: red;',
                'custom_class': 'custom-class',  # Custom class for styling
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your post content here...',
                'rows': 5
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
        }
        labels = {
            'title': 'Blog Title',
            'content': 'Content Test',
            'category': 'Select Category',
        }




class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter category name here...'
            }),
        }
        labels = {
            'name': 'Category Name',
        }
        