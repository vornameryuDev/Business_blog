# business_blog
```
- 공지사항 게시
- 사람들 질문받고 답하는 게시판 구현
- 회원가입 및 로그인
```



## Requirements
```
전체 패키지 등의 버젼은 requirements.txt에서 확인 가능. 주요 패키지들의 버젼만 제시
- python 3.10.11
- Flask 3.0.3
- Flask-Migrate 4.0.7
- Flask-Login 0.6.3
```

## Server
ip: AWS LightSail
web: NginX
WSGI: Gunicorn
  

## 화면구성
```
- Home & Notice
```
  ![image](https://github.com/vornameryuDev/business_blog/assets/164843831/3e837ea6-69de-4984-b70f-de127a447299)

```
- QnA
```
  ![image](https://github.com/vornameryuDev/business_blog/assets/164843831/16151e49-3abe-4416-9832-06a973399434)

```
- SignIn
```
  ![image](https://github.com/vornameryuDev/business_blog/assets/164843831/5359a26b-b61d-4421-8d10-4b53f5d5a7ac)

```
- LogIn
```
  ![image](https://github.com/vornameryuDev/business_blog/assets/164843831/0060f6c0-19b8-4f09-b206-32376cb58f81)


## 주요기능
```
1. blueprint
  - user(회원가입, 로그인, 로그아웃)
  - notice(등록, 수정, 삭제)
  - question(질문등록, 수정, 삭제, 추천)
  - answer(답변등록, 수정, 삭제, 추천)
  - comment(댓글등록, 수정, 삭제, 추천)

2. 사용기술
  - user: flask_login, load_user, login_required, current_user
  - error: flash
  - route: redirect, url_for, request(GET, POST)
  - db: MySQL(local), SQLAlchemy
  - security: CORS

3. logging
  - info수준으로 파일저장
  - RotatingFileHandler사용
```


## 디렉토리
```
📦business_blog
 ┣ 📂forms
 ┃ ┣ 📜answer_form.py
 ┃ ┣ 📜notice_form.py
 ┃ ┣ 📜question_form.py
 ┃ ┗ 📜user_forms.py
 ┣ 📂migrations
 ┣ 📂models
 ┃ ┣ 📜answer_model.py
 ┃ ┣ 📜comment_model.py
 ┃ ┣ 📜notice_model.py
 ┃ ┣ 📜question_model.py
 ┃ ┗ 📜user_model.py
 ┣ 📂static
 ┃ ┣ 📂js
 ┃ ┗ 📜style.css
 ┣ 📂templates
 ┃ ┣ 📂answer
 ┃ ┣ 📂comment
 ┃ ┣ 📂notice
 ┃ ┣ 📂question
 ┃ ┣ 📂snippets
 ┃ ┣ 📂user
 ┃ ┗ 📜base.html
 ┣ 📂views
 ┃ ┣ 📜answer_views.py
 ┃ ┣ 📜comment_views.py
 ┃ ┣ 📜notice_views.py
 ┃ ┣ 📜question_views.py
 ┃ ┗ 📜user_views.py
 ┣ 📜app.py
 ┣ 📜config.py
 ┣ 📜filters.py
```



