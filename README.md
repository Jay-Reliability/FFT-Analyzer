# 📊 Compressor Acceleration Analysis Dashboard (Web FFT Analyzer)

윈도우 데스크톱 GUI(`PyQt5` + `Matplotlib`) 기반 진동 신호 및 FFT 주파수 분석 프로그램(`01_FFT_GUI_Analyzer_1.py`)의 기능과 UI/UX Tone & Manner를 그대로 유지하여 웹 브라우저 및 **Streamlit Cloud**에서 즉시 실행할 수 있도록 구현한 프로젝트입니다.

---

## ✨ 주요 기능 (Key Features)

1. **CSV 데이터 로딩 및 메타데이터 자동 분석 (`1. Select Input Data` & `2. File Information`)**
   - 시계열 진동 CSV 파일(예: `TVN6_0124_1822_50deg_Time.csv`) 업로드 지원
   - `Time` 컬럼 자동 감지 및 다중 진동 채널(`CH11`, `CH12` 등) 체크박스 선택
   - 총 샘플 수(`Total Samples`), 측정 시간(`Duration`), 샘플링 주파수(`Sampling Rate`) 자동 계산 및 표시

2. **진동 및 FFT 분석 파라미터 설정 (`3. Analysis Configuration`)**
   - **Time Column**: 시간 축 데이터 컬럼 선택
   - **Vibration Channels**: 분석할 진동 채널 다중 선택
   - **Start Time (sec)** & **Analysis Duration (sec)**: 분석 구간(시작 시간 및 길이) 지정
   - **Max FFT Frequency (Hz)**: 관심 주파수 대역 상한 설정 (기본값 `200 Hz`)
   - **Gaussian Filter Sigma ($\sigma$)**: 스펙트럼 가우시안 스무딩 필터 계수 설정 (기본값 `0.50`, 반사 경계 조건 적용)

3. **Time Domain & Frequency Domain 동시 시각화 (`⚡ Run Diagnostics`)**
   - **Time Domain (상단 행)**:
     - 선택된 구간의 가속도(`g`) 시계열 파형 출력
     - 최대(`Max`) / 최소(`Min`) 가속도 수치 요약 및 그래프 내 화살표 어노테이션 박스 표시
   - **Frequency Domain - FFT (하단 행)**:
     - Hamming Window 및 RMS 진폭 보정(Single-Sided Spectrum) 적용 정밀 FFT 연산
     - `LINEAR (g RMS)` 스케일 및 `dB (Ref 10⁻⁵)` 스케일 실시간 전환 지원
     - `1X Peak Frequency`, `1X Magnitude`, 대역 내 `Overall Acceleration` 자동 도출 및 피크 화살표 어노테이션 표시

4. **데이터 및 고해상도 그래프 내보내기 (Export)**
   - **📥 Export FFT Data**: 전 채널의 주파수별 Linear / dB 스펙트럼 데이터를 CSV 파일(`*_FFT_Analysis.csv`)로 다운로드
   - **📷 Export Graphs (JPG)** / 개별 **📷 Save JPG**: 각 채널의 Time Domain 및 Frequency Spectrum 그래프를 고해상도(`1200x600`) JPG 이미지로 저장

---

## 📁 파일 구성 (Repository Structure)

```text
├── FFT_Analyzer.html               # 브라우저에서 단독 실행 가능한 Web FFT 분석 대시보드
├── app.py                          # Streamlit Cloud 배포용 메인 애플리케이션 엔트리포인트
├── requirements.txt                # Streamlit 실행을 위한 파이썬 패키지 의존성 목록
├── README.md                       # 프로젝트 설명 및 배포 가이드
├── 01_FFT_GUI_Analyzer_1.py        # 원본 PyQt5 데스크톱 애플리케이션 코드
└── TVN6_0124_1822_50deg_Time.csv   # 동작 검증용 샘플 진동 데이터 (CSV)
```

---

## 🚀 실행 방법 (How to Run)

### 1) 웹 브라우저에서 직접 실행 (설치 불필요)
`FFT_Analyzer.html` 파일을 더블클릭하여 Chrome, Edge, Safari 등 인터넷 브라우저에서 바로 실행할 수 있습니다.

### 2) 로컬 환경에서 Streamlit으로 실행
```bash
pip install -r requirements.txt
streamlit run app.py
```

### 3) GitHub & Streamlit Community Cloud 배포 방법
1. 본 디렉토리의 `FFT_Analyzer.html`, `app.py`, `requirements.txt`, `README.md` 파일을 GitHub 저장소(Repository)에 업로드(Push)합니다.
2. [Streamlit Community Cloud](https://share.streamlit.io/)에 접속하여 **Create app**을 클릭합니다.
3. 업로드한 GitHub 저장소와 브랜치를 선택하고 **Main file path**에 `app.py`를 입력한 뒤 **Deploy!** 버튼을 클릭하면 웹 앱이 게시됩니다.
