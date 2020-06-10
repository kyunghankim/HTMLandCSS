from django.db import models

# Create your models here.
class Article(models.Model):
    #원래는 있어야하는데 jango가 자동으로만들어줌
    #id = models.AutuField(primary_key=True) 
    title = models.CharField(max_length=100)
    content = models.TextField()
    #auto_now_add: 추가 될 때 한번만 시간 기록
    created_at = models.DateTimeField(auto_now_add=True)
    #auto_now: 변경사항 생길 때 마다 기록
    updated_at = models.DateTimeField(auto_now=True)
    #변경 사항 생길 때 마다 makemigrations하기
    def __str__(self): # f-string(문자열안에 변수를 넣기)
        return f'{self.id}번 글 - {self.title} : {self.content}'





# 1. models.py 작성 및 변경(생성 및 수정)
# 2. python manage.py makemigrations
#   => migration(설계도) 파일 생성
# 3. python manage.py migrate
#   => 실제 Database에 적용(테이블 생성)
#
# Django Shell
# python manage.py shell

# 0. Model import
# from articles.models import Article
# 1. Create
# 1-1. 인스턴스
# shell에서) article = Article()
# article.title = 'Fisrt'
# article.content = 'Wow!!'
# article.save() #<-save는 메소드라서 ()로 실행만 하는것
# 1-2. 두번째
# article = Article(title='Second',content='two')
# article.save()
# 1-3. 세번째 -> CREATE
# article = Article.objects.create(
# title='Third',content='three')

# 2. Read
# 2-1. all(): 전체를 불러들일때 ->SELECT  : 복수(0~여러개)
# articles = Article.objects.all()
# 2-2. filter() -> WHERE  : 복수(0~여러개)
# articles = Article.objects.filter(title='First')
# 2-3. get()   : 단수(1개) (인스턴스) 무조건1개만 return필수
# article = Article.objects.get(id=1)
# article = Article.objects.get(pk=1) <-id__exact
# article = Article.objects.get(title='First') <-Error
# article = Article.objects.get(pk=10) <-Error
# article = Article.objects.filter(pk=10) # []:error는 아님,빈리스트

# 2-4. QuerySet (유사 리스트)
# articles = Article.objects.all()
# articles[0] <-첫 번째 데이터
# articles.first() <-첫 번째 데이터
# articles[-1] or article.last() <-마지막 데이터
# articles[1:3] <- 2~3번째 데이터(OFFSET 1,  LIMIT 2)
# articles[OFFSET:OFFSET+LIMIT]
#
# 2-5. order_by()
# Article.objects.order_by('created_at') <-만들어진 시간 순정렬
# Article.objects.order_by('-created_at') <-역순정렬

# 3. Update
#  (1) 데이터 가져오기 (<- DB)
#  article = Article.objects.get(pk=1)
#  (2) 인스턴스 수정 (only python)
#  article.content = 'bye bye~'
#  (3) 인스턴스 저장(->DB)
#  article.save()
# 4. Delete
# (1) 데이터 가져오기 (<-DB)
# article = Article.objects.get(pk=1)
# (2) 인스턴스 삭제 (->DB)
# article.delete()
