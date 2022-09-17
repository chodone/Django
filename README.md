# Django

## 클라이언트 - 서버 구조
- 클라이언트(client)
     - 웹 사용자의 인터넷 연결장치
     - 웹 브라우저(chrome, firefox)
     - 서비스를 요청하는 주체(request)
- 서버(server)
    - 웹페이지, 사이트 또는 앱을 저장하는 컴퓨터
    - 클라이언의 request에 웹 페이지의 데이터를 response
    - 요청에 대해 서비스를 응답하는 주체(response)


    





## Web browser & Web page

- Web Browser
    - HTML/ CSS / JS 등의 코드를 읽어 실제 우리가 보고 있는 화면으로 만들어주는 프로그램
    - 웹 페이지의 파일을 우리가 보는 화면으로 바꿔주는 rendering 프로그램

- 정적 웹페이지(static web page)
    -  한번 작성된 HTML 파일의 내용이 변하지 않고 모든 사용자에게 동일한 모습으로 전달되는것

- **동적 웹페이지(dynamic web page)**
    - 클라이언트의 요청때마다 웹페이지가 바뀌는 구조는 비효율적이다
    - 따라서 사용자의 요청에 따라 웹페이지에 추가적인 수정이 되어 클라이언트에게 전달



## Design Pattern

- MVC 
    - Model - View - Controller의 준말
- **MTV**

  - ![MTV](.\img\img/MTV.jpeg)
  - Model - Template - View 의 준말
  - Django에서는 MTC 패턴을 사용
  - Model
    - 데이터와 관련된 로직 관리
    - 응용프로그램의 데이터 구조를 정의, 데이터베이스 기록 관리
  - Template
    - 레이아웃과 화면처리
    - 화면상의 사용자 인터페이스 구조와 레이아웃을 정의
    - MVC 에서 View
  - View
    - Model 과 Template 관련한 로직을 처리해서 응답을 반환 
    - 클라이언트 요청에 대한 처리를 분기하는 역할
    - 동작예시
      - 데이터가 필요하다면 Model에 접근해서 데이터를 가져오고 Template로 보내 화면을 구성 후 구성된 화면을 응답으로 만들어 클라이언트에게 반환
    - MVC에서 Controller 





### 가상환경 만들기
    
    - projcet 하나마다 하나의 가상환경을 생성한다
    - 폴더에서 git bash here 실행
    - 명령어 

            # 가상환경 활성화
             python -m venv venv


            
            python -m venv venv
            source venv/Scripts/activate -(window)
            source venv/bin/activate -(mac)


            # package 관리
            pip install django == 3.2.13 (Django 설치)
            pip freeze > requirements.txt  다운받은 패키지 목록을 txt 파일로 저장

            
            # git에서 클론 받은 후 작업이라면 
            pip install -r requirements.txt를 통해 패키지를 한번에 다운한다. 


            # 프로젝트 생성

            django-admin startproject '프로젝트명' - 프로젝트 생성
            python manage.py runserver - 서버 실행
            python manage.py startapp '어플리케이션명'  - 어플리케이션(앱) 생성 * 앱 이름은 복수로 작성하는것을 권장
            **반드시 어플리케이션 생성 후 프로젝트의 setting.py의 INSTALLED_APPS의 등록한다




