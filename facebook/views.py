from django.shortcuts import render, redirect
from facebook.models import Article
from facebook.models import Comment
# Create your views here.

count = 0

def play(request):
    return render(request, 'play.html')


def play2(request):
    name = 'jongho'
    global count
    count = count + 1
    age = 32
    if age > 20:
        status = '성인'
    else:
        status = '청소년'
    list = ['오늘은 진짜 좆나 짜증나는 날이다','아아 개짜증','살려줘', 'FFFFFFUCK']
    return render(request, 'play2.html', {'name':name,'cnt':count, 'status':status, 'list':list})

def profile(request):
    return render(request, 'profile.html')

def event(request):
    global count
    count = count + 1

    if count == 7:
        status = '당첨'
    else:
        status = '꽝'
    return render(request, 'event.html', {'count':count, 'status':status})

def newsfeed(request):
    articles = Article.objects.all()
    return render(request, 'newsfeed.html', {'articles' : articles})

def detail_feed(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        Comment.objects.create(
            article=article,
            author=request.POST.get('nickname'),
            text=request.POST.get('reply'),
            password=request.POST.get('password')
        )
        return redirect(f'/feed/{ article.pk }')
    return render(request, 'detail_feed.html', {'article' : article})
def new_feed(request):
    if request.method == 'POST':
        Article.objects.create(
            author=request.POST['author'],
            title=request.POST['title'],
            text=request.POST['content'],
            password=request.POST['password']
        )
    return render(request, 'new_feed.html')

def edit_feed(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.author = request.POST['author']
        article.title = request.POST['title']
        article.text = request.POST['content']
        article.save()
        return redirect(f'/feed/{article.pk}')
        # return redirect(f'/feed' + str(article.pk))
    return render (request, 'edit_feed.html', {'article' : article})

def remove_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        if article.password == request.POST['password']:
            article.delete()
            return redirect('/')
        else:
            #같이 않다면 '오류페이지'로 이
            pass

    return render (request, 'remove_feed.html', {'article' : article})
