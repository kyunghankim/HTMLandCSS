from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#1:N Relation
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    
    # Article: Comment = 1 : N
    # (부모) : (자식)

    # on_delete 옵션
    # 1. CASCADE - 부모가 삭제되면, 자식도 삭제됨 <-- 많이씀
    # 2. PROTECT - 자식이 있으면, 부모 삭제 불가
    # 3. SET_NULL - 부모가 삭제되면, 자식의 FK에 null 할당 <-- 큰 기업들이씀
    # 4. SET_DEFAULT - 부모가 삭제되면, 자식의 FK에 default값 할당
    # 5. DO_NOTHING - , 아무것도 하지 않음

    # 1. Create
    # article = Article.objects.get(pk=1)
    # comment = Comment()
    # comment.content = '첫 댓글 확인용'
    # comment.save()
    #