﻿# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define e = Character('조리(실무)사', color="#c8ffc8")
define a = Character('식판요정', color="#c8ffc8")

# 여기에서부터 게임이 시작합니다.
label start:

    #e "새로운 렌파이 게임을 만들었군요."

    #e "이야기와 그림, 음악을 더하면 여러분의 게임을 세상에 배포할 수 있어요!"

    e '좋아, 일단 장화, 팔토시, 고무장갑, 모자, 마스크 모두 착용 완료!'
    e '그리고... 채소들은 세척과 소독도 다 했으니, 이제 야채절단기로 당근과 양파를 슬라이스 해볼까?'

    return
