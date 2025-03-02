# SimpleBoard-project

## 소개
Django를 사용하여 간단한 게시판 기능을 구현했습니다. 홈 화면에서는 회원가입 또는 로그인이 가능하며 회원가입 및 로그인이 된 사용자만이 게시판에 접근가능합니다. 로그인이 완료된 사용자는 이미지를 포함한 게시글을 작성하고 수정 및 삭제할 수 있으며, 작성자만이 수정과 삭제 권한을 가지고 있습니다.

## 사용한 프레임워크
- Django 5.1.6
- Bootstrap

## 기능
- **사용자 인증**
  - 회원가입
  - 로그인
  - 로그아웃
- **게시글 관리**
  - 게시글 작성
  - 게시글 목록 미리보기
  - 게시글 상세 보기
  - 게시글 수정
  - 게시글 삭제
  - 자신의 게시글만 수정 및 삭제 가능
  - 삭제 확인 절차
 
## 동작화면
![로그인 전 홈 화면](https://github.com/UReWUI/SimpleBoard-project/blob/main/images/HomeBeforeLogin.png)
![로그인 전 게시판 화면](https://github.com/UReWUI/SimpleBoard-project/blob/main/images/BoardBeforeLogin.png)
![회원가입 화면](https://github.com/UReWUI/SimpleBoard-project/blob/main/images/Signup.png)
![로그인 후 게시판 화면](https://github.com/UReWUI/SimpleBoard-project/blob/main/images/BoardList.png)
![게시글 작성 화면](https://github.com/UReWUI/SimpleBoard-project/blob/main/images/PostCreate.png)
![게시판 화면(미리보기 형식 목록)](https://github.com/UReWUI/SimpleBoard-project/blob/main/images/PostCreate.png)
![게시글 삭제 확인 화면](https://github.com/UReWUI/SimpleBoard-project/blob/main/images/Delete.png)
![작성자가 아닌 경우의 화면](https://github.com/UReWUI/SimpleBoard-project/blob/main/images/NotWriter.png)
