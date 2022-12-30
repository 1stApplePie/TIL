# HTML5 문서 구조화와 웹 폼
## 1. HTML5의 문서 구조화
웹 페이지와 문서의 공통점은 모두 문서이며 잘 구조화 되어야 한다. 구조화의 중요성은 현시대의 정보 탐색에 있어 쉽게 탐색해보기 위해 노력해 보았다면 쉽게 이해할 수 있다.
<br>HTML에서 사용되던 <p\>, <div\>, <h1\>, <h2\> 등의 태그와 HTML5에서 추가된 <header\>, <section\>, <article\> 등 문서 구조와 의미를 표현하는 태그(시맨틱 태그)들을 사용하면 시맨틱 웹(semantic web)을 만들 수 있을것이다.
<br> HTML5 문서를 구조화 하는데 필요한 시맨틱 태그에 대해 알아보자.

---
## 2. 시맨틱 태그
* <header\>
    * <header\>는 페이지나 섹션의 머리말을 표현하는 태그. 보통 머리말에는 페이지 제목, 페이지를 소개한다. <header\>는 <section\>이나 <article\>태그 내에도 사용

* <nav\>
    * <nav\>는 navigation의 줄임말이며 하이퍼 링크를 모아놓은 섹션. 페이지 내 목차를 만들기 위해 주로 사용

* <section\>
    * <section\>은 문서의 장 혹은 절을 구성하는 역할. <section\>에는 헤딩 태그(<h1\> ~ <h6\>)로 섹션의 주제를 기재하는 것이 바람직

* <article\>
    * <article\>은 본문과 연관되어 있으나 독립적인 컨텐츠도 담는다.

* <aside\>
    * <aside\>는 웹 페이지 본문 흐름에서 약간 벗어난 노트나 팁, 신문, 잡지엣 주요 기사 옆에 짤막하게 곁들이는 관련 기사, 삽입 어구로 표시된 논평이나 글 등을 담는다.

* <footer\>
    * <footer\>는 꼬리말 영역을 표시하는 태그로서, 페이지나 <section\>내에 꼬리말을 담음. 주로 저자나 저작권 정보 등을 주로 표시.
---
## 3. HTML5 문서 구조화 사례
```'
<!DOCTYPE html>
<html>
    <head>
        <meta charset = "utf-8">
        <title>
            HTML5 문서 구조 시맨틱 태그 사용
        </title>
        <style>
            html, body {margin: 0; padding: 0; height: 100%;}
            header {width: 100%; height: 15%; background: yellow;}
            nav {width: 15%; height: 70%; float: left; background: orange;}
            section {width: 70%; height: 70%; float: left; background: olivedrab;}
            aside {width: 15%; height: 70%; float: left; background: plum;}
            footer {width: 100%; height: 15%; clear: both; background: plum;}
        </style>
    </head>
    <body>
        <header>header</header>
        <nav>nav</nav>
        <section>section</section>
        <aside>aside</aside>
        <footer>footer</footer>
    </body>
</html>
```
<br>
<!DOCTYPE html>
<html>
    <head>
        <meta charset = "utf-8">
        <title>
            HTML5 문서 구조 시맨틱 태그 사용
        </title>
        <style>
            html, body {margin: 0; padding: 0; height: 100%;}
            header {width: 100%; height: 15%; background: yellow;}
            nav {width: 15%; height: 70%; float: left; background: orange;}
            section {width: 70%; height: 70%; float: left; background: olivedrab;}
            aside {width: 15%; height: 70%; float: left; background: plum;}
            footer {width: 100%; height: 15%; clear: both; background: plum;}
        </style>
    </head>
    <body>
        <header>header</header>
        <nav>nav</nav>
        <section>section</section>
        <aside>aside</aside>
        <footer>footer</footer>
    </body>
</html>

---
## 4. 시맨틱 블록 태그
* <figure\>
    * 본문에 삽입된 그림을 블록화 하는 시맨틱 태그. 이미지, 동영상, 소스 코드 등 컨텐츠를 블록화 가능
```
<!DOCTYPE html>
<html>
<head>
<meta charset = "utf-8">
</head>
<body>
<h3>figure 태그 활용></h3>
<hr>
<figure id = "1-1">
    <figcaption>alert() 함수 활용</figcaption>
    <pre>
        <code>function f() {alert("경고합니다");}</code>
    </pre>
    <hr>
    <small>실행결과</small>
    <pre>
        <img src = 'media/alert.png' alt = "실행결과">
    </pre>
</figure>
</body>
</html>
```
