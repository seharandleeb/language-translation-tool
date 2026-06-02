import streamlit as st
from deep_translator import GoogleTranslator
from deep_translator.exceptions import LanguageNotSupportedException, RequestError

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="LinguaFlow · Translator",
    page_icon="🌐",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    background: #0d0d14;
    color: #e8e6f0;
    font-family: 'DM Sans', sans-serif;
}
[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(ellipse 70% 45% at 15% -5%, #1a053388 0%, transparent 55%),
        radial-gradient(ellipse 60% 40% at 85% 105%, #001a3a88 0%, transparent 55%),
        #0d0d14;
}
[data-testid="stHeader"], footer, [data-testid="stToolbar"] { display: none !important; }

/* Hero */
.hero { text-align: center; padding: 2.5rem 1rem 1.5rem; }
.hero-badge {
    display: inline-block;
    background: linear-gradient(135deg, rgba(139,92,246,.2), rgba(59,130,246,.12));
    border: 1px solid rgba(139,92,246,.35);
    border-radius: 100px;
    padding: .3rem 1rem;
    font-size: .7rem;
    font-weight: 600;
    letter-spacing: .12em;
    text-transform: uppercase;
    color: #a78bfa;
    margin-bottom: 1rem;
}
.hero h1 {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.2rem, 6vw, 3.5rem);
    font-weight: 800;
    margin: 0 0 .6rem;
    background: linear-gradient(135deg, #e8e6f0 30%, #a78bfa 65%, #60a5fa 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero p { color: #6b6880; font-size: 1rem; font-weight: 300; margin: 0; }

/* Cards */
.card {
    background: rgba(255,255,255,.03);
    border: 1px solid rgba(255,255,255,.07);
    border-radius: 18px;
    padding: 1.6rem 1.8rem;
    margin-bottom: 1rem;
}
.section-label {
    font-family: 'Syne', sans-serif;
    font-size: .65rem;
    font-weight: 700;
    letter-spacing: .14em;
    text-transform: uppercase;
    color: #55536a;
    margin-bottom: .6rem;
}

/* Selects */
/* Selects */
div[data-baseweb="select"] > div {
    background: #1a1828 !important;
    border: 1px solid rgba(255,255,255,.12) !important;
    border-radius: 10px !important;
    color: #e8e6f0 !important;
    font-family: 'DM Sans', sans-serif !important;
}
div[data-baseweb="select"] > div:focus-within {
    border-color: rgba(139,92,246,.5) !important;
    box-shadow: 0 0 0 3px rgba(139,92,246,.1) !important;
}
div[data-baseweb="select"] svg { fill: #a78bfa !important; }
ul[data-baseweb="menu"] {
    background: #1e1c2e !important;
    border: 1px solid rgba(139,92,246,.2) !important;
}
ul[data-baseweb="menu"] li { color: #e8e6f0 !important; background: #1e1c2e !important; }
ul[data-baseweb="menu"] li:hover { background: rgba(139,92,246,.2) !important; }

/* Textarea */
textarea {
    background: #1a1828 !important;
    border: 1px solid rgba(255,255,255,.12) !important;
    border-radius: 10px !important;
    color: #e8e6f0 !important;
    caret-color: #a78bfa !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: .98rem !important;
    line-height: 1.7 !important;
}
textarea:focus {
    border-color: rgba(139,92,246,.5) !important;
    box-shadow: 0 0 0 3px rgba(139,92,246,.1) !important;
    background: #1e1c2e !important;
}
textarea::placeholder { color: #55536a !important; }
/* also target the inner p/div Streamlit wraps around textarea in newer versions */
[data-testid="stTextArea"] textarea { background: #1a1828 !important; color: #e8e6f0 !important; }

/* Buttons — use stButton class directly, no wrapping div tricks */
.stButton > button {
    border-radius: 12px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 1rem !important;
    font-weight: 500 !important;
    padding: .72rem 1.4rem !important;
    width: 100% !important;
    transition: all .2s !important;
}
/* Primary translate button (first button rendered) */
button[kind="primary"],
.stButton:first-of-type > button {
    background: linear-gradient(135deg, #7c3aed, #4f46e5) !important;
    color: #fff !important;
    border: none !important;
    box-shadow: 0 4px 20px rgba(124,58,237,.3) !important;
}
button[kind="primary"]:hover,
.stButton:first-of-type > button:hover {
    background: linear-gradient(135deg, #8b5cf6, #6366f1) !important;
    box-shadow: 0 6px 28px rgba(124,58,237,.5) !important;
    transform: translateY(-1px) !important;
}
/* Secondary copy button */
button[kind="secondary"] {
    background: rgba(255,255,255,.06) !important;
    color: #b8b5cc !important;
    border: 1px solid rgba(255,255,255,.1) !important;
}
button[kind="secondary"]:hover {
    background: rgba(255,255,255,.1) !important;
    border-color: rgba(139,92,246,.4) !important;
    color: #e8e6f0 !important;
}

/* Result box */
.result-box {
    background: rgba(124,58,237,.07);
    border: 1px solid rgba(124,58,237,.18);
    border-radius: 12px;
    padding: 1.2rem 1.4rem;
    font-size: 1.02rem;
    line-height: 1.75;
    color: #ddd9ee;
    min-height: 72px;
    word-break: break-word;
    white-space: pre-wrap;
    margin-top: .5rem;
}
.result-placeholder { color: #35334a; font-style: italic; }

/* Char counter */
.char-info { text-align: right; font-size: .72rem; color: #45435a; margin-top: .25rem; }
.char-warn  { color: #f59e0b; }
.char-error { color: #ef4444; }

/* Arrow */
.lang-arrow { text-align: center; font-size: 1.4rem; color: #3a3852; padding-top: 1.55rem; }

/* Footer */
.footer { text-align: center; padding: 2rem 0 1rem; color: #33314a; font-size: .76rem; }

/* Alert tweaks */
[data-testid="stAlert"] {
    border-radius: 10px !important;
    font-family: 'DM Sans', sans-serif !important;
}
</style>
""", unsafe_allow_html=True)

# ── Language data ─────────────────────────────────────────────────────────────
LANGUAGES = {
    "Auto Detect": "auto",
    "Afrikaans": "af", "Albanian": "sq", "Amharic": "am", "Arabic": "ar",
    "Armenian": "hy", "Azerbaijani": "az", "Basque": "eu", "Bengali": "bn",
    "Bosnian": "bs", "Bulgarian": "bg", "Catalan": "ca",
    "Chinese (Simplified)": "zh-CN", "Chinese (Traditional)": "zh-TW",
    "Croatian": "hr", "Czech": "cs", "Danish": "da", "Dutch": "nl",
    "English": "en", "Esperanto": "eo", "Estonian": "et", "Finnish": "fi",
    "French": "fr", "Galician": "gl", "Georgian": "ka", "German": "de",
    "Greek": "el", "Gujarati": "gu", "Haitian Creole": "ht", "Hausa": "ha",
    "Hebrew": "iw", "Hindi": "hi", "Hungarian": "hu", "Icelandic": "is",
    "Indonesian": "id", "Irish": "ga", "Italian": "it", "Japanese": "ja",
    "Kannada": "kn", "Kazakh": "kk", "Khmer": "km", "Korean": "ko",
    "Kurdish": "ku", "Latin": "la", "Latvian": "lv", "Lithuanian": "lt",
    "Macedonian": "mk", "Malay": "ms", "Malayalam": "ml", "Maltese": "mt",
    "Maori": "mi", "Marathi": "mr", "Mongolian": "mn", "Nepali": "ne",
    "Norwegian": "no", "Pashto": "ps", "Persian": "fa", "Polish": "pl",
    "Portuguese": "pt", "Punjabi": "pa", "Romanian": "ro", "Russian": "ru",
    "Serbian": "sr", "Sinhala": "si", "Slovak": "sk", "Slovenian": "sl",
    "Somali": "so", "Spanish": "es", "Swahili": "sw", "Swedish": "sv",
    "Tagalog (Filipino)": "tl", "Tamil": "ta", "Telugu": "te", "Thai": "th",
    "Turkish": "tr", "Ukrainian": "uk", "Urdu": "ur", "Uzbek": "uz",
    "Vietnamese": "vi", "Welsh": "cy", "Yoruba": "yo", "Zulu": "zu",
}

SOURCE_LANGS = list(LANGUAGES.keys())
TARGET_LANGS = [l for l in LANGUAGES.keys() if l != "Auto Detect"]
MAX_CHARS = 5000

# ── Session state ─────────────────────────────────────────────────────────────
if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""
if "show_copy_box" not in st.session_state:
    st.session_state.show_copy_box = False

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-badge">🌐 CodeAlpha AI Internship · Task 1</div>
  <h1>LinguaFlow</h1>
  <p>Translate instantly across 80+ languages — free, no API key needed</p>
</div>
""", unsafe_allow_html=True)

# ── Language selector ─────────────────────────────────────────────────────────
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="section-label">⚡ Choose Languages</div>', unsafe_allow_html=True)

col_src, col_mid, col_tgt = st.columns([5, 1, 5])
with col_src:
    source_lang_name = st.selectbox(
        "Source", SOURCE_LANGS,
        index=SOURCE_LANGS.index("Auto Detect"),
        label_visibility="collapsed",
    )
with col_mid:
    st.markdown('<div class="lang-arrow">→</div>', unsafe_allow_html=True)
with col_tgt:
    target_lang_name = st.selectbox(
        "Target", TARGET_LANGS,
        index=TARGET_LANGS.index("English"),
        label_visibility="collapsed",
    )
st.markdown('</div>', unsafe_allow_html=True)

# ── Text input ────────────────────────────────────────────────────────────────
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="section-label">✍️ Enter Text</div>', unsafe_allow_html=True)

input_text = st.text_area(
    "Source text",
    height=150,
    max_chars=MAX_CHARS,
    placeholder="Type or paste text here…",
    label_visibility="collapsed",
)

n = len(input_text)
cls = "char-error" if n > MAX_CHARS * .95 else ("char-warn" if n > MAX_CHARS * .8 else "")
st.markdown(f'<div class="char-info {cls}">{n:,} / {MAX_CHARS:,} chars</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── Buttons ───────────────────────────────────────────────────────────────────
col_b1, col_b2 = st.columns(2)

with col_b1:
    translate_clicked = st.button("🌐  Translate", type="primary", use_container_width=True)

with col_b2:
    copy_clicked = st.button("📋  Copy Translation", type="secondary", use_container_width=True)

# ── Translate logic ───────────────────────────────────────────────────────────
if translate_clicked:
    st.session_state.show_copy_box = False
    if not input_text.strip():
        st.warning("⚠️  Please enter some text before translating.")
    elif source_lang_name != "Auto Detect" and source_lang_name == target_lang_name:
        st.warning("⚠️  Source and target are the same language. Pick a different target.")
    else:
        src_code = LANGUAGES[source_lang_name]
        tgt_code = LANGUAGES[target_lang_name]
        with st.spinner("Translating…"):
            try:
                translator = GoogleTranslator(source=src_code, target=tgt_code)
                result = translator.translate(input_text.strip())
                st.session_state.translated_text = result or ""
            except LanguageNotSupportedException:
                st.error("❌  Language pair not supported. Try a different combination.")
                st.session_state.translated_text = ""
            except RequestError:
                st.error("❌  Network error — check your internet connection and try again.")
                st.session_state.translated_text = ""
            except Exception as e:
                st.error(f"❌  Unexpected error: {e}")
                st.session_state.translated_text = ""

# ── Copy logic ────────────────────────────────────────────────────────────────
if copy_clicked:
    if not st.session_state.translated_text:
        st.warning("⚠️  Nothing to copy — translate some text first!")
    else:
        st.session_state.show_copy_box = True

# ── Result ────────────────────────────────────────────────────────────────────
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="section-label">🔤 Translation</div>', unsafe_allow_html=True)

if st.session_state.translated_text:
    # Escape HTML special chars so the result renders safely
    safe = (st.session_state.translated_text
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;"))
    st.markdown(f'<div class="result-box">{safe}</div>', unsafe_allow_html=True)
else:
    st.markdown(
        '<div class="result-box result-placeholder">Your translation will appear here…</div>',
        unsafe_allow_html=True,
    )

st.markdown('</div>', unsafe_allow_html=True)

# ── Copy feedback ─────────────────────────────────────────────────────────────
if st.session_state.show_copy_box and st.session_state.translated_text:
    st.success("✅  Select all and copy from the box below (Ctrl+A then Ctrl+C):")
    st.code(st.session_state.translated_text, language=None)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
  Built with ❤️ using Streamlit &amp; deep-translator &nbsp;·&nbsp; CodeAlpha AI Internship Task 1
</div>
""", unsafe_allow_html=True)