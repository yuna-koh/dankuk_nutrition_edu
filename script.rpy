init:
    define gui.main_menu_background = "images/start.png"

    image 조리사3 = "images/people3.png"
    image 식판요정 = "images/fairy.png"
    image 실패 = "images/sick.png"
    image 접시 = "images/dish.png"

    image bg cafe = "images/cafe.png"
    image bg clean = "images/clean.png"
    image bg end = "images/student.png"

    define e = Character('조리사(실무사)', color="#dc0c0c")
    define a = Character('식판요정', color="#a99aee")

# 여기에서부터 게임이 시작합니다.
label start:
    scene bg cafe

    play music "sound/music/hello.mp3"

    "오늘의 메뉴는 제육볶음입니다."

    "게임은 단계별로 안전하게 미션을 완수하면 급식 성공이지만 중간에 틀리면 게임 실패입니다. 안전하고, 맛있게 제육볶음을 만들어 주세요."   

    scene bg clean

    show 조리사3

    e "좋아, 오늘 배식도 무사히 마무리 했다."

    e "교차오염 방지를 위해 앞치마와 장갑도 세척실용으로 갈아입었으니 이제 식기세척기로 식판을 세척해 볼까!"

    "식기세척기 사용 방법 중 올바른 답안을 골라주세요."

    hide 조리사3

    menu:
        "가동 중인 컨베이어에 이물질이 걸리면 즉시 제거한다.":
            jump go_left

        "식판 표면의 온도는 71° C 이상이어야 한다.":
            jump go_center
            
        "식기세척기 내부 청소 시에 청소를 하고 전원을 끈다.":
            jump go_right

label go_left:
    show 실패

    play music "sound/music/fail.mp3"

    e "으악..! 내손..! 식기세척기에 손이 끼였어..."

    stop music

    e "오늘은 크게 안 다쳐서 다행이지만 다음에는 조심해야지..."

    e "앞으로는 컨베이어에 이물질이 걸리면 전원을 끄고 제거하도록 하자!"

    e "이제 남은 설거지를 마무리 해야지..."

    hide 실패

    jump final

label go_center:
    show 접시

    play music "sound/music/clear.mp3"

    e "정답이야! 식판이 깨끗하게 세척됐어! "

    stop music 

    e "식판의 표면 온도는 71° C 이상이어야 해."

    hide 접시

    jump final

label go_right:
    show 실패

    play music "sound/music/fail.mp3"

    e "으악..! 청소하기 전에 전원을 꺼야지..."

    stop music

    e "앞으로는 전원을 끄고 청소를 하도록 하고..."
    
    e "일단 남은 설거지를 마무리 하자"

    hide 실패

    jump final

label final:
    play music "sound/music/hello.mp3"

    "휴 오늘 급식 끝이다. 이제 퇴근하자..!"

    hide 조리사3

    show 식판요정

    a "식판 요정 등장!"

    a "제가 식기세척기의 올바른 사용 방법에 대해 설명해 드릴게요!"

    a "우선 세척기 작동 시 작동 설명서대로 온수 온도를 유지하며 식판이 살균되어야 해요."

    a "또한, 세척 상태가 양호한지 육안으로 확인하고, 소독제 용법, 용량을 준수해야 해요!"

    a "마지막으로 끼임 사고 예방을 위해 청소, 장해물 제거 시 반드시 전원을 차단한 후에 실시해야 해요. 우리의 소중한 손을 위해 올바르게 식기세척기를 사용합시다."

    hide 식판요정

    scene bg end

    show 식판요정 at right

    "게임은 어떠셨나요? 오늘은 안전하고 올바른 방법으로 기계를 사용하여 맛있는 급식을 학생들에게 제공할 수 있었어요!"

    "오늘의 시뮬레이션을 바탕으로 앞으로도 급식을 안전하고 맛있게 만들어 주실 거죠? 약~속!"

    return
