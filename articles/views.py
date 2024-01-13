from django.shortcuts import render , get_object_or_404 ,redirect
from .models import Article
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth import login , authenticate ,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ArticleForm
# Create your views here.

#to chow all articles
def All_articles(request):
    articles = Article.objects.all()
    return render(request,'articles/all_articles.html',{'articles':articles})


# see user articles
@login_required
def user_articles(request):
    user_articles = Article.objects.filter(author=request.user)
    return render(request, 'articles/user_articles.html', {'user_articles': user_articles})


@login_required
def article_detail(request,article_id):
    article= get_object_or_404(Article,id=article_id, author=request.user)
    return render(request ,'articles/article_detail.html',{'article':article})


@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('user_articles')
    else:
        form = ArticleForm()

    return render(request, 'articles/create_article.html', {'form': form})


@login_required
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id, author=request.user)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('user_articles')
    else:
        form = ArticleForm(instance=article)

    return render(request, 'articles/edit_article.html', {'form': form, 'article': article})


@login_required
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id, author=request.user)

    if request.method == 'POST':
        article.delete()
        return redirect('user_articles')

    return render(request, 'articles/delete_article.html', {'article': article})


def signup(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request,user)
            return redirect('../articles/all')
        else:
            print('not valid')
    else:
        form = UserCreationForm()
    return render(request,'registration/signup.html',{'form':form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('../articles/all')  # Change 'home' to the URL where you want users to be redirected after login
            else:
                messages.error(request, 'Invalid login credentials.')
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('../login')

