## 💡개요

- 진행기간 : 2023.11.16(목) ~ 2023.11.24(금)
- 주제 : 금융 상품 비교 애플리케이션 서비스
- 서비스명 : ***나행시(나만의 은행, 행복의 시작)***
<br>

## 📝 서비스 소개
- 내가 가입한 정보를 기반으로 금융 상품을 추천함
- 
<br>

## 👨 팀원 소개 및 역할

- 김경범 😊
  - 사이트 디자인 및 CSS
  - 에적금 상품 조회 및 상세 조회
  - 회원 커스터마이징

- 이현직 🙂
  - 로고 디자인, 홈페이지 디자인 및 CSS
  - 커뮤니티 기능 구현
  - 근처에 있는 은행 찾기 기능 구현

- 조수현 🤗
  - 환율 계산기 기능 구현
  - 회원 정보 수정, 비밀번호 변경, 회원 탈퇴 기능 구현
  - 예적금 상품 추천 알고리즘 구현
<br>


## 🖥️ 개발 환경

- Backend
  - django 4.2.4
- Frontend
  - vue.js 3.3.4
  - vite 4.4.11
<br>


## 🛠️ 기술 스택

### Backend
![Django](https://img.shields.io/badge/Django-092E20.svg?style=for-the-badge&logo=django&logoColor=white)&nbsp;
![Python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)&nbsp;
![sqlite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=nodedotjs&logoColor=white)&nbsp;


### Frontend
![Vite](https://img.shields.io/badge/vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)&nbsp;
![Vue.js](https://img.shields.io/badge/vue.js-4FC08D?style=for-the-badge&logo=vuedotjs&logoColor=white)&nbsp;
![Html5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)&nbsp;
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)&nbsp;
![Vuetify](https://img.shields.io/badge/Vuetify-1867C0?style=for-the-badge&logo=vuetify&logoColor=white)&nbsp;


### DevOps
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)&nbsp;
![GitLab](https://img.shields.io/badge/GitLab-FC6D26?style=for-the-badge&logo=gitlab&logoColor=white)&nbsp;


### Tools
![Notion](https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white)&nbsp;
![VS code](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)&nbsp;
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)&nbsp;
<br>


## 🛢️ DB 설계
![image](https://github.com/chosuhyeon0812/FinancialPJT/assets/119795734/a9ad51b7-786b-4184-b011-201c5961f089)

<br>


## 💪 주요 기능

- 예적금 금리 비교
  - 예적금 상품 정보를 다양한 은행에서 제공하고, 사용자가 원하는 상품을 선택하여 비교할 수 있는 기능 개발
  - 상품 비교는 사용자가 선택한 기준에 따라 정렬되며, 최대 우대 금리가 높은 순으로 내림차순 정렬


- 환율 계산기
  - 외부 API를 통해 실시간으로 가져오며, 사용자의 입력에 따라 계산되어 화면에 표시됨
  - 사용자가 환율을 계산할 수 있는 간쳔한 도구를 제공


- 근처 은행 검색
  - KaKao Map API를 이용하여 현재 위치에사 가장 가까운 은행 위치를 검색하고 표시
  - 지도를 활용하여 사용자의 현재 위치 주변에 있는 은행 위치를 마커로 표시


- 커뮤니티(게시판)
  - 회원들 간의 소통과 예적금 상품에 대한 정보 공유를 위한 게시판 개발
  - 사용자들이 글을 작성하고 댓글을 남길 수 있는 인터페이스 설계


- 프로필 페이지 (금융상품 추천 알고리즘)
  - 내가 가입한 정보를 기반으로 금융 상품 추천을 받을 수 있는 페이지 제공
  - 가입한 상품 목록을 조회할 수 페이지 제공



