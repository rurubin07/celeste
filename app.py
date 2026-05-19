import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="CELESTE 축제 부스 안내",
    page_icon="🎪",
    layout="centered"
)

# -----------------------------
# 모바일 스타일
# -----------------------------
st.markdown("""
<style>
    .main .block-container {
        padding-top: 1rem;
        padding-left: 1rem;
        padding-right: 1rem;
        max-width: 500px;
    }

    div.stButton > button {
        width: 100%;
        height: 3.2rem;
        border-radius: 14px;
        font-size: 1rem;
        font-weight: 700;
        margin-bottom: 0.4rem;
    }

    .booth-card {
        padding: 1rem;
        border-radius: 16px;
        background-color: #f7f7f7;
        border: 1px solid #e5e5e5;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 배치도 이미지
# -----------------------------
MAP_IMAGE = "map.jpg"

# -----------------------------
# 부스 데이터
# -----------------------------
booths = {

    "인공지능": {
        "location": "운동장 왼쪽 라인",
        "desc": "인공지능학과 부스입니다.",
        "instagram": "https://www.instagram.com/cuk_ai_?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
        "images": ["images/ai.jpg"]
    },

    "대패": {
        "location": "운동장 왼쪽 라인",
        "desc": "대패 부스입니다.",
        "images": []
    },

    "철학": {
        "location": "운동장 왼쪽 라인",
        "desc": "철학과 부스입니다.",
        "instagram": "https://www.instagram.com/cuk_philosophy?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
        "images": ["images/phi1.jpg", "images/phi2.jpg", "images/phi3.jpg"]
    },

    "법학": {
        "location": "운동장 왼쪽 라인",
        "desc": "법학과 부스입니다.",
        "instagram": "https://www.instagram.com/cuk_law_?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
        "images": ["images/law1.jpg", "images/law2.jpg", "images/law3.jpg"]
    },

    "특교": {
        "location": "운동장 왼쪽 라인",
        "desc": "특수교육과 부스입니다.",
        "instagram": "https://www.instagram.com/cuk__vrse?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
        "images": ["images/vrse.jpg"]
    },

    "중문": {
        "location": "운동장 왼쪽 라인",
        "desc": "중국언어문화학과 부스입니다.",
        "instagram": "https://www.instagram.com/cuk_chinese?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
        "images": ["images/chi.jpg"]
    },

    "심리": {
        "location": "운동장 왼쪽 라인",
        "desc": "심리학과 부스입니다.",
        "instagram": "https://www.instagram.com/cuk_psychology?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
        "images": ["images/psy1.jpg", "images/psy2.jpg"]
    },

    "영문": {
        "location": "운동장 왼쪽 라인",
        "desc": "영어영문학부 부스입니다.",
        "instagram": "https://www.instagram.com/cuk_english?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
        "images": ["images/eng.jpg"]
    },

    "의생명": {
        "location": "운동장 왼쪽 라인",
        "desc": "의생명과학과 부스입니다.",
        "instagram": "https://www.instagram.com/cuk_med_bioscience?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
        "images": ["images/med1.jpg", "images/med2.jpg", "images/med3.jpg"]
    },

    "더게임/회계": {
        "location": "운동장 왼쪽 라인",
        "desc": "더게임/회계 부스입니다.",
        "instagram": "https://www.instagram.com/cuk_accounting?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
        "images": ["images/acc1.jpg", "images/acc2.jpg"]
    },

    "획/국제": {
        "location": "운동장 왼쪽 라인",
        "desc": "획/국제 부스입니다.",
        "instagram": "https://www.instagram.com/astroke_official?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
        "instagram2": "https://www.instagram.com/cuk_sis?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
        "images": ["images/sis1.jpg", "images/sis2.jpg"]
    },

    "바스타즈": {
        "location": "운동장 왼쪽 라인",
        "desc": "바스타즈 부스입니다.",
        "instagram": "https://www.instagram.com/cuk_bastards?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
        "images": ["images/bas1.jpg", "images/bas2.jpg"]
    },

    "국문": {
        "location": "운동장 왼쪽 라인",
        "desc": "국어국문학과 부스입니다.",
        "instagram": "https://www.instagram.com/cuk_kll?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
        "images": ["images/kor1.jpg", "images/kor2.jpg"]
    },

    "생과대": {
        "location": "운동장 왼쪽 라인",
        "desc": "생활과학대학 부스입니다.",
        "instagram": "https://www.instagram.com/cuk_living.sciences?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
        "images": ["images/ls1.jpg", "images/ls2.jpg"]
    },

    "국사": {
        "location": "운동장 오른쪽 라인",
        "desc": "국사학과 부스입니다.",
        "instagram": "https://www.instagram.com/cuk_history?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
        "images": ["images/his.jpg"]
    },

    "바메솦": {
        "location": "운동장 오른쪽 라인",
        "desc": "바이오메디컬소프트웨어학과 부스입니다.",
        "instagram": "https://www.instagram.com/cuk_bmsw?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
        "images": ["images/bmcs.jpg"]
    },

    "컴공": {
        "location": "운동장 오른쪽 라인",
        "desc": "컴퓨터정보공학부 부스입니다.",
        "instagram": "https://www.instagram.com/cuk.csie?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
        "images": ["images/com.jpg"]
    },

    "생공": {
        "location": "운동장 오른쪽 라인",
        "desc": "생명공학과 부스입니다.",
        "instagram": "https://www.instagram.com/cuk_biotech?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
        "images": ["images/bt1.jpg", "images/bt2.jpg", "images/bt3.jpg"]
    },

    "일문": {
        "location": "운동장 오른쪽 라인",
        "desc": "일어일본문화학과 부스입니다.",
        "instagram": "https://www.instagram.com/cuk_japan?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
        "images": ["images/jap.jpg"]
    },

    "경영": {
        "location": "운동장 오른쪽 라인",
        "desc": "경영학과 부스입니다.",
        "instagram": "https://www.instagram.com/cuk.business?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
        "images": []
    },

    "예환공": {
        "location": "운동장 오른쪽 라인",
        "desc": "에너지환경공학과 부스입니다.",
        "instagram": "https://www.instagram.com/cuk_energy_envtech?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
        "images": ["images/eh1.jpg", "images/eh2.jpg", "images/eh3.jpg", "images/eh4.jpg", "images/eh5.jpg"]
    },

    "미콘": {
        "location": "운동장 오른쪽 라인",
        "desc": "미디어기숧콘텐츠학과 부스입니다.",
        "instagram": "https://www.instagram.com/cuk_mtc?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
        "images": ["images/mc1.jpg", "images/mc2.jpg"]
    },

    "정통": {
        "location": "운동장 오른쪽 라인",
        "desc": "정보통신전자공학부 부스입니다.",
        "instagram": "https://www.instagram.com/cuk.ice?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
        "images": ["images/ice.jpg"]
    },

    "바메화공": {
        "location": "운동장 오른쪽 라인",
        "desc": "바이오메디컬화학공학과 부스입니다.",
        "instagram": "https://www.instagram.com/cuk_bmce?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
        "images": ["images/bmce1.jpg", "images/bmce2.jpg"]
    },

    "사회": {
        "location": "운동장 오른쪽 라인",
        "desc": "사회학과 부스입니다.",
        "instagram": "https://www.instagram.com/cuk_socio?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
        "images": ["images/soc.jpg"]
    },

    "데사": {
        "location": "운동장 오른쪽 라인",
        "desc": "데이터사이언스학과 부스입니다.",
        "instagram": "https://www.instagram.com/cuk_datascience?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
        "images": ["images/dcs1.jpg", "images/dcs2.jpg", "images/dcs3.jpg"]
    },

    "소피바라": {
        "location": "운동장 오른쪽 라인",
        "desc": "소피바라 부스입니다.",
        "instagram": "https://www.instagram.com/sophiebarat_cuk?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
        "images": ["images/sop.jpg"]
    },
}

# -----------------------------
# 세션 상태
# -----------------------------
if "selected_booth" not in st.session_state:
    st.session_state.selected_booth = None

# -----------------------------
# 제목
# -----------------------------
st.title("🎪 CELESTE 부스 안내")
st.caption("가톨릭대학교 축제 주점 · 메뉴 안내")

# -----------------------------
# 상세 페이지
# -----------------------------
if st.session_state.selected_booth:

    booth_name = st.session_state.selected_booth
    booth = booths[booth_name]

    if st.button("← 뒤로가기"):
        st.session_state.selected_booth = None
        st.rerun()

    st.markdown(f"## {booth_name}")

with st.container(border=True):

    st.markdown("**📍 위치**")
    st.write(
        booth.get(
            "location",
            "위치 정보 없음"
        )
    )

    st.markdown("**📝 설명**")
    st.write(
        booth.get(
            "desc",
            "설명 없음"
        )
    )

    # 인스타 버튼
    if booth.get("instagram"):

        st.link_button(
            "📸 인스타그램",
            booth["instagram"],
            use_container_width=True
        )

    # 추가 인스타 버튼
    if booth.get("instagram2"):

        st.link_button(
            "📸 추가 인스타그램",
            booth["instagram2"],
            use_container_width=True
        )

    st.markdown("### 📋 메뉴판")

    for image_path in booth["images"]:

        if Path(image_path).exists():

            st.image(
                image_path,
                use_container_width=True
            )

        else:

            st.warning(f"이미지 없음: {image_path}")

    st.stop()

# -----------------------------
# 메인 페이지
# -----------------------------
st.markdown("### 🗺️ 부스 배치도")

if Path(MAP_IMAGE).exists():
    st.image(MAP_IMAGE, use_container_width=True)

# -----------------------------
# 검색
# -----------------------------
st.markdown("### 🔍 부스 검색")

keyword = st.text_input(
    "부스명을 입력하세요",
    placeholder="예: 컴공, 바메화공"
)

filtered_booths = [
    name for name in booths
    if keyword.strip() in name
]

# -----------------------------
# 버튼 배치
# -----------------------------
st.markdown("### 🍻 부스 선택")

left_booths = [
    "인공지능",
    "대패",
    "철학",
    "법학",
    "특교",
    "중문",
    "심리",
    "영문",
    "의생명",
    "더게임/회계",
    "획/국제",
    "바스타즈",
    "국문",
    "생과대"
]

right_booths = [
    "국사",
    "바메숲",
    "컴공",
    "생공",
    "일문",
    "경영",
    "예환공",
    "미콘",
    "정통",
    "바메화공",
    "사회",
    "데사",
    "소피바라"
]

col1, col2 = st.columns(2)

with col1:
    for booth in left_booths:

        if booth in filtered_booths:

            if st.button(
                booth,
                use_container_width=True
            ):
                st.session_state.selected_booth = booth
                st.rerun()

with col2:
    for booth in right_booths:

        if booth in filtered_booths:

            if st.button(
                booth,
                use_container_width=True
            ):
                st.session_state.selected_booth = booth
                st.rerun()
