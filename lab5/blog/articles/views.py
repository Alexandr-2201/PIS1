from .models import Article
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render, redirect

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
