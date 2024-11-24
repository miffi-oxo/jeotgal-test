# jeotgal-test
## 날 오소리라 놀리는 자 철퇴를 맞을 지어다... 테스트용



 다음의 욕설탐지모듈 프로젝트 코드를 참고했습니다.
+ https://github.com/0-inf/KoreanBadwordDetection
+ https://github.com/0-inf/badwordDetection2/tree/main



## 개발 목표
 게임 디스코드에서 오소리라는 별명으로 놀림받고 있어 오소리 관련 키워드를 사용하면 자동으로 타임아웃을 시켜주는 봇을 만들게 되었습니다. 블랙리스트에 올라간 단어들 뿐만 아니라, 이와 유사도를 측정하여 비슷한 단어들도 타임아웃시켜주는 것을 목표로 개발하였습니다.



## 원리
 참고 링크의 설명을 읽으면 됩니다. 타임아웃과 관련한 코드는 첫 번째 KoreanBadwordDetection 프로젝트를, 필터링과 관련한 코드는 badwordDetection2 프로젝트를 참고했습니다. 



## 사용 방법
1. 디스코드 봇을 만들어 원하는 서버에 넣어줍니다.
2. Badwords.txt에 원하는 금칙어를 작성합니다.
3. 디스코드 봇 토큰이 작성된 token.txt를 생성합니다.
4. timeout.py를 실행하면 봇이 작동하는 것을 확인할 수 있습니다. (단, 관리자 권한을 가진 사람을 대상으로는 타임아웃이 적용되지 않음)

![image](https://github.com/user-attachments/assets/0525b99a-199e-46f7-83c5-93d780d3ee7f)



























 
