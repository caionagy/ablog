from secrets import choice
from django import forms
from .models import Category, Post
#lista set
#choices = [('test1', 'test1'),('test2','test2')]
choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title Post'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tag page'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username', 'value':'', 'id':'elder', 'type':'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Lorem Inp...'}),
            
        } 
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title Post'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tag page'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Lorem Inp...'}),
            
        } 


