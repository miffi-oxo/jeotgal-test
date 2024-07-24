# jeotgal-test
## 날 오소리라 놀리는 자 철퇴를 맞을 지어다... 테스트용



 다음의 욕설탐지모듈 프로젝트 코드를 참고했습니다.
+ https://github.com/0-inf/KoreanBadwordDetection
+ https://github.com/0-inf/badwordDetection2/tree/main



## 개발 목표
 로아 디스코드에서 오소리라는 별명으로 자주 놀림을 받고 있습니다... 그러던 어느 날, 갑자기 "오소리"라는 키워드를 사용하면 자동으로 타임아웃을 시켜주는 봇을 만들고 싶어졌습니다. 그런데 만약 단순히 "오소리" 외에도, 유사한 단어들을 필터링하여 전부 타임아웃시켜준다면? 복수의 시대가 도래했다!



## 원리
 참고 링크의 설명을 읽으면 됩니다. 타임아웃과 관련한 코드는 첫 번째 KoreanBadwordDetection 프로젝트를, 필터링과 관련한 코드는 badwordDetection2 프로젝트를 참고했습니다. 



## 사용 방법
1. 디스코드 봇을 만들어 원하는 서버에 넣어줍니다.
2. Badwords.txt에 원하는 금칙어를 작성합니다.
3. 디스코드 봇 토큰이 작성된 token.txt를 생성합니다.
4. timeout.py를 실행하면 봇이 작동하는 것을 확인할 수 있습니다. (단, 관리자 권한을 가진 사람을 대상으로는 타임아웃이 적용되지 않음)



























 
