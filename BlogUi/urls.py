from django.urls import path,include
from BlogUi.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('about/',AboutView.as_view(),name='about'),
    path('article/',ArticleView.as_view(),name='article'),
    path('create/',login_required(Admin.as_view()),name='create'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('contact/',contactCreateView.as_view(),name='contact'),
    path('post/<int:pk>',PostView.as_view(),name="post"),
    path('<pk>/update',ArticleUpdateView.as_view(),name="update"),
    path('<pk>/delete/',CommentDeleteView.as_view(),name="delete"),
    path('search/', UserSearch.as_view(), name='profile-search'),


]