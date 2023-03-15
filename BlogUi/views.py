from django.shortcuts import render
from django.views.generic import*
from BlogUi.models import *
from BlogUi.forms import *
from django.contrib.auth.decorators import login_required
from ipware import get_client_ip
import socket
import openai
import config
import os
from django.http import HttpResponseRedirect
from django.db.models import Q


# Create your views here.
openai.api_key = "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"

class Index(View):
    def get(self,request,*args, **kwargs):
        post=Article.objects.all()
        context={"post":post}
        return render(request,"index.html",context=context)


        


class AboutView(TemplateView):
    template_name = "about.html"




class ArticleUpdateView(UpdateView):
    model = Article
    template_name = "article_edit.html"
    fields=['body','title']
    success_url="/"


class ArticleView(TemplateView):
    template_name="article.html"












class ContactList(ListView):
    model = contact
    template_name='contact.html'
    
class contactCreateView(CreateView):
    model=contact
    template_name = "contact.html"
    fields=['email','req']
    success_url="/"


    def get_form(self, form_class=None):
      form = super(contactCreateView, self).get_form(form_class)
      form.fields['email'].required = True
      form.fields['req'].required = True
      return form



class ArticleView(ListView):
    model=Article
    template_name="article.html"


class ArticleListView(ListView):
    model = Article
    template_name = "index.html"







class PostView(View):
    def get(self,request,pk,*args, **kwargs):
        post=Article.objects.get(pk=pk)
        comment_form=CommentForm()
        comments=Comment.objects.filter(post=post).order_by('-date')
        context={"posts":post,"form":comment_form,"comments":comments}
        return render(request,"article_view.html",context=context)

        
        


    def post(self,request,pk,*args, **kwargs):
        post=Article.objects.get(pk=pk)
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post=post
            new_comment.save()
        comments=Comment.objects.filter(post=post).order_by('-date')
        context={
            'form':comment_form,
            'posts':post,
            'comments': comments,
            }

        
        return render(request, 'article_view.html', context)






def contacts(request):
    reach=contact.objects.all()
    context={"reach":reach}
    return render(request,"admin.html",context)





class Admin(View):
    def get(self,request):
        reach=contact.objects.all()
        form =ArticleForm()
        promptform=PromptForm()
        return render(request,"admin.html",{"reach":reach,"form":form,"promptform":promptform})
    

    def post(self,request):
        form =ArticleForm(request.POST)
        prompt=""
        promptform=PromptForm(request.POST)

        if promptform.is_valid():
            prompt= promptform.cleaned_data.get("promp")

        response=openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            temperature=0.7,
            max_tokens=4000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        resp=response['choices'][0]['text']
        if form.is_valid():
            new_form=form.save(commit=False)
            new_form.author=request.user
            new_form.save()

        reach=contact.objects.all()

        return render(request,"admin.html",{"reach":reach,"form":form,"promptform":promptform,"resp":resp})


        


class CommentDeleteView(DeleteView):
    model = Comment
    success_url ="/"
    template_name = "comment_delete.html"


class UserSearch(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        blog_list = Article.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )

        context = {
            'blog_list': blog_list,
            'query':query
        }

        return render(request, 'search.html', context)