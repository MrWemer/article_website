from django.urls import path
from .views import All_articles,article_detail ,user_articles
from .views import create_article , edit_article,delete_article
from .views import signup ,user_login , user_logout


urlpatterns=[
    path('articles/all',All_articles,name='all_articles'),
    path('articles/user_articles/', user_articles, name='user_articles'),
    path('articles/user_articles/<int:article_id>/', article_detail, name='article_detail'),
    path('articles/user_articles/<int:article_id>/edit/', edit_article, name='edit_article'),
    path('articles/user_articles/<int:article_id>/delete/', delete_article, name='delete_article'),
    path('articles/create/', create_article, name='create_article'),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]