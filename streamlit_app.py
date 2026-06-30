import streamlit as st

st.set_page_config(
    page_title="Amadou's First AI App",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #e0f2fe, #f8fafc);
}
.hero {
    padding: 50px;
    border-radius: 25px;
    background: linear-gradient(135deg, #0284c7, #38bdf8);
    color: white;
    text-align: center;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.15);
}
.card {
    padding: 25px;
    border-radius: 18px;
    background-color: white;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>🚀 Welcome to My First Streamlit App</h1>
    <h3>Built by Amadou Sidibe</h3>
    <p>AI • Program Management • Data • Cloud • Cybersecurity</p>
</div>
""", unsafe_allow_html=True)

st.write("")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3>🤖 AI Projects</h3>
        <p>Building AI tools that solve real business problems.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>📊 Program Management</h3>
        <p>Helping teams deliver projects with clarity and structure.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>☁️ Cloud & Data</h3>
        <p>Exploring modern cloud, analytics, and automation solutions.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.markdown("## Try the App")

name = st.text_input("Enter your name")

if name:
    st.success(f"Hello {name}! Welcome to my first deployed Streamlit application.")

st.markdown("---")
st.caption("Built with Python and Streamlit | First deployment project")
