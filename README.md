## 💡개요

- 진행기간 : 2023.11.16(목) ~ 2023.11.24(금)
- 주제 : 금융 상품 비교 애플리케이션 서비스
- 서비스명 : ***나행시(나만의 은행, 행복의 시작)***


## 서비스 소개



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


## 🛢️ DB 설계
![Alt text](image.png)


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
  - 내가 가입한 정ㅂ조를 기반으로 금융 상품 추천을 받을 수 있는 페이지 제공
  - 가입한 상품 목록을 조회할 수 페이지 제공



## 📝 금융 상품 추천 알고리즘에 대한 기술적 설명

1\. **사용자 입력 수집**:

-   사용자가 회원가입 시 입력한 정보(주 거래 은행, 가입 상품, 저축 기간 등)은 axios를 사용하여 Django 서버로 안전하게 전송됩니다.

2\. **데이터베이스 필터링 및 정렬**:

-   서버에서 전달받은 정보를 기반으로 예적금 데이터베이스에서 필터링을 수행합니다.
-   최대 우대 금리를 기준으로 한 내림차순 정렬을 수행하여 사용자에게 가장 이익이 되는 상품을 상위에 배치합니다.

3\. **상품 필터링**:

-   사용자가 이미 가입한 상품은 필터링하여 중복 제거합니다.
-   사용자가 선택한 저축 기간에 해당하는 상품만을 고려합니다.

4\. **주거래 은행 기반 필터링**:

-   사용자가 지정한 주 거래 은행에 해당하는 상품을 필터링합니다.
-   주거래 은행에 해당하는 상품이 존재하면 이를 사용자에게 제시하고, 그렇지 않은 경우에는 이전 단계에서 필터링한 내역에서 상위 3개의 상품을 추천합니다.

5\. 서비스 대표 기능들에 대한 설명

1) **예적금 금리 비교**

-   다양한 은행들의 예적금 상품 정보를 제공합니다.
-   원하는 상품을 버튼을 통해 비교함으로써 각 은행의 금리를 쉽게 확인할 수 있습니다.

2) **환율 계산기**

-   사용자가 원하는 환율을 계산할 수 있는 도구를 제공합니다.
-   간편한 인터페이스를 통해 실시간 환율 정보를 확인하고 계산할 수 있습니다.

3) **근처 은행 검색**

-   현재 위치와 은행 종류를 기반으로 근처 은행을 검색할 수 있습니다.
-   지도와 연동하여 사용자에게 가장 편리한 은행 위치를 찾을 수 있습니다.

4) **커뮤니티 (게시판)**

-   회원 간의 소통과 예적금 상품 정보 공유를 위한 게시판을 운영합니다.
-   다양한 주제로 금융에 관련된 정보를 나눌 수 있는 플랫폼을 제공합니다.

5) **프로필 페이지 (금융상품 추천 알고리즘)**

-   내가 가입한 정보를 기반으로 한 금융 상품 추천을 받을 수 있는 페이지를 제공합니다.
-   가입한 상품을 손쉽게 확인하고 관리할 수 있는 기능을 제공하며, 회원 개인정보를 쉽게 등록, 수정, 비밀번호 변경이 가능합니다.

