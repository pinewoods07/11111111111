import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import random

# 페이지 설정
st.set_page_config(
    page_title="👽 왹-져 주식 침공 👽",
    page_icon="🛸",
    layout="wide"
)

# 👽 우주 대혼돈 CSS 스타일 (눈뽕 주의!) 👽
st.markdown("""
<style>
    /* 1. 광속으로 회전하는 무지개 배경 */
    .stApp {
        background: linear-gradient(45deg, #ff00ff, #00ffff, #ffff00, #ff0000, #00ff00, #0000ff, #ff00ff);
        background-size: 600% 600%;
        animation: hyperRainbow 3s linear infinite !important; /* 3초만에 한바퀴 도는 광기의 속도 */
    }
    @keyframes hyperRainbow {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    /* 2. 외계인 궁서체 박스 (형광 초록 글씨 + 핫핑크 테두리) */
    .content-box {
        background-color: #000000 !important; /* 칠흑 같은 우주 블랙 */
        border: 10px ridge #ff00ff !important; /* 킹받는 핫핑크 입체 테두리 */
        border-radius: 0px !important; /* 둥근 모서리 금지! 각진 세기말 감성 */
        padding: 25px;
        margin-bottom: 25px;
        box-shadow: 0px 0px 30px #00ff00; /* 형광 초록 오오라 */
    }

    /* 3. 진지한 궁서체 텍스트 */
    h1, h2, h3, p, span, label, .stMarkdown {
        font-family: 'Gungsuh', 'GungsuhChe', '궁서', 'Comic Sans MS', cursive !important;
        text-shadow: 2px 2px 0px #ff0000, -2px -2px 0px #0000ff; /* 글자에 3D 적청 입체 효과 */
    }

    /* 4. 빙글빙글 도는 UFO */
    .spinning-ufo {
        display: inline-block;
        animation: spin 0.5s linear infinite;
        font-size: 50px;
    }
    @keyframes spin {
        100% { transform: rotate(-360deg); }
    }

    /* 5. 깜빡이는 텍스트 (Blink) */
    .blink-text {
        animation: blink 0.3s step-end infinite;
        color: #ffff00;
        font-weight: bold;
        font-size: 24px;
        text-align: center;
    }
    @keyframes blink {
        50% { opacity: 0; }
    }

    /* 6. 사이드바도 눈뽕 테러 */
    [data-testid="stSidebar"] {
        background-color: #00ff00 !important; /* 형광 연두색 사이드바 */
        border-right: 10px dashed #ff0000;
    }
    [data-testid="stSidebar"] * {
        color: #000000 !important;
        font-weight: bold !important;
    }
</style>
""", unsafe_allow_html=True)

# 🛸 흘러가는 전광판 (Marquee) - 보노보노 PPT의 정수!
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

# 종목 설정 (지구인들의 우량주)
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

# 사이드바 (눈을 찌르는 디자인)
st.sidebar.markdown("# 👾 왹져의 지령실 👾")
market = st.sidebar.radio("🛸 지구의 영토를 고르라!", ["🇰🇷 김치 주식", "🇺🇸 버거 주식"])

stock_dict = korea_stocks if market == "🇰🇷 김치 주식" else us_stocks

selected_names = st.sidebar.multiselect(
    "🔥 네 지갑을 털어갈 종목을 고르라!! 🔥",
    options=list(stock_dict.keys()),
    default=list(stock_dict.keys())[:3]
)

period = st.sidebar.selectbox("📅 지구 시간 기준 기간", ["1mo", "3mo", "6mo", "1y"])

# 왹져 납치 버튼 (이스터에그)
st.sidebar.markdown("---")
if st.sidebar.button("👽 우주선 납치 버튼 (절대 누르지 마시오)"):
    st.balloons()
    st.toast("🛸 왹왹왹! 지구인을 납치했다!!!")
    st.toast("☄️ 계좌 잔고가 안드로메다로 날아갑니다!")

# 메인 로직
if not selected_names:
    st.error("👽 종목을 골라라 지구인아!!! 안 고르면 지구를 폭파하겠다!!! 💣")
else:
    selected_tickers = {name: stock_dict[name] for name in selected_names}

    with st.spinner("🛸 안드로메다 망원경 조율 중... 으아아아악!!!"):
        price_data = {}
        for name, ticker in selected_tickers.items():
            try:
                # 데이터 수집 (안정성을 위해 multi_level_index=False)
                df = yf.download(ticker, period=period, progress=False, multi_level_index=False)
                if not df.empty:
                    price_data[name] = df
            except Exception as e:
                st.error(f"🛸 {name} 통신 두절! 우주 먼지가 되었나? : {e}")

    if price_data:
        # 1. 미친 네온 차트 (검정 배경 + 형광색 라인) 📊
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.markdown("<h2 style='color:#00ff00; text-align:center;'>📈 뇌정지 수익률 배틀그라운드</h2>", unsafe_allow_html=True)

        return_fig = go.Figure()
        return_summary = []
        
        # 왹져스러운 네온 색상 풀
        neon_colors = ["#ff00ff", "#00ffff", "#ffff00", "#ff0000", "#00ff00", "#ffffff"]

        for idx, (name, df) in enumerate(price_data.items()):
            close = df['Close']
            normalized = (close / close.iloc[0] - 1) * 100
            
            # 피할 수 없는 무지개색 선들!
            line_color = neon_colors[idx % len(neon_colors)]
            
            return_fig.add_trace(go.Scatter(
                x=df.index,
                y=normalized,
                mode='lines+markers', # 마커까지 붙여서 극도로 산만하게 만들기
                name=f"🛸 {name}",
                line=dict(width=4, color=line_color),
                marker=dict(size=8, symbol='star') # 별 모양 마커!
            ))
            final_return = float(normalized.iloc[-1])
            return_summary.append({"종목": name, "수익률(%)": f"{round(final_return, 2)}% 왹!"})

        # 왹져 감성의 블랙홀 플롯 배경 설정
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

        # 수익률 표
        summary_df = pd.DataFrame(return_summary)
        st.markdown("<h3 style='color:#ff00ff;'>🏆 현 시각 우주 서열 (수익률 순)</h3>", unsafe_allow_html=True)
        st.dataframe(summary_df, use_container_width=True, hide_index=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # 2. 광기의 캔들 차트 🕯️
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.markdown("<h2 style='color:#ffff00; text-align:center;'>🕯️ 우주 에너지 파동 (캔들차트)</h2>", unsafe_allow_html=True)

        chart_name = st.selectbox("🛸 스캔할 지구 기업을 선택하라:", list(price_data.keys()))
        chart_df = price_data[chart_name]

        # 형광 핑크(상승)와 형광 파랑(하락)의 지옥의 조합
        candle_fig = go.Figure(data=[go.Candlestick(
            x=chart_df.index,
            open=chart_df['Open'],
            high=chart_df['High'],
            low=chart_df['Low'],
            close=chart_df['Close'],
            increasing_line_color='#ff00ff', # 상승은 핫핑크!
            decreasing_line_color='#00ffff'  # 하락은 형광 하늘색!
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
