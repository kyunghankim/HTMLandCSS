from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
        # Database 조회(꺼내오기)
    articles = Article.objects.all() #<- DB에 있는 게시글 데이터 전부!
    context = {
        'articles': articles,
       
    }
    return render(request, 'articles/index.html',context)

def new(request): #<-GET
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        # 데이터베이스에 저장
        # 1. Article 인스턴스 생성
        article = Article(title=title, content=content)
        # 2. save!
        article.save()

        return redirect('articles:detail', article.pk)
    else:
        context = {

        }
        return render(request, 'articles/new.html',context)

#get으로 보낸요청은 get로만 받아야함
#post도 마찬가지
def create(request): #<-POST
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 데이터베이스에 저장
    # 1. Article 인스턴스 생성
    article = Article(title=title, content=content)
    # 2. save!
    article.save()

    return redirect('articles:detail', article.pk)
    # context = {
    #     'title':title,
    #     'content': content,                  <-필요없어짐 
    # }

    #return render(request, 'articles/create.html',context) <-필요없어짐 
    
def detail(request, pk):
    # Database 조회: 단 하나의 data
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk): # POST
    #Database 삭제 (조회+삭제)
    # 1. 조회
    article = Article.objects.get(pk=pk)
    # 2. 삭제 명령
    article.delete()

    return redirect('/articles/index/')

def edit(request, pk): #GET
    # 1. 조회
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        # 게시글 수정!
        title = request.POST.get('title')
        content = request.POST.get('content')
        # database 조회 + 수정
        # 2. 수정
        article.title = title
        article.content = content
        # 3. 저장
        article.save()

        return redirect('detail',article.pk)
    else:
        #게시글 수정 양식!

        # Database 조회(+ 저장)
        # 1. 조회
        # 2. 저장
        context = {
            'article': article,
        }
        return render(request, 'articles/edit.html',context)

def update(request, pk): #POST
    title = request.POST.get('title')
    content = request.POST.get('content')

    # database 조회 + 수정
    # 1. 조회
    article = Article.objects.get(pk=pk)
    # 2. 수정
    article.title = title
    article.content = content
    # 3. 저장
    article.save()

    return redirect('detail',article.pk)