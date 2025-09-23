import streamlit as st
import matplotlib.pyplot as plt
import koreanize_matplotlib

# --- 페이지 설정 ---
st.set_page_config(
    page_title="데이터 탐정단 프로젝트 대시보드",
    page_icon="🕵️‍♂️",
    layout="wide"
)

# --- 데이터 저장 ---
# 각 차시별 데이터
sessions = {
    "phase1": [
        {"id": 1, "title": "1차시: 데이터 탐정단, 임무를 파악하라!", "goals": ["데이터의 개념과 필요성, 그리고 데이터 윤리의 중요성을 설명할 수 있다.", "우리 팀만의 '탐정 사무소'를 결성하고 역할을 정할 수 있다.", "'탐정 사무소 설립 보고서'를 작성하고 소개할 수 있다."]},
        {"id": 2, "title": "2차시: 첫 사건 파일, 진짜 문제를 찾아라!", "goals": ["'탐정의 나침반' 기준(흥미, 측정 가능성)에 따라 탐구 주제를 1가지 선정할 수 있다.", "'질문 깔때기' 기법을 활용하여, 주제를 데이터로 측정 가능한 핵심 질문으로 바꿀 수 있다."]},
        {"id": 3, "title": "3차시: 최고의 기획안을 만들어라!", "goals": ["좋은 질문과 나쁜 질문의 차이를 구별하고 설명할 수 있다.", "질문의 목적에 따라 객관식, 체크박스, 척도 등 다양한 질문 유형을 올바르게 사용할 수 있다.", "동료 검토를 통해 설문지를 완성할 수 있다."]}
    ],
    "phase2": [
        {"id": 4, "title": "4차시: 데이터 쿡방, 최고의 재료를 준비하라!", "goals": ["데이터 정제가 왜 필수적인 과정인지 설명할 수 있다.", "구글 시트의 '필터', '찾기 및 바꾸기' 기능으로 데이터를 깨끗하게 만들 수 있다.", "COUNTIF 함수를 사용하여 기초 통계를 낼 수 있다."]},
        {"id": 5, "title": "5차시: 데이터 셰프, 숫자를 요리하라!", "goals": ["데이터 시각화의 중요성을 설명할 수 있다.", "데이터의 목적에 따라 막대 차트와 원 차트를 선택하고 만들 수 있다."]},
        {"id": 6, "title": "6차시: 미슐랭 스타의 조건, 최고의 차트로 설득하라!", "goals": ["좋은 차트의 3대 요소(제목, 축 레이블, 범례)를 적용하여 차트를 개선할 수 있다.", "색상 등 디자인 요소를 활용하여 데이터의 핵심 메시지를 효과적으로 강조할 수 있다."]},
        {"id": 7, "title": "7차시: 비밀 레시피, 데이터의 '환상의 조합'을 찾아라!", "goals": ["단순 사실과 '인사이트'의 차이점을 설명할 수 있다.", "'피벗 테이블'을 이용하여 데이터를 교차 분석하고 숨겨진 패턴을 발견할 수 있다."]},
        {"id": 8, "title": "8차시: 총괄 셰프의 결단, '시그니처 코스 메뉴'를 개발하라!", "goals": ["분석한 모든 결과를 종합하여 전체 스토리를 파악할 수 있다.", "데이터에 근거하여 문제에 대한 구체적인 해결책을 도출할 수 있다."]}
    ],
    "phase3": [
        {"id": 9, "title": "9차시: 데이터 셰프 코리아, 결승 무대를 빛내라!", "goals": ["데이터 스토리텔링의 5단계 구조를 이해하고 설명할 수 있다.", "분석 결과를 5단계 스토리 구조에 맞게 재구성하여 '발표 스토리보드'를 완성할 수 있다."]},
        {"id": 10, "title": "10차시: 최종 리허설, 최고의 무대를 준비하라!", "goals": ["좋은 발표 자료와 나쁜 발표 자료의 차이를 설명할 수 있다.", "스토리보드를 바탕으로 실제 발표 자료(구글 슬라이드) 1차 완성본을 제작할 수 있다."]},
        {"id": 11, "title": "11차시: 우승을 향한 마지막 점검!", "goals": ["동료들 앞에서 발표를 연습하고 건설적인 피드백을 주고받을 수 있다.", "예상 질문을 만들고 데이터에 기반한 답변을 준비할 수 있다."]},
        {"id": 12, "title": "12차시: 데이터, 세상을 바꾸는 레시피! 최종 결승전!", "goals": ["12주간의 프로젝트 결과물을 바탕으로 최종 해결책을 자신감 있게 발표할 수 있다.", "프로젝트 전체 과정을 되돌아보며 데이터 분석의 의미를 스스로 정리하고 성찰할 수 있다."]}
    ]
}

# 차트 시뮬레이션 데이터
food_data = {
    'labels': ['돈까스', '스파게티', '떡볶이', '김치찌개', '비빔밥'],
    'all': [50, 30, 25, 15, 10],
    'low': [60, 25, 20, 5, 5],
    'high': [40, 35, 30, 25, 15]
}

insight_texts = {
    'all': "전체 학년에서 '돈까스'가 압도적인 1위를 차지했습니다.",
    'low': "저학년은 '돈까스'에 대한 선호도가 매우 높은 반면, 한식 메뉴는 선호도가 낮습니다.",
    'high': "고학년은 '돈까스' 선호도가 여전히 높지만, 저학년에 비해 '스파게티', '김치찌개' 등 다양한 메뉴를 선호합니다."
}

# 핵심 개념 데이터
concepts = {
    "데이터": "짐작이 아닌, 증거에 기반하여 문제를 해결하게 해주는 강력한 무기 (숫자, 글자, 위치 등)",
    "데이터 윤리": "개인의 비밀이 아닌, 모두를 위한 해결책을 찾기 위해 반드시 익명의 정보를 다뤄야 한다는 규칙",
    "데이터 정제": "분석하기 전, 오타나 오류 등 '더러운 데이터'를 '깨끗한 데이터'로 만드는 필수 과정",
    "시각화": "숫자 목록을 한눈에 이해할 수 있는 차트(요리)로 만드는 과정. 최고의 '플레이팅' 기술!",
    "피벗 테이블": "데이터를 두 가지 이상의 기준으로 손쉽게 조합하고 요약해주는 '마법의 레시피 조합기'. 인사이트 발견을 위한 강력한 도구!",
    "인사이트": "단순 사실을 넘어, 데이터 속 숨겨진 관계나 패턴을 발견하는 것('환상의 맛 조합'). '아하!'하는 깨달음을 주는 새로운 발견!",
    "스토리텔링": "데이터를 논리적인 순서와 감동적인 메시지로 엮어, 청중을 설득하는 기술"
}
concept_keys = list(concepts.keys())

# --- 세션 상태 초기화 ---
if 'active_filter' not in st.session_state:
    st.session_state.active_filter = 'all'
if 'selected_concept' not in st.session_state:
    st.session_state.selected_concept = '데이터'


# --- UI 그리기 ---
st.markdown("""
<style>
    /* 폰트 및 기본 스타일 */
    .stApp {
        background-color: #f4f4f2;
    }
    h1, h2, h3, h4, h5, h6 {
        font-weight: 900 !important;
        color: #44403c;
    }
    /* 헤더 */
    .st-emotion-cache-10trblm e1nzilvr1 {
        text-align: center;
    }
    /* 타임라인은 markdown으로 직접 구현 */
</style>
""", unsafe_allow_html=True)


# --- 헤더 ---
st.title("데이터 탐정단 프로젝트")
st.markdown("<p style='text-align: center; font-size: 1.25rem; color: #78716c;'>우리 학교를 1% 더 좋게 만들기 위한 12주간의 위대한 여정</p>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- 타임라인 네비게이션 (앵커 링크 사용) ---
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("[<h3 style='text-align:center;'>1️⃣ 수사 착수 (1-3차시)</h3>](#1-1-3-)", unsafe_allow_html=True)
with c2:
    st.markdown("[<h3 style='text-align:center;'>2️⃣ 데이터 분석 (4-8차시)</h3>](#2-4-8-)", unsafe_allow_html=True)
with c3:
    st.markdown("[<h3 style='text-align:center;'>3️⃣ 최종 발표 (9-12차시)</h3>](#3-9-12-)", unsafe_allow_html=True)

st.markdown("---")


# --- 메인 레이아웃 (콘텐츠 + 사이드바) ---
main_col, sidebar_col = st.columns([2, 1])

with main_col:
    # --- 1단계: 수사 착수 ---
    st.markdown("<a name='1-1-3-'></a>", unsafe_allow_html=True)
    st.header("1단계: 수사 착수 (1-3차시)")
    for session in sessions['phase1']:
        with st.expander(f"**{session['title']}**"):
            st.subheader("🎯 오늘의 도전")
            for goal in session['goals']:
                st.markdown(f"- {goal}")
    
    st.markdown("<br>", unsafe_allow_html=True)

    # --- 2단계: 데이터 분석 ---
    st.markdown("<a name='2-4-8-'></a>", unsafe_allow_html=True)
    st.header("2단계: 데이터 분석 (4-8차시)")
    
    with st.container(border=True):
        st.subheader("📊 데이터 시뮬레이션: 학년별 급식 선호도 분석")
        st.caption("아래 버튼을 클릭하여 학년별로 가장 좋아하는 급식 메뉴가 어떻게 다른지 직접 확인해보세요!")
        
        filter_cols = st.columns(3)
        if filter_cols[0].button("전체 학년", use_container_width=True, type="primary" if st.session_state.active_filter == 'all' else "secondary"):
            st.session_state.active_filter = 'all'
        if filter_cols[1].button("저학년", use_container_width=True, type="primary" if st.session_state.active_filter == 'low' else "secondary"):
            st.session_state.active_filter = 'low'
        if filter_cols[2].button("고학년", use_container_width=True, type="primary" if st.session_state.active_filter == 'high' else "secondary"):
            st.session_state.active_filter = 'high'
            
        # Matplotlib 차트 생성
        fig, ax = plt.subplots()
        ax.barh(food_data['labels'], food_data[st.session_state.active_filter], color='rgba(234, 88, 12, 0.6)')
        ax.invert_yaxis()
        ax.set_xlabel('학생 수 (명)')
        ax.set_title('급식 메뉴 선호도', fontweight='bold')
        st.pyplot(fig)
        
        st.info(f"**💡 분석 인사이트:** {insight_texts[st.session_state.active_filter]}")

    for session in sessions['phase2']:
        with st.expander(f"**{session['title']}**"):
            st.subheader("🎯 오늘의 도전")
            for goal in session['goals']:
                st.markdown(f"- {goal}")

    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- 3단계: 최종 발표 ---
    st.markdown("<a name='3-9-12-'></a>", unsafe_allow_html=True)
    st.header("3단계: 최종 발표 (9-12차시)")
    for session in sessions['phase3']:
        with st.expander(f"**{session['title']}**"):
            st.subheader("🎯 오늘의 도전")
            for goal in session['goals']:
                st.markdown(f"- {goal}")


with sidebar_col:
    # --- 핵심 개념 사이드바 ---
    with st.container(border=True):
        st.subheader("🔑 핵심 개념")
        
        # 버튼들을 여러 줄로 나누어 배치
        cols = st.columns(2)
        for i, key in enumerate(concept_keys):
            col = cols[i % 2]
            if col.button(key, use_container_width=True, type="primary" if st.session_state.selected_concept == key else "secondary"):
                st.session_state.selected_concept = key
        
        st.markdown("---")

        selected_title = st.session_state.selected_concept
        selected_text = concepts[selected_title]

        st.markdown(f"#### {selected_title}")
        st.write(selected_text)

