import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="CELESTE 축제 부스 안내",
    page_icon="🎪",
    layout="centered"
)

# -----------------------------
# 기본 스타일: 모바일 보기 최적화
# -----------------------------
st.markdown("""
<style>
    .main .block-container {
        padding-top: 1.2rem;
        padding-left: 1rem;
        padding-right: 1rem;
        max-width: 480px;
    }
    div.stButton > button {
        width: 100%;
        height: 3.2rem;
        border-radius: 14px;
        font-size: 1.05rem;
        font-weight: 700;
        margin-bottom: 0.35rem;
    }
    .booth-card {
        padding: 1rem;
        border-radius: 18px;
        background: #f7f9fb;
        border: 1px solid #e5e7eb;
        margin-bottom: 1rem;
    }
    .small-text {
        color: #666;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 이미지 파일 경로
# GitHub에 아래 구조로 올리면 됨
# app.py
# map.jpg
# images/부스메뉴사진.jpg
# -----------------------------
MAP_IMAGE = "map.jpg"

booths = {
    "인공지능": {
        "location": "운동장 왼쪽 라인",
        "desc": "인공지능학과 부스입니다.",
        "images": []
    },
    "대패": {
        "location": "운동장 왼쪽 라인",
        "desc": "대패 부스입니다.",
        "images": []
    },
    "철학": {
        "location": "운동장 왼쪽 라인",
        "desc": "철학과 부스입니다.",
        "images": []
    },
    "법학": {
        "location": "운동장 왼쪽 라인",
        "desc": "법학과 부스입니다.",
        "images": []
    },
    "특교": {
        "location": "운동장 왼쪽 라인",
        "desc": "특수교육과 부스입니다.",
        "images": []
    },
    "중문": {
        "location": "운동장 왼쪽 라인",
        "desc": "중국언어문화학과 부스입니다.",
        "images": []
    },
    "심리": {
        "location": "운동장 왼쪽 라인",
        "desc": "심리학과 부스입니다.",
        "images": []
    },
    "영문": {
        "location": "운동장 왼쪽 라인",
        "desc": "영어영문학부 부스입니다.",
        "images": []
    },
    "의생명": {
        "location": "운동장 왼쪽 라인",
        "desc": "의생명과학과 부스입니다.",
        "images": []
    },
    "더게임/회계": {
        "location": "운동장 왼쪽 라인",
        "desc": "더게임/회계 부스입니다.",
        "images": []
    },
    "화/국제": {
        "location": "운동장 왼쪽 라인",
        "desc": "화학/국제 부스입니다.",
        "images": []
    },
    "바스타즈": {
        "location": "운동장 왼쪽 라인",
        "desc": "바스타즈 부스입니다.",
        "images": []
    },
    "국문": {
        "location": "운동장 왼쪽 라인",
        "desc": "국어국문학과 부스입니다.",
        "images": []
    },
    "생과대": {
        "location": "운동장 왼쪽 라인",
        "desc": "생활과학대학 부스입니다.",
        "images": []
    },
    "국사": {
        "location": "운동장 오른쪽 라인",
        "desc": "국사학과 부스입니다.",
        "images": []
    },
    "바메숲": {
        "location": "운동장 오른쪽 라인",
        "desc": "바메숲 부스입니다.",
        "images": []
    },
    "컴공": {
        "location": "운동장 오른쪽 라인",
        "desc": "컴퓨터공학부 부스입니다.",
        "images": []
    },
    "생공": {
        "location": "운동장 오른쪽 라인",
        "desc": "생명공학과 부스입니다.",
        "images": []
    },
    "일문": {
        "location": "운동장 오른쪽 라인",
        "desc": "일어일본문화학과 부스입니다.",
        "images": []
    },
    "경영": {
        "location": "운동장 오른쪽 라인",
        "desc": "경영학과 부스입니다.",
        "images": []
    },
    "예환공": {
        "location": "운동장 오른쪽 라인",
        "desc": "에너지환경공학과 부스입니다.",
        "images": []
    },
    "미콘": {
        "location": "운동장 오른쪽 라인",
        "desc": "미디어콘텐츠학과 부스입니다.",
        "images": []
    },
    "정통": {
        "location": "운동장 오른쪽 라인",
        "desc": "정보통신전자공학부 부스입니다.",
        "images": []
    },
    "바메화공": {
        "location": "운동장 오른쪽 라인",
        "desc": "바이오메디컬화학공학과 부스입니다.",
        "images": ["images/bmce1.jpg", "images/bmce2.jpg"]
    },
    "사회": {
        "location": "운동장 오른쪽 라인",
        "desc": "사회학과 부스입니다.",
        "images": []
    },
    "데사": {
        "location": "운동장 오른쪽 라인",
        "desc": "데이터사이언스학과 부스입니다.",
        "images": []
    },
    "소피바라": {
        "location": "운동장 오른쪽 라인",
        "desc": "소피바라 부스입니다.",
        "images": []
    },
}

# -----------------------------
# 세션 상태
# -----------------------------
if "selected_booth" not in st.session_state:
    st.session_state.selected_booth = None

# -----------------------------
# 상단 타이틀
# -----------------------------
st.title("🎪 CELESTE 부스 안내")
st.caption("가톨릭대학교 축제 주점 · 부스 메뉴 확인")

# -----------------------------
# 상세 페이지
# -----------------------------
if st.session_state.selected_booth:
    booth_name = st.session_state.selected_booth
    booth = booths[booth_name]

    if st.button("← 부스 목록으로 돌아가기"):
        st.session_state.selected_booth = None
        st.rerun()

    st.markdown(f"## {booth_name}")
    st.markdown(
        f"""
        <div class="booth-card">
            <b>📍 위치</b><br>{booth['location']}<br><br>
            <b>📝 설명</b><br>{booth['desc']}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 📋 메뉴판")
    if booth["images"]:
        for image_path in booth["images"]:
            if Path(image_path).exists():
                st.image(image_path, use_container_width=True)
            else:
                st.warning(f"이미지 파일이 없습니다: {image_path}")
    else:
        st.info("아직 등록된 메뉴판 이미지가 없습니다.")

    st.stop()

# -----------------------------
# 메인 페이지
# -----------------------------
st.markdown("### 🗺️ 부스 배치도")
if Path(MAP_IMAGE).exists():
    st.image(MAP_IMAGE, use_container_width=True)
else:
    st.info("map.jpg 파일을 업로드하면 여기에 배치도가 표시됩니다.")

st.markdown("### 🔍 부스 검색")
keyword = st.text_input("부스명을 검색하세요", placeholder="예: 컴공, 바메화공, 경영")

filtered_booths = [name for name in booths if keyword.strip() in name]
if not filtered_booths:
    st.warning("검색 결과가 없습니다.")

st.markdown("### 🍻 부스 선택")

# 모바일에서 누르기 편하게 2열 버튼 구성
for i in range(0, len(filtered_booths), 2):
    cols = st.columns(2)
    for j, col in enumerate(cols):
        if i + j < len(filtered_booths):
            name = filtered_booths[i + j]
            with col:
                if st.button(name):
                    st.session_state.selected_booth = name
                    st.rerun()

st.divider()
st.markdown("<p class='small-text'>※ 음악과 부스는 목록에서 제외했습니다.</p>", unsafe_allow_html=True)
