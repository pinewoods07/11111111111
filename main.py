import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta

# 페이지 설정
st.set_page_config(
    page_title="🌈 무지개 주식 분석 🌈",
    page_icon="🚀",
    layout="wide"
)

# 화려한 무지개 CSS 스타일 ✨
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(-45deg, #ff0000, #ff7f00, #ffff00, #00ff00, #0000ff, #4b0082, #9400d3);
        background-size: 400% 400%;
        animation: rainbow 15s ease infinite;
    }
    @keyframes rainbow {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    .sparkle-title {
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(to right, #ff0080, #ff8c00, #40e0d0, #ff0080);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: pulse 2s infinite;
        text-shadow: 2px 2px 10px rgba(255,255,255,0.8);
    }
    @keyframes pulse {
        0% {transform: scale(1);}
        50% {transform: scale(1.05);}
        100% {transform: scale(1);}
    }
    .content-box {
        background: rgba(255, 255, 255, 0.85);
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
    }
</style>
""", unsafe_allow_html=True)

# 화려한 제목 🌈
st.markdown('<p class="sparkle-title">🌈✨ 무지개 반짝반짝 주식 분석 외계인 🛸 ✨🌈</p>', unsafe_allow_html=True)
st.markdown('<h3 style="text-align:center; color:white;">🚀 으아아아악! 한국 & 미국 주식 한눈에 비교 ㅋㅋㅋ 🚀</h3>', unsafe_allow_html=True)
st.markdown("---")

# 주요 종목 딕셔너리 (이름: 티커)
korea_stocks = {
    "삼성전자": "005930.KS",
    "SK하이닉스": "000660.KS",
    "현대차": "005380.KS",
    "NAVER": "035420.KS",
    "카카오": "035720.KS",
    "LG에너지솔루션": "373220.KS",
}

us_stocks = {
    "애플(Apple)": "AAPL",
    "마이크로소프트(Microsoft)": "MSFT",
    "엔비디아(NVIDIA)": "NVDA",
    "테슬라(Tesla)": "TSLA",
    "구글(Google)": "GOOGL",
    "아마존(Amazon)": "AMZN",
}

# 사이드바 설정 🎨
st.sidebar.markdown("## 🛸 외계인 설정 패널 🛸")

market = st.sidebar.radio("🌍 시장을 선택하세요!", ["🇰🇷 한국", "🇺🇸 미국"])

if market == "🇰🇷 한국":
    stock_dict = korea_stocks
else:
    stock_dict = us_stocks

selected_names = st.sidebar.multiselect(
    "✨ 비교할 종목 선택 (여러 개 가능!) ✨",
    options=list(stock_dict.keys()),
    default=list(stock_dict.keys())[:3]
)

period_option = st.sidebar.selectbox(
    "📅 분석 기간",
    ["1개월", "3개월", "6개월", "1년", "2년"]
)
period_map = {"1개월": "1mo", "3개월": "3mo", "6개월": "6mo", "1년": "1y", "2년": "2y"}
period = period_map[period_option]

st.sidebar.markdown("---")
st.sidebar.info("🌈 데이터 출처: Yahoo Finance (yfinance)")

# 메인 로직
if not selected_names:
    st.warning("👽 종목을 하나 이상 선택해주세요! 으아아악~ 🛸")
else:
    selected_tickers = {name: stock_dict[name] for name in selected_names}

    with st.spinner("🚀 외계 행성에서 데이터 가져오는 중... 으아아악! 🛸"):
        price_data = {}
        for name, ticker in selected_tickers.items():
            try:
                # ✅ multi_level_index=False 추가 (컬럼 구조를 단순하게!)
                df = yf.download(ticker, period=period, progress=False, multi_level_index=False)
                if not df.empty:
                    price_data[name] = df
            except Exception as e:
                st.error(f"❌ {name} 데이터를 못 가져왔어요: {e}")

    if price_data:
        # 1. 수익률 비교 📊
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.markdown("### 💰 수익률 비교 (기간 시작 대비 %) 🌈")

        return_fig = go.Figure()
        return_summary = []

        for name, df in price_data.items():
            close = df['Close']
            normalized = (close / close.iloc[0] - 1) * 100
            return_fig.add_trace(go.Scatter(
                x=df.index,
                y=normalized,
                mode='lines',
                name=name,
                line=dict(width=3)
            ))
            final_return = float(normalized.iloc[-1])
            return_summary.append({"종목": name, "수익률(%)": round(final_return, 2)})

        return_fig.update_layout(
            title="📈 누적 수익률 추이",
            xaxis_title="날짜",
            yaxis_title="수익률 (%)",
            template="plotly_white",
            height=450,
            hovermode="x unified"
        )
        st.plotly_chart(return_fig, use_container_width=True)

        summary_df = pd.DataFrame(return_summary).sort_values("수익률(%)", ascending=False)
        st.markdown("#### 🏆 수익률 순위표")
        st.dataframe(summary_df, use_container_width=True, hide_index=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # 2. 종목별 캔들차트 🕯️
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.markdown("### 🕯️ 종목별 가격 차트 (캔들스틱) ✨")

        chart_name = st.selectbox("🔍 자세히 볼 종목 선택", list(price_data.keys()))
        chart_df = price_data[chart_name]

        candle_fig = go.Figure(data=[go.Candlestick(
            x=chart_df.index,
            open=chart_df['Open'],
            high=chart_df['High'],
            low=chart_df['Low'],
            close=chart_df['Close'],
            increasing_line_color='red',
            decreasing_line_color='blue'
        )])
        candle_fig.update_layout(
            title=f"🚀 {chart_name} 캔들차트",
            xaxis_title="날짜",
            yaxis_title="가격",
            template="plotly_white",
            height=500,
            xaxis_rangeslider_visible=True
        )
        st.plotly_chart(candle_fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.balloons()
    else:
        st.error("👽 데이터를 가져오지 못했어요. 으아아악! 다시 시도해주세요 🛸")

# 푸터
st.markdown("---")
st.markdown('<p style="text-align:center; color:white;">🌈✨ Made with Streamlit | 당곡고 학습 프로젝트 ✨🌈</p>', unsafe_allow_html=True)
