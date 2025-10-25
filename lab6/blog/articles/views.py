from .models import Article
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all(), 'full_text': False})

def get_archive(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'archive.html', {"posts": [post], 'full_text': True})
    except Article.DoesNotExist:
        raise Http404

def article(request):
    return render(request, 'article.html', {"posts": Article.objects.all(), 'full_text': False})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"posts": [post], 'full_text': True})
    except Article.DoesNotExist:
        raise Http404

def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            # обработать данные формы, если метод POST
            form = {
                'text': request.POST["text"], 
                'title': request.POST["title"]
            }
            # в словаре form будет храниться информация, введенная пользователем
            if form["text"] and form["title"]:
                # Проверка уникальности названия
                if Article.objects.filter(title=form["title"]).exists():
                    form['errors'] = "Статья с таким названием уже существует"
                    return render(request, 'create_post.html', {'form': form})
                
                # если поля заполнены без ошибок и название уникально
                try:
                    new_article = Article.objects.create(
                        text=form["text"], 
                        title=form["title"], 
                        author=request.user
                    )
                    return redirect('get_article', article_id=new_article.id)
                except:
                    # Если произошла ошибка при создании (например, нарушение уникальности)
                    form['errors'] = "Статья с таким названием уже существует"
                    return render(request, 'create_post.html', {'form': form})
            else:
                # если введенные данные некорректны
                form['errors'] = "Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            # просто вернуть страницу с формой, если метод GET
            return render(request, 'create_post.html', {})
    else:
        raise Http404

def registration(request):
    if request.method == "POST":
        # обработать данные формы, если метод POST
        form = {
            'password': request.POST["password"],
            'email': request.POST["email"], 
            'login': request.POST["login"]
        }
        # в словаре form будет храниться информация, введенная пользователем
        if form["password"] and form["email"] and form["login"]:
            try:
                User.objects.get(username=form["login"])
                # если пользователь существует, то ошибки не произойдет и программа
                # удачно доберется до следующей строчки
                form['errors'] = "Пользователь с таким логином уже существует"
                return render(request, 'registration.html', {'form': form})
            except User.DoesNotExist:
                new_user = User.objects.create_user(form["login"], form["email"], form["password"])
                return redirect('article')
        else:
            # если введенные данные некорректны
            form['errors'] = "Не все поля заполнены"
            return render(request, 'registration.html', {'form': form})
    else:
        # просто вернуть страницу с формой, если метод GET
        return render(request, 'registration.html', {})

def auth(request):
    if request.method == "POST":
        # обработать данные формы, если метод POST
        form = {
            'password': request.POST["password"],
            'login': request.POST["login"]
        }
        # в словаре form будет храниться информация, введенная пользователем
        if form["password"] and form["login"]:
            user = authenticate(username=form["login"], password=form["password"])
            if user is None:
                form['errors'] = "Пользователя с таким паролем не существует"
                return render(request, 'auth.html', {'form': form})
            else:
                login(request, user)
                return redirect('article')
        else:
            # если введенные данные некорректны
            form['errors'] = "Не все поля заполнены"
            return render(request, 'auth.html', {'form': form})
    else:
        # просто вернуть страницу с формой, если метод GET
        return render(request, 'auth.html', {})
