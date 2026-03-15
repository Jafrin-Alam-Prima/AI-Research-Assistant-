"""
ResearchAI - Premium AI Research Assistant
Streamlit multi-page app redesigned for a modern, minimalistic SaaS aesthetic.
"""

import sys
from pathlib import Path

# Add project root to path
project_root = str(Path(__file__).parent.parent)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import streamlit as st

try:
    from streamlit_extras.add_vertical_space import add_vertical_space
except ImportError:
    def add_vertical_space(n=1):
        st.markdown("<br/>" * (n * 2), unsafe_allow_html=True)

# ── Page Configuration ───────────────────────────────────────────
st.set_page_config(
    page_title="ResearchAI — AI Powered Research Discovery",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ──────────────────────────────────────────────────
st.markdown("""
<style>
/* your full CSS here, unchanged */
</style>
""", unsafe_allow_html=True)

# ── Internal State & Logic ──────────────────────────────────────
if "orchestrator" not in st.session_state:
    st.session_state.orchestrator = None
if "results" not in st.session_state:
    st.session_state.results = None
if "papers" not in st.session_state:
    st.session_state.papers = []
if "paper_summaries" not in st.session_state:
    st.session_state.paper_summaries = {}
if "gaps" not in st.session_state:
    st.session_state.gaps = []
if "experiments" not in st.session_state:
    st.session_state.experiments = []
if "predictions" not in st.session_state:
    st.session_state.predictions = []

@st.cache_resource
def get_orchestrator():
    from src.orchestrator.agent_orchestrator import AgentOrchestrator
    return AgentOrchestrator()

# ── Sidebar Navigation ──────────────────────────────────────────
NAV_OPTIONS = [
    "🏠 Home",
    "🔎 Smart Paper Search",
    "📚 Paper Library",
    "🧠 Research Knowledge Map",
    "🧩 Research Gap Finder",
    "💡 Idea & Hypothesis Generator",
    "📈 Trend Forecast",
]
if "nav_radio" not in st.session_state:
    st.session_state.nav_radio = NAV_OPTIONS[0]

with st.sidebar:
    st.markdown("""
    <div style="padding: 8px 0 20px 0; border-bottom: 1px solid rgba(255,255,255,0.06);">
        <span style="font-size: 1.5rem;">🤖</span>
        <span style="font-family: 'Outfit', sans-serif; font-weight: 700; font-size: 1.2rem; margin-left: 8px;">AI Research Assistant</span>
        <p style="font-size: 0.75rem; color: #64748b; margin: 4px 0 0 0;">Searches, analyzes, and organizes research papers so you can explore any topic faster.</p>
    </div>
    """, unsafe_allow_html=True)
    add_vertical_space(1)
    
    page = st.radio(
        "NAVIGATION",
        NAV_OPTIONS,
        key="nav_radio",
        label_visibility="collapsed",
    )
    
    add_vertical_space(2)
    st.markdown("---")
    
    orchestrator = get_orchestrator()
    stats = orchestrator.get_graph_stats()
    
    st.markdown("#### 📊 Knowledge Map")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Nodes", stats.get('total_nodes', 0))
    with col2:
        st.metric("Edges", stats.get('total_edges', 0))
        
    add_vertical_space(2)
    st.caption("Powered by 6 AI agents • 100% free")

# ── Page Routing ────────────────────────────────────────────────
if page == "🏠 Home":
    add_vertical_space(1)
    st.markdown('<div class="hero-title">🔬 ResearchAI — AI Powered Research Discovery</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">Explore papers, discover insights, and generate research ideas using autonomous AI agents.</div>', unsafe_allow_html=True)
    add_vertical_space(2)

    modules = [
        ("🔎", "Smart Paper Search", "Search academic papers and research sources using AI-powered deep search.", "🔎 Smart Paper Search"),
        ("📚", "Paper Library", "Browse and explore all collected research papers and documents in one place.", "📚 Paper Library"),
        ("🧠", "Research Knowledge Map", "Visualize connections between concepts, papers, and research ideas.", "🧠 Research Knowledge Map"),
        ("🧩", "Research Gap Finder", "Identify missing research areas and unexplored opportunities in the literature.", "🧩 Research Gap Finder"),
        ("💡", "Idea & Hypothesis Generator", "Generate new research ideas and hypotheses based on existing knowledge.", "💡 Idea & Hypothesis Generator"),
        ("📈", "Trend Forecast", "See which research directions are growing and emerging over time.", "📈 Trend Forecast"),
    ]

    # Fixed module cards with safe rerun
    for row in range(0, 6, 3):
        cols = st.columns(3)
        for i, col in enumerate(cols):
            idx = row + i
            if idx < len(modules):
                icon, title, desc, nav_val = modules[idx]
                with col:
                    st.markdown(f"""
                    <div class="module-card">
                        <p style="font-size: 2.5rem; margin-bottom: 12px;">{icon}</p>
                        <p style="font-family: 'Outfit', sans-serif; font-weight: 600; font-size: 1.1rem; margin-bottom: 8px;">{title}</p>
                        <p style="font-size: 0.85rem; color: #94a3b8; line-height: 1.5; margin-bottom: 16px;">{desc}</p>
                    </div>
                    """, unsafe_allow_html=True)

                    if st.button("Open", key=f"card_{idx}", use_container_width=True, help=f"Open {title}"):
                        st.session_state.nav_radio = nav_val
                        st.experimental_rerun()

    add_vertical_space(2)
    st.markdown("---")
    st.markdown("#### How it works")
    st.markdown("""
    <div class="workflow-steps">
        <div class="workflow-step"><strong>Step 1</strong><br/>Search papers</div>
        <div class="workflow-step"><strong>Step 2</strong><br/>Explore papers</div>
        <div class="workflow-step"><strong>Step 3</strong><br/>See knowledge connections</div>
        <div class="workflow-step"><strong>Step 4</strong><br/>Detect research gaps</div>
        <div class="workflow-step"><strong>Step 5</strong><br/>Generate research ideas</div>
    </div>
    """, unsafe_allow_html=True)

# ── The rest of your pages ──
# Replace all st.rerun() with st.experimental_rerun() in:
# 🔎 Smart Paper Search → Load Demo, Summarize
# 🧩 Research Gap Finder → Recalculate Gaps
# 💡 Idea & Hypothesis Generator → Generate Ideas

# ── Global Footer ────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <strong>Created by Jafrin Alam Prima.</strong><br>
    <a href="https://japrima.com" target="_blank" rel="noopener noreferrer">Learn more about the creator</a>
</div>
""", unsafe_allow_html=True)
