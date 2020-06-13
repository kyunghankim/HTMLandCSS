1. 가상 환경 설정
```
python -m venv venv
```

2. 가상 환경 세팅(VS code 기능)
    - `Ctrl + Shift + p`
    - Python Select Interpreter 검색 후 venv 선택

3. Django 설치
```
pip install django==2.2.13
```

4. Django 프로젝트 생성
```
django-admin startproject crud .
```

5. Django App 생성
```
python manage.py startapp articles
```


6. App 등록
```python
INSTALLED_APPS = [
    'articles',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

7. 언어와 시간
 - settings.py  
 - `LANGUAGE_CODE = 'ko-kr'`
 - `TIME_ZONE = 'Asia/Seoul'`

8. base.html 설정
    - settings.py
    - TEMPLATES - DIRS 추가
    - `os.path.join(BASE_DIR,
    'templates')` 추가
    - 최상위 폴더에서 templates 폴더 생성
    - templates > base.html 생성

 9. urls.py 분리
    - articles > urls.py 생성
    - crud > urls.py에서 include로 path 추가