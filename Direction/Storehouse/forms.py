from logging import PlaceHolder
from secrets import choice
from django import forms
from .models import Post, Category




class ContactForm(forms.Form):
    first_name = forms.CharField(max_length = 50)
	

#choices = [('GOD', 'GOD'), ('Life Issues', 'Life Issues'), ('World Problems', 'World Problems'),]
choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)
    

class PostForm(forms.ModelForm):
    class Meta:
        model =Post
        fields = ('title', 'author', 'category', 'body', 'Snippet', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'Kufre', 'type':'hidden'}),
        # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'Snippet': forms.Textarea(attrs={'class': 'form-control'}),
            
        }

class EditForm(forms.ModelForm):
    class Meta:
        model =Post
        fields = ('title',  'body', 'Snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'Snippet': forms.Textarea(attrs={'class': 'form-control'}),
            
        }