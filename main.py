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
    st.session_state.fortune_msg = "🔮 위의 구슬을 누르면 외계 정령이 주식 운세를 알려줍니다..."

# 페이지 설정
st.set_page_config(
    page_title="👽 왹-져 주식 침공 👽",
    page_icon="🛸",
    layout="wide"
)

# 👽 우주 대혼돈 + 날아다니는 애니메이션 CSS 스타일 👽
bg_animation = "hyperRainbow 3s linear infinite"
if st.session_state.berserk_mode:
    bg_animation = "berserkFlash 0.1s steps(2) infinite"

st.markdown(f"""
<style>
    /* [기본 무지개 배경] */
    .stApp {{
        background: linear-gradient(45deg, #ff00ff, #00ffff, #ffff00, #ff0000, #00ff00, #0000ff, #ff00ff);
        background-size: 600% 600%;
        animation: {bg_animation} !important;
    }}
    @keyframes hyperRainbow {{
        0% {{background-position: 0% 50%;}}
        50% {{background-position: 100% 50%;}}
        100% {{background-position: 0% 50%;}}
    }}
    @keyframes berserkFlash {{
        0% {{ filter: hue-rotate(0deg) invert(0); }}
        100% {{ filter: hue-rotate(360deg) invert(1); }}
    }}

    /* ----------------------------------------------------
       🚀 정신없이 날아다니는 외계인 & 효과 CSS 애니메이션
       ---------------------------------------------------- */
    .flying-object {{
        position: fixed;
        pointer-events: none; /* 💡 중요: 날아다니는 아이콘이 마우스 클릭을 막지 않도록 설정! */
        z-index: 99999;       /* 화면 가장 위에 표시 */
        font-size: 50px;
    }}

    /* 비행 경로 1 (왼쪽 아래 -> 오른쪽 위로 지그재그) */
    @keyframes zigZagFly {{
        0% {{ left: -10%; top: 80%; transform: rotate(0deg) scale(1); }}
        25% {{ left: 30%; top: 20%; transform: rotate(180deg) scale(1.5); }}
        50% {{ left: 60%; top: 70%; transform: rotate(360deg) scale(0.8); }}
        75% {{ left: 80%; top: 10%; transform: rotate(540deg) scale(2); }}
        100% {{ left: 110%; top: 50%; transform: rotate(720deg) scale(1); }}
    }}

    /* 비행 경로 2 (오른쪽 위 -> 왼쪽 아래로 회전 낙하) */
    @keyframes spinDrop {{
        0% {{ right: -10%; top: 10%; transform: rotate(0deg); }}
        50% {{ right: 50%; top: 80%; transform: rotate(-720deg) scale(2); }}
        100% {{ right: 110%; top: 90%; transform: rotate(-1440deg); }}
    }}

    /* 비행 경로 3 (아래에서 위로 수직 솟구치기) */
    @keyframes rocketUp {{
        0% {{ left: 45%; top: 110%; transform: scale(1) rotate(0deg); }}
        50% {{ left: 55%; top: 50%; transform: scale(3) rotate(20deg); }}
        100% {{ left: 40%; top: -20%; transform: scale(1) rotate(-20deg); }}
    }}

    /* 비행 경로 4 (미친듯이 화면을 튕겨다니는 핀볼 효과) */
    @keyframes pinball {{
        0% {{ left: 10%; top: 10%; }}
        20% {{ left: 90%; top: 30%; transform: rotate(90deg); }}
        40% {{ left: 20%; top: 80%; transform: rotate(180deg); }}
        60% {{ left: 80%; top: 50%; transform: rotate(270deg); }}
        80% {{ left: 40%; top: 20%; transform: rotate(360deg); }}
        100% {{ left: 10%; top: 10%; }}
    }}

    /* [컨텐츠 박스 및 폰트] */
    .content-box {{
        background-color: #000000 !important;
        border: 10px ridge #ff00ff !important;
        border-radius: 0px !important;
        padding: 25px;
        margin-bottom: 25px;
        box-shadow: 0px 0px 30px #00ff00;
    }}
    h1, h2, h3, p, span, label, .stMarkdown {{
        font-family: 'Gungsuh', 'GungsuhChe', '궁서', 'Comic Sans MS', cursive !important;
        text-shadow: 2px 2px 0px #ff0000, -2px -2px 0px #0000ff;
    }}
    .spinning-ufo {{
        display: inline-block;
        animation: spin 0.5s linear infinite;
        font-size: 50px;
    }}
    @keyframes spin {{
        100% {{ transform: rotate(-360deg); }}
    }}
    .blink-text {{
        animation: blink 0.3s step-end infinite;
        color: #ffff00;
        font-weight: bold;
        font-size: 24px;
        text-align: center;
    }}
    @keyframes blink {{
        50% {{ opacity: 0; }}
    }}
    [data-testid="stSidebar"] {{
        background-color: #00ff00 !important;
        border-right: 10px dashed #ff0000;
    }}
    [data-testid="stSidebar"] * {{
        color: #000000 !important;
        font-weight: bold !important;
    }}
</style>
""", unsafe_allow_html=True)

# 🛸 화면 위를 쉴 새 없이 날아다니는 유령 비행체들 방출!
st.markdown("""
<div class="flying-object" style="animation: zigZagFly 6s linear infinite;">🛸</div>
<div class="flying-object" style="animation: spinDrop 8s ease-in-out infinite;">👽</div>
<div class="flying-object" style="animation: rocketUp 5s ease infinite;">🚀</div>
<div class="flying-object" style="animation: pinball 12s linear infinite;">🌈</div>
<div class="flying-object" style="animation: zigZagFly 10s linear infinite; animation-delay: 2s;">💸</div>
<div class="flying-object" style="animation: spinDrop 7s ease infinite; animation-delay: 3s;">👾</div>
<div class="flying-object" style="animation: pinball 9s ease-in-out infinite; animation-delay: 1s;">✨</div>
<div class="flying-object" style="animation: rocketUp 4s linear infinite; animation-delay: 2.5s;">💥</div>
""", unsafe_allow_html=True)


# 🛸 전광판
st.markdown("""
<marquee direction="left" scrollamount="20" style="background-color: #ffff00; color: #ff0000; font-size: 30px; font-weight: bold; font-family: '궁서';">
    🚨 [비상] 외계인 주식 시장 대침공!!! 인간들아 너희들의 원화를 모두 주식에 부어라!!! 왹왹왹왹!!! 👽🛸👾🚀☄️
</marquee>
""", unsafe_allow_html=True)

# 메인 타이틀
st.markdown("""
<div style="text-align: center; margin: 30px 0;">
    <span class="spinning-ufo">🛸</span>
    <span style="font-size: 60px; color: #00ff00; font-weight: bold; text-shadow: 4px 4px 0px #ff00ff, -4px -4px 0px #00ffff;">
        왹져 주식 대전쟁 3000
    </span>
    <span class="spinning-ufo">🛸</span>
</div>
""", unsafe_allow_html=True)

st.markdown('<p class="blink-text">⚠️ 경고: 이 웹사이트는 지구인의 미적 기준을 파괴합니다. ⚠️</p>', unsafe_allow_html=True)

# ==========================================
# 🧪 비밀 실험실 (동작 버튼들)
# ==========================================
st.markdown('<div class="content-box">', unsafe_allow_html=True)
st.markdown("<h2 style='color:#00ffff; text-align:center;'>🧪 안드로메다 비밀 실험실 (절대 누르지 마시오)</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🚨 왹져 폭주 모드 가동!!! 🚨", use_container_width=True):
        st.session_state.berserk_mode = not st.session_state.berserk_mode
        st.rerun()

with col2:
    if st.button("💸 합법 주가 조작 (초급등) 💸", use_container_width=True):
        st.session_state.stock_pump = not st.session_state.stock_pump
        if st.session_state.stock_pump:
            st.toast("🔮 왹왹! 지구인 주가 무한 동력 가동!")
        else:
            st.toast("💤 주가 조작 장치 전원 꺼짐...")
        st.rerun()

with col3:
    if st.button("☄️ 지구 파괴 미사일 발사 ☄️", use_container_width=True):
        st.warning("🚀 지구 파괴 미사일 충전 시작... 피하십시오!")
        progress_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.02)
            progress_bar.progress(percent_complete + 1)
        
        fail_reasons = [
            "❌ 에러: 미사일 발사 버튼에 우주 먼지가 끼어 취소되었습니다.",
            "❌ 에러: 테슬라(TSLA) 주가가 너무 떨어져 우주선 연료비가 부족합니다.",
            "❌ 에러: 지구인들이 보낸 '김치' 냄새에 격추당했습니다.",
            "❌ 에러: 외계인 사령관이 주식 창 보느라 발사 스위치를 못 눌렀습니다."
        ]
        st.error(random.choice(fail_reasons))

st.markdown("---")
st.markdown("### 🔮 우주 주식 점성술")
if st.button("🪐 오늘의 주식 운세 보기 🪐"):
    fortunes = [
        "👽 오늘 삼성전자를 사면 외계인 우주선 승차권을 얻게 됩니다.",
        "👽 오늘은 테슬라 차트가 UFO 모양을 그릴 것입니다. 매수각입니다.",
        "👽 주식 창을 끄고 안드로메다 방향으로 절을 3번 하십시오. 평화가 올 것입니다.",
        "👽 왹왹! 오늘 당신의 계좌에 은하계 초신성이 폭발해 0원이 될 수도 있습니다.",
        "👽 우주의 기운이 당신의 매도를 막고 있습니다. 존버하십시오."
    ]
    st.session_state.fortune_msg = random.choice(fortunes)

st.info(st.session_state.fortune_msg)
st.markdown('</div>', unsafe_allow_html=True)


# ==========================================
# 📊 주식 데이터 분석 영역
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

# 사이드바
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
if st.sidebar.button("👽 우주선 납치 버튼 (절대 누르지 마시오)"):
    st.balloons()
    st.toast("🛸 왹왹왹! 지구인을 납치했다!!!")

# 데이터 시각화 메인 로직
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
        # 1. 미친 네온 차트
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.markdown("<h2 style='color:#00ff00; text-align:center;'>📈 뇌정지 수익률 배틀그라운드</h2>", unsafe_allow_html=True)

        return_fig = go.Figure()
        return_summary = []
        
        neon_colors = ["#ff00ff", "#00ffff", "#ffff00", "#ff0000", "#00ff00", "#ffffff"]

        for idx, (name, df) in enumerate(price_data.items()):
            close = df['Close']
            normalized = (close / close.iloc[0] - 1) * 100
            
            # 주가 조작 폭등 연출
            if st.session_state.stock_pump:
                normalized = normalized * 99999 + random.randint(10000, 50000)

            line_color = neon_colors[idx % len(neon_colors)]
            
            return_fig.add_trace(go.Scatter(
                x=df.index,
                y=normalized,
                mode='lines+markers',
                name=f"🛸 {name}",
                line=dict(width=4, color=line_color),
                marker=dict(size=8, symbol='star')
            ))
            final_return = float(normalized.iloc[-1])
            
            unit = "왹(WOEK)" if st.session_state.stock_pump else "% 왹!"
            return_summary.append({"종목": name, "수익률": f"{round(final_return, 2):,}{unit}"})

        return_fig.update_layout(
            plot_bgcolor='black',
            paper_bgcolor='black',
            title=dict(text="🌌 안드로메다 수익률 레이스", font=dict(color='#00ff00', size=24)),
            xaxis=dict(gridcolor='#555555', tickfont=dict(color='#00ff00')),
            yaxis=dict(gridcolor='#555555', tickfont=dict(color='#00ff00')),
            legend=dict(font=dict(color='#00ff00')),
            height=500
        )
        st.plotly_chart(return_fig, use_container_width=True)

        # 수익률 순위표
        summary_df = pd.DataFrame(return_summary)
        st.markdown("<h3 style='color:#ff00ff;'>🏆 현 시각 우주 서열 (수익률 순)</h3>", unsafe_allow_html=True)
        st.dataframe(summary_df, use_container_width=True, hide_index=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # 2. 광기의 캔들 차트
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.markdown("<h2 style='color:#ffff00; text-align:center;'>🕯️ 우주 에너지 파동 (캔들차트)</h2>", unsafe_allow_html=True)

        chart_name = st.selectbox("🛸 스캔할 지구 기업을 선택하라:", list(price_data.keys()))
        chart_df = price_data[chart_name]

        # 주가 조작 폭등 시 캔들 가격 조절
        open_val = chart_df['Open']
        high_val = chart_df['High']
        low_val = chart_df['Low']
        close_val = chart_df['Close']
        if st.session_state.stock_pump:
            open_val *= 12345
            high_val *= 12345
            low_val *= 12345
            close_val *= 12345

        candle_fig = go.Figure(data=[go.Candlestick(
            x=chart_df.index,
            open=open_val,
            high=high_val,
            low=low_val,
            close=close_val,
            increasing_line_color='#ff00ff',
            decreasing_line_color='#00ffff'
        )])
        
        candle_fig.update_layout(
            plot_bgcolor='black',
            paper_bgcolor='black',
            title=dict(text=f"☄️ {chart_name} 에너지 분출 강도", font=dict(color='#ffff00', size=24)),
            xaxis=dict(gridcolor='#555555', tickfont=dict(color='#ffff00'), rangeslider_visible=False),
            yaxis=dict(gridcolor='#555555', tickfont=dict(color='#ffff00')),
            height=450
        )
        st.plotly_chart(candle_fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    else:
        st.error("👽 지구 인터넷이 너무 느리다!!! 으아아아아악!!! 🛸")

# 왹져 전용 푸터
st.markdown("""
<div style="background-color: #000000; border: 5px dashed #00ff00; padding: 20px; text-align: center; margin-top: 50px;">
    <p style="color: #ff00ff; font-size: 20px;">🛸 본 앱은 당곡고등학교 왹져 연구소에서 개발되었습니다. 🛸</p>
    <p style="color: #00ffff; font-size: 14px;">Copyright © 3026 Alien Investment Group. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
