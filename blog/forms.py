from django import forms
from django.forms import fields
from blog.models import Post,Comment

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ("preview_field","author","post_image","title","text")
        widgets={
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }



class CommentForm(forms.ModelForm):

    class Meta:
        model= Comment
        fields=("author","text")

        widgets={
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
