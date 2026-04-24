import streamlit as st

def load_styles():
    st.markdown("""
<style>
.stApp{
background:radial-gradient(circle at top left,rgba(124,58,237,.25),transparent 28%),
radial-gradient(circle at top right,rgba(37,99,235,.22),transparent 28%),
linear-gradient(135deg,#06111f,#111827 45%,#1e1b4b);
color:#eef2ff}
.block-container{padding-top:1.5rem;max-width:1280px}
.hero,.glass,.card{border:1px solid rgba(255,255,255,.12);box-shadow:0 18px 50px rgba(0,0,0,.32)}
.hero{padding:34px;border-radius:26px;background:linear-gradient(135deg,rgba(15,23,42,.95),rgba(49,46,129,.72));margin-bottom:20px}
.hero h1{font-size:3.1rem;color:white;margin:0 0 8px}
.hero p{font-size:1.05rem;color:#dbe7ff}
.glass{background:rgba(255,255,255,.06);border-radius:22px;padding:20px}
.card{background:linear-gradient(180deg,rgba(255,255,255,.08),rgba(255,255,255,.04));border-radius:22px;padding:22px;min-height:220px}
.section-title{font-size:1.55rem;font-weight:800;color:white;margin-bottom:10px}
.tiny,.navnote{color:#cbd5ff;font-size:.96rem}
.metric-card{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.12);border-radius:18px;padding:14px;text-align:center}
.metric-label{font-size:.9rem;color:#cdd9ff}.metric-value{font-size:1.35rem;font-weight:800;color:white}
div[data-testid="stButton"]>button{width:100%;border-radius:14px;padding:.8rem 1rem;border:1px solid rgba(255,255,255,.14);
background:linear-gradient(135deg,#7c3aed,#2563eb);color:white;font-weight:800}
div[data-testid="stButton"]>button:hover{filter:brightness(1.08)}
</style>
""", unsafe_allow_html=True)
