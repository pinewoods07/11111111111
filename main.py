import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import time
import random

# 1. 세션 상태(session_state) 초기화
if 'berserk_mode' not in st.session_state:
    st.session_state.berserk_mode = False
if 'stock_pump' not in st.session_state:
    st.session_state.stock_pump = False
if 'fortune_msg' not in st.session_state:
    st.session_state.fortune_msg = "🔮 정령의 전언: 돈은 있다가도 없고 없다가도 없는 것, 왹왹!"

# 페이지 설정
st.set_page_config(
    page_title="👽 안드로메다 멸망 주식 👽",
    page_icon="👾",
    layout="wide"
)

# 2. 파이썬으로 50개의 무작위 날아다니는 물체 동적 생성 🌪️
# (이렇게 파이썬 루프를 활용해 무작위 CSS 코드를 찍어내는 것은 동적 퍼블리싱의 꿀팁입니다!)
flying_html = ""
emojis = ["🛸", "👽", "🚀", "🌈", "💸", "👾", "✨", "💥", "🔥", "🦄", "☄️", "🦖", "🤪"]
for i in range(50):
    emo = random.choice(emojis)
    duration = random.randint(3, 12)  # 날아가는 속도 제각각
    delay = random.uniform(0, 5)     # 출발 시간 제각각
    scale = random.uniform(0.5, 2.5) # 크기 제각각
    # 미리 정의된 미친 애니메이션 중 무작위 배정
    anim_name = random.choice(["zigZagFly", "spinDrop", "rocketUp", "pinball", "crazyOrbit"])
    
    flying_html += f"""
    <div class="flying-object" style="
        animation: {anim_name} {duration}s linear infinite;
        animation-delay: -{delay}s;
        transform: scale({scale});
        font-size: 35px;
    ">{emo}</div>
    """

# 3. 우주 최강 지옥의 CSS 스타일시트 💥
bg_animation = "hyperRainbow 2s linear infinite"
screen_shake = ""

# 폭주 모드일 때만 전체 화면을 지진 모드로!
if st.session_state.berserk_mode:
    bg_animation = "berserkFlash 0.05s steps(2) infinite"
    screen_shake = "animation: earthquake 0.1s linear infinite;"

st.markdown(f"""
<style>
    /* 🛸 마우스 커서 외계인으로 교체! */
    html, body, [data-testid="stAppViewContainer"] {{
        cursor: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='40' height='40' style='font-size:30px'><text y='30'>🛸</text></svg>"), auto !important;
    }}

    /* 🫨 폭주모드 시 전체 웹사이트 흔들기 */
    .stApp {{
        background: linear-gradient(45deg, #ff00ff, #00ffff, #ffff00, #ff0000, #00ff00, #0000ff, #ff00ff);
        background-size: 600% 600%;
        animation: {bg_animation} !important;
        {screen_shake}
    }}

    /* ----------------------------------
       🔥 지옥의 무작위 3D 궤적 애니메이션
       ---------------------------------- */
    .flying-object {{
        position: fixed;
        pointer-events: none;
        z-index: 99999;
    }}
    @keyframes zigZagFly {{
        0% {{ left: -10%; top: 10%; transform: rotate(0deg); }}
        33% {{ left: 50%; top: 90%; transform: rotate(180deg); }}
        66% {{ left: 80%; top: 30%; transform: rotate(360deg); }}
        100% {{ left: 110%; top: 80%; transform: rotate(720deg); }}
    }}
    @keyframes spinDrop {{
        0% {{ right: -10%; top: 90%; transform: scale(1) rotate(0deg); }}
        50% {{ right: 50%; top: 10%; transform: scale(3) rotate(-360deg); }}
        100% {{ right: 110%; top: 90%; transform: scale(0.5) rotate(-720deg); }}
    }}
    @keyframes rocketUp {{
        0% {{ left: 10%; top: 110%; }}
        50% {{ left: 90%; top: -10%; }}
        51% {{ left: 90%; top: 110%; }}
        100% {{ left: 10%; top: -10%; }}
    }}
    @keyframes pinball {{
        0% {{ left: 5%; top: 5%; }}
        25% {{ left: 95%; top: 5%; }}
        50% {{ left: 95%; top: 95%; }}
        75% {{ left: 5%; top: 95%; }}
        100% {{ left: 5%; top: 5%; }}
    }}
    @keyframes crazyOrbit {{
        0% {{ left: 50%; top: 50%; transform: rotate(0deg) translate(-200px) rotate(0deg); }}
        100% {{ left: 50%; top: 50%; transform: rotate(360deg) translate(-200px) rotate(-360deg); }}
    }}

    /* 🫨 지진 발생 장치 */
    @keyframes earthquake {{
        0% {{ transform: translate(3px, 3px) rotate(0deg); }}
        20% {{ transform: translate(-3px, -3px) rotate(-1deg); }}
        40% {{ transform: translate(-5px, 0px) rotate(1deg); }}
        60% {{ transform: translate(0px, 4px) rotate(0deg); }}
        80% {{ transform: translate(3px, -2px) rotate(2deg); }}
        100% {{ transform: translate(1px, -3px) rotate(-1deg); }}
    }}

    @keyframes hyperRainbow {{
        0% {{background-position: 0% 50%;}}
        50% {{background-position: 100% 50%;}}
        100% {{background-position: 0% 50%;}}
    }}
    @keyframes berserkFlash {{
        0% {{ filter: hue-rotate(0deg) invert(0) brightness(1.5); }}
        100% {{ filter: hue-rotate(180deg) invert(1) brightness(2); }}
    }}

    /* 💥 킹받는 버튼 호버 효과 추가 */
    button {{
        transition: all 0.05s ease-in-out !important;
    }}
    button:hover {{
        transform: scale(1.4) rotate(15deg) !important;
        background-color: #ff00ff !important;
        color: #00ffff !important;
        border: 5px dashed #ffff00 !important;
        box-shadow: 0px 0px 30px #ff0000 !important;
    }}

    /* [컨텐츠 박스 & 글꼴] */
    .content-box {{
        background-color: #000000 !important;
        border: 15px double #00ffff !important;
        border-radius: 0px !important;
        padding: 25px;
        margin-bottom: 25px;
        box-shadow: 0px 0px 50px #ff00ff;
    }}
    h1, h2, h3, p, span, label, .stMarkdown, .stButton {{
        font-family: 'Gungsuh', 'GungsuhChe', '궁서', 'Comic Sans MS', cursive !important;
        text-shadow: 3px 3px 0px #ff0000, -3px -3px 0px #0000ff;
    }}
    .blink-text {{
        animation: blink 0.15s step-end infinite;
        color: #ffff00;
        font-weight: bold;
        font-size: 35px;
        text-align: center;
    }}
    @keyframes blink {{
        50% {{ opacity: 0; }}
    }}
    [data-testid="stSidebar"] {{
        background-color: #ffff00 !important;
        border-right: 15px double #ff00ff;
    }}
    [data-testid="stSidebar"] * {{
        color: #ff0000 !important;
        font-weight: 900 !important;
        font-size: 20px !important;
    }}
</style>
""", unsafe_allow_html=True)

# 🛸 50마리의 외계인 대기갑부대 투입!
st.markdown(flying_html, unsafe_allow_html=True)

# 🛸 전광판 2개 동시 발사 (하나는 왼쪽, 하나는 오른쪽으로 교차 돌진!)
st.markdown("""
<marquee direction="left" scrollamount="30" style="background-color: #ff00ff; color: #00ffff; font-size: 35px; font-weight: bold; font-family: '궁서';">
    👾 왹왹왹왹!! 지구인들아!! 무릎을 꿇어라!!! 안드로메다 연합 우주 군단 침략 개시!!! 👾
</marquee>
<marquee direction="right" scrollamount="25" style="background-color: #00ff00; color: #ff0000; font-size: 30px; font-weight: bold; font-family: '궁서';">
    🛸 [속보] 주가 폭등에 우주 연합군 전투기 연료비 조달 성공!!! 으아아아악!!! 🛸
</marquee>
""", unsafe_allow_html=True)

# 메인 타이틀
st.markdown("""
<div style="text-align: center; margin: 30px 0; transform: skew(-15deg) rotate(-2deg);">
    <span style="font-size: 80px; color: #ffff00; font-weight: bold; text-shadow: 6px 6px 0px #ff0000, -6px -6px 0px #0000ff;">
        🪐 왹져 은하 연합 금융 침공 🪐
    </span>
</div>
""", unsafe_allow_html=True)

st.markdown('<p class="blink-text">☠️ 뇌 세포가 녹아내리는 중입니다 ☠️</p>', unsafe_allow_html=True)

# ==========================================
# 🧪 비밀 실험실 (폭주 컨트롤러)
# ==========================================
st.markdown('<div class="content-box">', unsafe_allow_html=True)
st.markdown("<h2 style='color:#00ffff; text-align:center;'>🧪 외계인 비밀 과학 기지 (호버링 금지!)</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🚨 은하계 자폭 스위치 (폭주 모드) 🚨", use_container_width=True):
        st.session_state.berserk_mode = not st.session_state.berserk_mode
        st.rerun()

with col2:
    if st.button("💸 왹져 중앙은행 화폐 대발행 💸", use_container_width=True):
        st.session_state.stock_pump = not st.session_state.stock_pump
        if st.session_state.stock_pump:
            st.toast("🤑 삐리리릭... 위폐 인쇄기 풀가동!!!")
        else:
            st.toast("💤 인쇄기 고장남...")
        st.rerun()

with col3:
    if st.button("☄️ 멸망의 핵미사일 버튼 ☄️", use_container_width=True):
        st.warning("🚀 목표 좌표: 당곡고등학교 앞마당... 핵분열 충전 중!")
        progress_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.01)
            progress_bar.progress(percent_complete + 1)
        
        fail_reasons = [
            "❌ 폭발 실패: 외계 우주선 승무원들이 단체로 연차를 썼습니다.",
            "❌ 폭발 실패: 코스피(KOSPI)가 너무 하락하여 분통이 터져 미사일이 꺼졌습니다.",
            "❌ 폭발 실패: 지구인들이 급하게 뿌린 불닭볶음면 스프에 센서가 녹았습니다.",
            "❌ 폭발 실패: 주식 물려가지고 기분이 안 좋아서 왹져 대장이 취소함."
        ]
        st.error(random.choice(fail_reasons))

st.markdown("---")
st.markdown("### 🔮 우주 점성술 무당방")
if st.button("🪐 은하 점성 정령 소환 🪐"):
    fortunes = [
        "👽 오늘 삼성전자를 풀매수하지 않으면 은하수 감옥에 갇힐 것입니다.",
        "👽 엔비디아(NVDA) 주가는 사실 외계인의 음모에 의해 우상향하고 있습니다.",
        "👽 당장 주식창을 덮고 밤하늘의 카시오페아 자리를 바라보며 우십시오.",
        "👽 왹왹!! 우주의 악령이 당신의 예수금을 주시하고 있습니다!! 도망쳐!!",
        "👽 존버하십시오. 우주 법률 제42조에 의해 존버는 무조건 승리합니다."
    ]
    st.session_state.fortune_msg = random.choice(fortunes)

st.info(st.session_state.fortune_msg)
st.markdown('</div>', unsafe_allow_html=True)


# ==========================================
# 📊 주식 시장 데이터 수집 영역
# ==========================================
korea_stocks = {
    "삼성전자": "005930.KS",
    "SK하이닉스": "000660.KS",
    "현대차": "005380.KS",
    "NAVER": "035420.KS",
    "카카오": "035720.KS",
}

us_stocks = {
    "애플(Apple)": "AAPL",
    "마이크로소프트(Microsoft)": "MSFT",
    "엔비디아(NVIDIA)": "NVDA",
    "테슬라(Tesla)": "TSLA",
    "구글(Google)": "GOOGL",
}

# 사이드바 (극도로 쨍한 테마)
st.sidebar.markdown("# 👾 왹져의 지령실 👾")
market = st.sidebar.radio("🛸 지구의 영토를 고르라!", ["🇰🇷 김치 주식", "🇺🇸 버거 주식"])

stock_dict = korea_stocks if market == "🇰🇷 김치 주식" else us_stocks

selected_names = st.sidebar.multiselect(
    "🔥 네 지갑을 털어갈 종목을 고르라!! 🔥",
    options=list(stock_dict.keys()),
    default=list(stock_dict.keys())[:3]
)

period = st.sidebar.selectbox("📅 지구 시간 기준 기간", ["1mo", "3mo", "6mo", "1y"])

st.sidebar.markdown("---")
if st.sidebar.button("👽 우주선 납치 버튼"):
    st.balloons()
    st.toast("🛸 왹왹! 지구인 주식 전사 1호 납치 완료!")

# 메인 주식 계산 로직
if not selected_names:
    st.error("👽 종목을 골라라 지구인아!!! 안 고르면 지구를 폭파하겠다!!! 💣")
else:
    selected_tickers = {name: stock_dict[name] for name in selected_names}

    with st.spinner("🛸 안드로메다 망원경 조율 중... 으아아아악!!!"):
        price_data = {}
        for name, ticker in selected_tickers.items():
            try:
                df = yf.download(ticker, period=period, progress=False, multi_level_index=False)
                if not df.empty:
                    price_data[name] = df
            except Exception as e:
                st.error(f"🛸 {name} 통신 두절! : {e}")

    if price_data:
        # 1. 뇌정지 네온 수익률 레이스 차트 📊
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.markdown("<h2 style='color:#00ff00; text-align:center;'>📈 뇌정지 수익률 배틀그라운드</h2>", unsafe_allow_html=True)

        return_fig = go.Figure()
        return_summary = []
        neon_colors = ["#ff00ff", "#00ffff", "#ffff00", "#ff0000", "#00ff00", "#ffffff"]

        for idx, (name, df) in enumerate(price_data.items()):
            close = df['Close']
            normalized = (close / close.iloc[0] - 1) * 100
            
            # 💸 무한 주가 조작 (왹 소유 단위로 왜곡)
            if st.session_state.stock_pump:
                normalized = normalized * 1234567 + random.randint(50000, 150000)

            line_color = neon_colors[idx % len(neon_colors)]
            
            return_fig.add_trace(go.Scatter(
                x=df.index,
                y=normalized,
                mode='lines+markers',
                name=f"🛸 {name}",
                line=dict(width=6, color=line_color), # 대폭 굵어진 선!
                marker=dict(size=12, symbol='star-diamond') # 광란의 별다이아몬드형 마커!
            ))
            final_return = float(normalized.iloc[-1])
            
            unit = "왹(WOEK)" if st.session_state.stock_pump else "% 왹!"
            return_summary.append({"종목": name, "수익률": f"{round(final_return, 2):,}{unit}"})

        return_fig.update_layout(
            plot_bgcolor='black',
            paper_bgcolor='black',
            title=dict(text="🌌 안드로메다 수익률 레이스", font=dict(color='#00ff00', size=24)),
            xaxis=dict(gridcolor='#ff00ff', tickfont=dict(color='#00ff00')), # 핑크 그리드로 눈부시게!
            yaxis=dict(gridcolor='#00ffff', tickfont=dict(color='#00ff00')), # 파란 그리드로!
            legend=dict(font=dict(color='#00ff00')),
            height=550
        )
        st.plotly_chart(return_fig, use_container_width=True)

        # 수익률 표
        summary_df = pd.DataFrame(return_summary)
        st.markdown("<h3 style='color:#ff00ff;'>🏆 현 시각 우주 서열 (수익률 순)</h3>", unsafe_allow_html=True)
        st.dataframe(summary_df, use_container_width=True, hide_index=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # 2. 광란의 캔들 차트 🕯️
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.markdown("<h2 style='color:#ffff00; text-align:center;'>🕯️ 우주 에너지 파동 (캔들차트)</h2>", unsafe_allow_html=True)

        chart_name = st.selectbox("🛸 스캔할 지구 기업을 선택하라:", list(price_data.keys()))
        chart_df = price_data[chart_name]

        open_val = chart_df['Open']
        high_val = chart_df['High']
        low_val = chart_df['Low']
        close_val = chart_df['Close']
        if st.session_state.stock_pump:
            open_val *= 99999
            high_val *= 99999
            low_val *= 99999
            close_val *= 99999

        candle_fig = go.Figure(data=[go.Candlestick(
            x=chart_df.index,
            open=open_val,
            high=high_val,
            low=low_val,
            close=close_val,
            increasing_line_color='#00ff00', # 상승은 형광초록!
            decreasing_line_color='#ff0000'  # 하락은 피눈물 빨강!
        )])
        
        candle_fig.update_layout(
            plot_bgcolor='black',
            paper_bgcolor='black',
            title=dict(text=f"☄️ {chart_name} 에너지 분출 강도", font=dict(color='#ffff00', size=24)),
            xaxis=dict(gridcolor='#ff00ff', tickfont=dict(color='#ffff00'), rangeslider_visible=False),
            yaxis=dict(gridcolor='#00ffff', tickfont=dict(color='#ffff00')),
            height=450
        )
        st.plotly_chart(candle_fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    else:
        st.error("👽 지구 인터넷이 너무 느리다!!! 으아아아아악!!! 🛸")

# 왹져 전용 지옥의 푸터
st.markdown("""
<div style="background-color: #000000; border: 10px dashed #00ff00; padding: 20px; text-align: center; margin-top: 50px; transform: rotate(1deg);">
    <p style="color: #ff00ff; font-size: 25px;">👽 본 앱은 당곡고등학교 왹져 사령부 컴퓨터에서 작동 중입니다. 👽</p>
    <p style="color: #00ffff; font-size: 16px;">Copyright © 3026 Alien Empire. Earth Will Be Destroyed Soon.</p>
</div>
""", unsafe_allow_html=True)
