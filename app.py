import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

# 이미지 불러오기
pageIcon = Image.open("page_icon.png")
mainIcon= Image.open("main_icon.png")
image1 = Image.open("patturning_bg.png")
image2 = Image.open("guideline.png")

#Layout
st.set_page_config(
    page_title="PatTurning",
    layout="wide",
    page_icon=pageIcon,
    initial_sidebar_state="expanded")

#Data Pull and Functions
st.markdown("""
<style>
.big-font {
    font-size:80px !important;
}
</style>
""", unsafe_allow_html=True)



#Options Menu
with st.sidebar:
    selected = option_menu('PatTurning', ["💡Intro", '📚About','❓How To Contribute', '❗Commit Convention'], 
                           menu_icon="cast", default_index=0)


# Intro 페이지
if selected == "Intro":
    # Header
    left_col, right_col = st.columns(2)
    left_col.image(mainIcon, caption="PatTurning Icon", use_column_width=True)
    right_col.markdown("# Rascore")
    right_col.markdown("### A tool for analyzing RAS protein structures")
    right_col.markdown("**Created by Mitchell Parker and Roland Dunbrack**")
    right_col.markdown("**Fox Chase Cancer Center**")
    
    st.title('PatTurning')
    st.write("Patturning은 온라인 쇼핑몰에서 발생하는 다크 패턴을 탐지하여 사용자에게 보다 투명한 쇼핑 경험을 제공합니다.")
    st.divider()


    st.image(image1, caption="Patturning 배경 이미지", use_column_width=True)

    # 팀 소개
    st.markdown("""
    **Patturning** 팀은 경희대학교 소프트웨어융합대학 학생 5명으로 구성되어 있으며, 사용자의 합리적인 소비를 돕기 위해 다크 패턴을 감지 및 필터링하는 서비스를 개발하고 있습니다. 특히 정보 소외 계층에게 취약한 다크 패턴의 사회적 문제점을 알리려 노력합니다.
    """)
    st.divider()

    # Support & Contact 섹션
    st.header("Support & Contact")
    st.write("GitHub Repository: [Dark Pattern Detection Project](https://github.com/HyejiYu/PatTuning)")
    st.divider()

    # 라이센스
    st.header("License")
    st.write("MIT License") 
    
#Intro Page
if selected=="About":
    # 기능 소개 섹션
    st.header("Patturning의 기능")
    st.subheader("[1] 다크패턴 탐지 기능")
    st.write("""
    Patturning의 **다크 패턴 탐지 기능**을 통해 웹사이트에서 특정 문구가 등장할 때 해당 문구를 자동으로 블러 처리하여 사용자가 쉽게 인지할 수 있도록 합니다.
    """)
    st.image(image2, caption="2023년 공정거래위원회 가이드라인", use_column_width=True)

    # 다크 패턴 문구 예시 표
    st.write("다음은 저희 팀이 분류한 다크 패턴 문구 예시입니다.")
    st.table({
        "다크패턴": ["오도형", "압박형(소비유도)", "압박형(다른사람행동알림)", "압박형(긴급성)"],
        "유형": ["아니요, 정가를 지불하고 싶습니다", "45개 남음", "월간 구매 34,422개", "품절임박! 딱 4개 남았어요"]
    })

    # 가격 추적 기능 소개
    st.subheader("[2] 온라인 쇼핑몰 상품 가격 추적")
    st.write("""
    Patturning은 온라인 쇼핑몰의 상품 가격을 추적하여 소비자가 다크 패턴에 쉽게 영향을 받지 않도록 지원합니다. 
    """)
    # (여기에는 추적된 가격 변동 그래프를 추가할 수 있습니다.)

    # 다크 패턴 신고 기능 소개
    st.subheader("[3] 다크패턴 문구 신고 기능")

    # 기대 효과 섹션
    st.header("Patturning의 기대 효과")
    st.write("""
    - **소비자 보호 강화**: 비합리적인 구매 유도 행위를 차단하여 소비자의 권익을 보호합니다.
    - **윤리적인 웹 디자인**: 기업들이 윤리적인 웹 디자인을 추구하도록 유도합니다.
    - **사회적 가치 창출**: 투명한 커뮤니케이션 촉진을 통해 소비 환경 개선을 목표로 합니다.
    """)

    # 함께 하실 분 모집 섹션
    st.header("Patturning과 함께 하실 분을 모집합니다")
    st.write("""
    [1] **오픈소스 기여**: Patturning 개발에 기여할 수 있습니다. 코드 개선, 버그 수정, 새로운 기능 제안 등이 가능합니다.
    [2] **다크 패턴 관련 자문**: 윤리적 디자인과 관련된 전문가의 자문을 구하고 있습니다.
    """)
    st.write("[How to Contribute](https://www.notion.so/How-to-Contribute-7147ada1b92549538bdaa86028780734?pvs=21)")

