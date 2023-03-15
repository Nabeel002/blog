from .models import *
from django import forms
import os
import openai
import config
class PostForm(forms.ModelForm):
    title=forms.CharField(
        label='title of the blog',
        widget=forms.TextInput(
                              attrs={'class': "form-control"})
    )
    
    body=forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'name':'name',
            'placeholde':'make a blog post',
            'class':'textarea'
        })
    )






    
    class Meta:
        model = Article
        fields = ('Author','title','body')




class CommentForm(forms.ModelForm):
    comment=forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class':'input',
            'name':'body', 
            'rows': '2',
            'placeholder': 'Add a comment...'
        }))

    
    class Meta:
        model = Comment
        fields = ("comment","name")



class ArticleForm(forms.ModelForm):
    

    class Meta:
        model = Article
        fields = ("Author","title","body","preview_image")



class PromptForm(forms.Form):
    promp= forms.CharField(max_length=250)

