🌏 Languages: [한국어](README.md) | [English](README_original_en.md)

---

깃허브에 저장소를 새로 만들고 전체 폴더를 올리는 과정입니다. 

<details>
<summary><b>0단계: 깃 사용자 정보 설정 (이 컴퓨터에서 최초 1회만)</b></summary>

---

깃은 커밋마다 “누가 남긴 기록인지”를 함께 저장합니다. 사용자 정보 설정이 없으면 3번 커밋에서 `Please tell me who you are.` 에러로 멈춥니다.
~~~
git config --global user.name 
~~~
~~~
git config --global user.email 
~~~

>ex)  
>git config --global user.name "본인_영문이름_또는_깃허브_아이디"  
>git config --global user.email "깃허브에_가입한_이메일"  

<details>
<summary><b>설정 여/부 확인 방법</b></summary>
   
~~~
git config --global --list
~~~

</details>

<details>
<summary><b>사용자 정보 설정은 실제 로그인 과정이 아닙니다.</b></summary> 

```
* 이 단계는 실제 로그인이 아닙니다. 깃허브 계정 인증은 6번 git push에서 따로 진행됩니다.
* 여기 적은 이메일이 깃허브 가입 이메일과 다르면 커밋이 내 프로필(GitHub 계정)에 연결되지 않습니다.  
* 커밋에 박힌 이메일은 공개 저장소에 영구히 남습니다.  
* 개인 이메일을 숨기려면 깃허브 Settings → Emails의 12345678+아이디@users.noreply.github.com 주소를 쓰세요.  
* 학교·공용 컴퓨터라면 --global을 빼고 해당 폴더 안에서 실행하세요.
```

</details>

</details>

---

# 1단계: 깃허브 웹사이트에서 레포지토리 만들기

   1. 깃허브(Github.com)에 로그인합니다.
   2. 오른쪽 상단의 + 버튼을 누르고 New repository를 선택합니다.
   3. Repository name에 CODYSSEY_2_ProJect를 입력합니다.
   4. 다른 설정(README, .gitignore 등)은 체크하지 말고 비워둔 채 맨 아래 Create repository를 누릅니다.
   5. 화면에 나오는 주소창에서 https://github.com 형태의 저장소 주소를 복사합니다.

---

# 2단계: 컴퓨터 터미널에서 명령어 입력하기
올리려는 폴더 안에서 터미널(Git Bash 또는 CMD)을 열고,    

아래 명령어의 `"쌍따옴표(큰따옴표)_사이에_있는_곳"` 따옴표 내부 글자에 떠오르는 어떤 단어든지 적어주세요.  
("쌍따옴표(큰따옴표)_사이에_있는_곳" 에는 따옴표를 남겨두신채, 내용만 비워두셔도 됩니다)    

그리고, `[복사한_깃허브_저장소_주소를_뒤에_붙여넣으세요]` 에는 본인이 직접 복사한 주소를 붙여넣어 실행하세요.  
(우리는 이미 '1단계: 깃허브 웹사이트에서 레포지토리 만들기' 에서 깃허브 링크를 복사 했었습니다.)  

## 0. 기존에 잘못 연결된 명령어(연결 주소) 삭제
~~~
git remote remove origin
~~~

## 1. 현재 폴더를 깃 저장소로 초기화
~~~
git init
~~~

## 2. 폴더 내 모든 파일을 업로드 대기 상태로 추가

~~~
git add .
~~~

## 3. 세이브포인트 기록 생성

~~~
git commit -m
~~~

>ex)  
>git commit -m "쌍따옴표(큰따옴표)_사이에_있는_곳_에는_제목으로_올리고_싶은_것_아무거나_적으셔도_상관_없습니다."  

## 4. 기본 브랜치 이름을 main으로 변경

~~~
git branch -M main
~~~

## 5. 내 컴퓨터와 깃허브 저장소 연결

~~~
git remote add origin
~~~

>ex)  
>git remote add origin [복사한_깃허브_저장소_주소를_뒤에_붙여넣으세요]  

## 6. 깃허브로 최종 파일 전송 (로그인 창이 뜨면 로그인 진행)

~~~
git push -u origin main
~~~

------------------------------

# 👨‍💻 막히는 부분이 있다면 알려주세요:

Developed by

 [https://github.com/seongbin45](https://github.com/seongbin45)

------------------------------
