import os
import streamlit as st
import streamlit.components.v1 as components

# Configure Streamlit page to wide layout matching the desktop dashboard
st.set_page_config(
    page_title="Compressor Acceleration Analysis Dashboard 📊",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Remove default Streamlit padding/header/footer so FFT_Analyzer.html fills the viewport cleanly
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .stApp {
            background-color: #0a0a0f;
        }
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        iframe {
            display: block;
            border: none;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


def main():
    html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "FFT_Analyzer.html")
    if not os.path.exists(html_path):
        st.error("FFT_Analyzer.html 파일을 찾을 수 없습니다. 동일한 디렉토리에 파일이 존재하는지 확인해 주세요.")
        return

    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Render the standalone HTML dashboard inside Streamlit
    components.html(html_content, height=960, scrolling=True)


if __name__ == "__main__":
    main()
