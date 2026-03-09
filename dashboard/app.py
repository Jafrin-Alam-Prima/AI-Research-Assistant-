
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
    page_title="ResearchAI | Autonomous Assistant",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS: Modern Professional Dashboard ───────────────────
st.markdown("""
<style>
    /* Google Fonts: Outfit for headings, Inter for body */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600&display=swap');

    /* Design System */
    :root {
        --bg-primary: #0d0d12;
        --bg-secondary: #14141c;
        --bg-card: rgba(255, 255, 255, 0.04);
        --bg-card-hover: rgba(255, 255, 255, 0.06);
        --border-subtle: rgba(255, 255, 255, 0.06);
        --border-accent: rgba(99, 102, 241, 0.4);
        --accent: #6366f1;
        --accent-hover: #818cf8;
        --accent-glow: rgba(99, 102, 241, 0.35);
        --accent-muted: rgba(99, 102, 241, 0.2);
        --text-primary: #f8fafc;
        --text-secondary: #94a3b8;
        --text-muted: #64748b;
        --success: #22c55e;
        --warning: #f59e0b;
        --radius-sm: 8px;
        --radius-md: 12px;
        --radius-lg: 16px;
        --radius-xl: 20px;
        --shadow-card: 0 4px 24px rgba(0, 0, 0, 0.3);
        --shadow-hover: 0 12px 40px rgba(99, 102, 241, 0.2);
    }

    /* Core */
    html, body, [data-testid="stAppViewContainer"], .stApp {
        font-family: 'Inter', -apple-system, sans-serif !important;
        background: var(--bg-primary) !important;
        color: var(--text-primary) !important;
    }

    /* Gradient background */
    .stApp {
        background: linear-gradient(165deg, var(--bg-primary) 0%, #0f0f1a 40%, var(--bg-primary) 100%) !important;
        background-attachment: fixed !important;
    }

    /* Main content area padding */
    [data-testid="stVerticalBlock"] > [data-testid="stVerticalBlock"] {
        padding: 0.5rem 0 !important;
    }

    /* Glass cards */
    .glass-card {
        background: var(--bg-card);
        border: 1px solid var(--border-subtle);
        border-radius: var(--radius-lg);
        padding: 24px;
        backdrop-filter: blur(16px);
        box-shadow: var(--shadow-card);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        margin-bottom: 20px;
    }
    .glass-card:hover {
        background: var(--bg-card-hover);
        border-color: var(--border-accent);
        box-shadow: var(--shadow-hover);
        transform: translateY(-2px);
    }

    /* Hero typography */
    .hero-title {
        font-family: 'Outfit', sans-serif !important;
        font-size: 3.5rem;
        font-weight: 700;
        letter-spacing: -0.04em;
        line-height: 1.1;
        background: linear-gradient(135deg, #ffffff 0%, #a5b4fc 50%, #c7d2fe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.75rem;
        text-align: center;
    }
    .hero-subtitle {
        font-family: 'Inter', sans-serif !important;
        font-size: 1.15rem;
        font-weight: 400;
        color: var(--text-secondary) !important;
        text-align: center;
        max-width: 640px;
        margin: 0 auto 2.5rem auto;
        line-height: 1.7;
    }

    /* Section headers */
    .section-title {
        font-family: 'Outfit', sans-serif !important;
        font-size: 1.6rem;
        font-weight: 600;
        letter-spacing: -0.02em;
        margin-bottom: 1.25rem;
        color: var(--text-primary) !important;
        border-bottom: 1px solid var(--border-subtle);
        padding-bottom: 12px;
    }

    /* Search input */
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid var(--border-subtle) !important;
        border-radius: var(--radius-md) !important;
        color: var(--text-primary) !important;
        font-size: 1.05rem !important;
        padding: 14px 18px !important;
    }
    .stTextInput > div > div > input:focus {
        border-color: var(--accent) !important;
        box-shadow: 0 0 0 3px var(--accent-glow) !important;
    }

    /* Primary buttons */
    div[data-testid="stHorizontalBlock"] div.stButton > button,
    div.stButton > button[kind="primary"],
    .stButton > button {
        background: linear-gradient(135deg, var(--accent) 0%, #4f46e5 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: var(--radius-md) !important;
        padding: 0.65rem 1.4rem !important;
        font-weight: 600 !important;
        transition: all 0.25s ease !important;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, var(--accent-hover) 0%, var(--accent) 100%) !important;
        transform: translateY(-2px);
        box-shadow: 0 8px 24px var(--accent-glow);
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: rgba(13, 13, 18, 0.95) !important;
        border-right: 1px solid var(--border-subtle) !important;
    }
    section[data-testid="stSidebar"] .stRadio > label {
        font-weight: 500 !important;
    }

    /* Expanders */
    div[data-testid="stExpander"] {
        background: var(--bg-card) !important;
        border: 1px solid var(--border-subtle) !important;
        border-radius: var(--radius-md) !important;
        margin-bottom: 12px !important;
    }
    div[data-testid="stExpander"] > summary {
        font-weight: 600 !important;
        padding: 12px 16px !important;
    }

    /* Metrics */
    [data-testid="stMetricValue"] {
        font-family: 'Outfit', sans-serif !important;
        font-size: 1.9rem !important;
        font-weight: 700 !important;
        color: var(--text-primary) !important;
    }
    [data-testid="stMetricLabel"] {
        font-size: 0.8rem !important;
        color: var(--text-muted) !important;
        text-transform: uppercase;
        letter-spacing: 1.2px;
    }

    /* Badges */
    .status-badge {
        display: inline-flex;
        align-items: center;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.7rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        background: var(--accent-muted);
        color: #a5b4fc;
        border: 1px solid var(--border-accent);
    }

    /* Info box */
    .stAlert {
        border-radius: var(--radius-md) !important;
        border: 1px solid var(--border-subtle) !important;
    }

    /* Demo card */
    .demo-card {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.08) 0%, rgba(79, 70, 229, 0.05) 100%);
        border: 1px dashed var(--border-accent);
        border-radius: var(--radius-lg);
        padding: 28px;
        text-align: center;
        margin: 24px 0;
    }

    /* Empty state */
    .empty-state {
        text-align: center;
        padding: 48px 24px;
        color: var(--text-secondary);
        background: var(--bg-card);
        border-radius: var(--radius-lg);
        border: 1px dashed var(--border-subtle);
    }

    /* Footer */
    .footer {
        text-align: center;
        font-size: 0.8rem;
        color: var(--text-muted);
        margin-top: 4rem;
        padding: 2rem;
        border-top: 1px solid var(--border-subtle);
    }

    hr {
        border-color: var(--border-subtle) !important;
        margin: 2rem 0 !important;
    }

    /* Progress bar styling */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, var(--accent), var(--accent-hover)) !important;
    }
</style>
""", unsafe_allow_html=True)


# ── Internal State & Logic ─────────────────────────────────────────

if "orchestrator" not in st.session_state:
    st.session_state.orchestrator = None
if "results" not in st.session_state:
    st.session_state.results = None
if "papers" not in st.session_state:
    st.session_state.papers = []
if "paper_summaries" not in st.session_state:
    st.session_state.paper_summaries = {}  # paper_id -> summary_text
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
with st.sidebar:
    st.markdown("""
    <div style="padding: 8px 0 20px 0; border-bottom: 1px solid rgba(255,255,255,0.06);">
        <span style="font-size: 1.5rem;">🔬</span>
        <span style="font-family: 'Outfit', sans-serif; font-weight: 700; font-size: 1.2rem; margin-left: 8px;">ResearchAI</span>
        <p style="font-size: 0.75rem; color: #64748b; margin: 4px 0 0 0;">Autonomous Multi-Agent Assistant</p>
    </div>
    """, unsafe_allow_html=True)
    add_vertical_space(1)
    
    page = st.radio(
        "NAVIGATION",
        ["🔍 Deep Search", "📖 Corpus Explorer", "🕸️ Knowledge Graph",
         "🎯 Gap Analysis", "🧪 Hypotheses Lab", "🔮 Trend Matrix"],
        label_visibility="collapsed",
    )
    
    add_vertical_space(2)
    st.markdown("---")
    
    orchestrator = get_orchestrator()
    stats = orchestrator.get_graph_stats()
    
    st.markdown("#### 📊 Knowledge Graph")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Nodes", stats.get('total_nodes', 0))
    with col2:
        st.metric("Edges", stats.get('total_edges', 0))
        
    add_vertical_space(2)
    st.caption("Powered by 6 intelligent agents • 100% free")


# ── Page Routing ─────────────────────────────────────────────────

if page == "🔍 Deep Search":
    # ── Hero Section ─────────────────────────────────────────────
    add_vertical_space(2)
    st.markdown('<div class="hero-title">ResearchAI</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="hero-subtitle">Enter a research topic. Our autonomous agents retrieve papers, build knowledge graphs, detect literature gaps, and forecast emerging trends—all in one pipeline.</div>',
        unsafe_allow_html=True,
    )
    
    # ── Search Input (Centered Container) ────────────────────────
    with st.container():
        col1, col2, col3 = st.columns([1, 4, 1])
        with col2:
            query = st.text_input(
                "Topic",
                placeholder="e.g., Graph Neural Networks, Transformers in NLP, Federated Learning...",
                label_visibility="collapsed"
            )
            
            with st.expander("⚙️ Search Parameters", expanded=False):
                sc1, sc2, sc3 = st.columns(3)
                with sc1:
                    max_papers = st.slider("Papers to retrieve", 5, 50, 15, help="Number of papers per source")
                with sc2:
                    year_from = st.number_input("From year", 2010, 2026, 2020)
                with sc3:
                    year_to = st.number_input("To year", 2010, 2026, 2026)
            
            add_vertical_space(1)
            submit = st.button("🚀 Synthesize Knowledge", use_container_width=True, type="primary")
        
        add_vertical_space(2)

    # ── Execution Logic ──────────────────────────────────────────
    if submit:
        if not query:
            st.toast("Please enter a research topic first.", icon="⚠️")
        else:
            with st.status(f"**Synthesizing knowledge** — _{query[:50]}{'...' if len(query) > 50 else ''}_", expanded=True) as status:
                orchestrator = get_orchestrator()
                progress_bar = st.progress(0, text="Starting pipeline...")
                try:
                    results = orchestrator.run_full_pipeline(
                        query=query,
                        max_papers=max_papers,
                        year_from=year_from,
                        year_to=year_to,
                    )
                    progress_bar.progress(100, text="Complete!")
                    st.session_state.results = results
                    st.session_state.papers = results["stages"].get("paper_retrieval", {}).get("result", [])
                    st.session_state.gaps = results["stages"].get("gap_detection", {}).get("result", [])
                    st.session_state.experiments = results["stages"].get("experiment_suggestion", {}).get("result", [])
                    st.session_state.predictions = results["stages"].get("trend_prediction", {}).get("result", [])
                    status.update(label="✅ Synthesis complete! Explore the sidebar for results.", state="complete", expanded=False)
                    st.toast("Analysis finished! Check Knowledge Graph, Gaps & Trends.", icon="✅")
                except Exception as e:
                    progress_bar.empty()
                    status.update(label=f"❌ Synthesis failed: {str(e)[:80]}...", state="error")
                    st.error(f"Pipeline error: {e}")

    # ── Display Last Results Overview ────────────────────────────
    if st.session_state.results:
        add_vertical_space(2)
        res = st.session_state.results
        
        st.markdown(f"### 📊 Results: **{res['query']}**", unsafe_allow_html=True)
        add_vertical_space(1)
        
        overview_c1, overview_c2, overview_c3, overview_c4 = st.columns(4)
        papers_retrieved = len(res["stages"].get("paper_retrieval", {}).get("result", []))
        gaps_found = len(res["stages"].get("gap_detection", {}).get("result", []))
        exps_suggested = len(res["stages"].get("experiment_suggestion", {}).get("result", []))
        trends_pred = len(res["stages"].get("trend_prediction", {}).get("result", []))
        
        with overview_c1:
            st.markdown(f'<div class="glass-card"><p style="color:#94a3b8; font-size:0.85rem; margin-bottom:8px;">📄 Papers</p><p style="font-size:2rem; font-weight:700; margin:0;">{papers_retrieved}</p><span class="status-badge">Retrieved</span></div>', unsafe_allow_html=True)
        with overview_c2:
            st.markdown(f'<div class="glass-card"><p style="color:#94a3b8; font-size:0.85rem; margin-bottom:8px;">🎯 Gaps</p><p style="font-size:2rem; font-weight:700; margin:0;">{gaps_found}</p><span class="status-badge">Identified</span></div>', unsafe_allow_html=True)
        with overview_c3:
            st.markdown(f'<div class="glass-card"><p style="color:#94a3b8; font-size:0.85rem; margin-bottom:8px;">🧪 Hypotheses</p><p style="font-size:2rem; font-weight:700; margin:0;">{exps_suggested}</p><span class="status-badge">Suggested</span></div>', unsafe_allow_html=True)
        with overview_c4:
            st.markdown(f'<div class="glass-card"><p style="color:#94a3b8; font-size:0.85rem; margin-bottom:8px;">🔮 Trends</p><p style="font-size:2rem; font-weight:700; margin:0;">{trends_pred}</p><span class="status-badge">Predicted</span></div>', unsafe_allow_html=True)
        
        add_vertical_space(1)
        st.info("💡 **Tip:** Use the sidebar to explore **Knowledge Graph**, **Gap Analysis**, **Hypotheses Lab**, and **Trend Matrix**.")

    # ── Demo Mode ────────────────────────────────────────────────
    st.markdown("<hr/>", unsafe_allow_html=True)
    with st.container():
        st.markdown("""
        <div class="demo-card">
            <p style="font-size:1.1rem; margin:0 0 8px 0; color:#e2e8f0;">🚀 Try it without APIs</p>
            <p style="font-size:0.9rem; color:#94a3b8; margin:0;">Load 20 pre-loaded papers, knowledge graph, gaps, and trends — no model downloads or API calls.</p>
        </div>
        """, unsafe_allow_html=True)
        colA, colB, colC = st.columns([1, 2, 1])
        with colB:
            if st.button("📦 Load Demo Dataset", use_container_width=True):
                import json
                import os
                os.environ["DEMO_MODE"] = "1"
                
                data_dir = Path(project_root) / "data"
                with open(data_dir / "sample_papers.json", "r") as f:
                    sample_papers = json.load(f)
                with open(data_dir / "sample_citations.json", "r") as f:
                    sample_citations = json.load(f)

                orchestrator = get_orchestrator()
                from src.models.data_models import Paper, Author

                papers = []
                for p in sample_papers:
                    paper = Paper(
                        paper_id=p["paper_id"], title=p["title"], abstract=p.get("abstract", ""),
                        authors=[Author(**a) for a in p.get("authors", [])], year=p.get("year"),
                        venue=p.get("venue", ""), citation_count=p.get("citation_count", 0),
                        source=p.get("source", ""), keywords=p.get("keywords", []),
                    )
                    papers.append(paper)

                st.session_state.papers = papers
                with st.spinner("📥 Injecting demo knowledge graph..."):
                    orchestrator.knowledge_agent.process(papers=papers)
                    for cite in sample_citations:
                        orchestrator.kg.add_citation(cite["citing"], cite["cited"], cite.get("year", 0))
                    orchestrator.kg.save()
                with st.spinner("🎯 Detecting research gaps..."):
                    gaps = orchestrator.gap_agent.process(top_n=10)
                    st.session_state.gaps = gaps
                with st.spinner("🧪 Generating experiment suggestions..."):
                    experiments = orchestrator.experiment_agent.process(gaps=gaps)
                    st.session_state.experiments = experiments
                with st.spinner("🔮 Predicting trends..."):
                    predictions = orchestrator.trend_agent.process(time_horizon="5_years", top_n=8)
                    st.session_state.predictions = predictions
                st.success("✅ Demo loaded! Explore **Knowledge Graph**, **Gap Analysis**, **Hypotheses Lab**, and **Trend Matrix** in the sidebar.")


elif page == "📖 Corpus Explorer":
    st.markdown('<div class="section-title">📖 Corpus Explorer</div>', unsafe_allow_html=True)
    st.markdown("<p style='color:#94a3b8; font-size:0.95rem; margin-bottom:1.5rem;'>Search, filter, and summarize academic papers from your active session.</p>", unsafe_allow_html=True)
    
    papers = st.session_state.get("papers", [])
    if not papers and st.session_state.get("results"):
        papers = st.session_state.results["stages"].get("paper_retrieval", {}).get("result", [])

    if not papers:
        st.markdown("""
        <div class="empty-state">
            <p style="font-size:2.5rem; margin-bottom:12px;">📄</p>
            <p style="font-weight:600; font-size:1.1rem; margin-bottom:8px;">No papers in context</p>
            <p>Run a <strong>Deep Search</strong> or load the <strong>Demo Dataset</strong> to get started.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Toolbar
        search_query = st.text_input("Local Search:", placeholder="Filter by title or abstract keywords...")
        
        # Display papers
        search_lower = search_query.lower().strip() if search_query else ""
        filtered_papers = [p for p in papers if not search_lower or search_lower in (p.title or "").lower() or search_lower in (p.abstract or "").lower()]
        
        st.markdown(f"**Showing {len(filtered_papers)} of {len(papers)} papers**")
        add_vertical_space(1)
        
        for i, paper in enumerate(filtered_papers):
            with st.expander(f"📄 {paper.title[:80]}{'...' if len(paper.title) > 80 else ''}"):
                c1, c2, c3 = st.columns([3, 1, 1])
                with c1:
                    st.markdown(f"**Authors:** {', '.join(a.name for a in paper.authors[:5])}")
                with c2:
                    st.markdown(f"**Year:** {paper.year or 'N/A'}")
                with c3:
                    st.markdown(f"**Citations:** {paper.citation_count}")
                
                if paper.abstract:
                    st.markdown(f"<div style='background:rgba(255,255,255,0.04); padding:16px; border-radius:12px; font-size:0.95rem; line-height:1.65; color:#cbd5e1; border-left:3px solid rgba(99,102,241,0.5);'><strong>Abstract</strong><br/><br/>{paper.abstract}</div>", unsafe_allow_html=True)

                add_vertical_space(1)
                # Show cached summary if available
                if paper.paper_id in st.session_state.paper_summaries:
                    st.markdown("#### ✨ AI Summary")
                    st.success(st.session_state.paper_summaries[paper.paper_id])
                bt_col1, bt_col2 = st.columns([1, 4])
                with bt_col1:
                    if st.button("📝 Summarize", key=f"sum_{paper.paper_id}"):
                        with st.spinner("Abstracting..."):
                            orchestrator = get_orchestrator()
                            summaries = orchestrator.summary_agent.process(papers=[paper])
                            if summaries:
                                st.session_state.paper_summaries[paper.paper_id] = summaries[0].summary_text
                                st.rerun()


elif page == "🕸️ Knowledge Graph":
    st.markdown('<div class="section-title">🕸️ Knowledge Graph</div>', unsafe_allow_html=True)
    st.markdown("<p style='color:#94a3b8; font-size:0.95rem; margin-bottom:1.5rem;'>Visualize papers, topics, methods, datasets, and authors as an interactive network.</p>", unsafe_allow_html=True)
    
    orchestrator = get_orchestrator()
    stats = orchestrator.get_graph_stats()
    
    if stats.get("total_nodes", 0) > 0:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.markdown("#### 📊 Topology")
            filter_type = st.selectbox("Focus Entity", ["All", "paper", "topic", "method", "dataset", "author"])
            st.markdown("---")
            st.markdown("#### ⭐ Top Central Nodes")
            top_nodes = orchestrator.kg.get_centrality(top_n=5)
            for rank, (nid, score) in enumerate(top_nodes, 1):
                node = orchestrator.kg.get_node(nid)
                name = node.get("name", node.get("title", nid)) if node else nid
                short_name = (name[:30] + "...") if len(str(name)) > 30 else name
                st.markdown(f"<p style='margin:6px 0; font-size:0.9rem;'><strong>{rank}.</strong> {short_name}</p>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
        with col2:
            st.markdown('<div class="glass-card" style="padding:0; overflow:hidden;">', unsafe_allow_html=True)
            try:
                from pyvis.network import Network
                import tempfile
                import os

                net = Network(height="600px", width="100%", bgcolor="#0d0d12", font_color="#e2e8f0")
                net.barnes_hut(gravity=-2000, central_gravity=0.3, spring_length=150)

                color_map = {"paper": "#5e6ad2", "topic": "#ec4899", "method": "#10b981", "dataset": "#f59e0b", "author": "#6366f1"}

                for node_id, data in orchestrator.kg.graph.nodes(data=True):
                    ntype = data.get("node_type", "unknown")
                    if filter_type != "All" and ntype != filter_type: continue
                    raw_label = data.get("name", data.get("title", node_id)) or str(node_id)
                    label = raw_label[:25] + "..." if len(raw_label) > 25 else raw_label
                    net.add_node(node_id, label=label, color=color_map.get(ntype, "#475569"), size=20 if ntype=="paper" else 15)

                for u, v, data in orchestrator.kg.graph.edges(data=True):
                    if filter_type != "All":
                        ut = orchestrator.kg.graph.nodes.get(u, {}).get("node_type", "")
                        vt = orchestrator.kg.graph.nodes.get(v, {}).get("node_type", "")
                        if filter_type not in [ut, vt]: continue
                    net.add_edge(u, v, title=data.get("relation_type", ""), color="rgba(255,255,255,0.1)")

                with tempfile.NamedTemporaryFile(delete=False, suffix=".html", mode="w") as f:
                    net.save_graph(f.name)
                    with open(f.name, "r", encoding="utf-8") as html_file:
                        st.components.v1.html(html_file.read(), height=600)
                    os.unlink(f.name)
            except ImportError:
                st.warning("PyVis required for rendering.")
        st.markdown("")
    else:
        st.markdown("""
        <div class="empty-state">
            <p style="font-size:2.5rem; margin-bottom:12px;">🕸️</p>
            <p style="font-weight:600; font-size:1.1rem; margin-bottom:8px;">Knowledge graph is empty</p>
            <p>Run a <strong>Deep Search</strong> or load the <strong>Demo Dataset</strong> to build the graph.</p>
        </div>
        """, unsafe_allow_html=True)


elif page == "🎯 Gap Analysis":
    st.markdown('<div class="section-title">🎯 Research Gap Detection</div>', unsafe_allow_html=True)
    st.markdown("<p style='color:#94a3b8; font-size:0.95rem; margin-bottom:1.5rem;'>Algorithmic identification of underexplored areas, contradictions, and missing method-dataset combinations.</p>", unsafe_allow_html=True)

    orchestrator = get_orchestrator()
    gaps = st.session_state.get("gaps", [])
    
    c1, c2 = st.columns([1, 4])
    with c1:
        if st.button("🔄 Recalculate Gaps", use_container_width=True):
            if orchestrator.kg.graph.number_of_nodes() > 0:
                with st.spinner("🎯 Analyzing graph topology..."):
                    gaps = orchestrator.gap_agent.process(top_n=10)
                    st.session_state.gaps = gaps
            else:
                st.error("Knowledge graph is empty. Run Deep Search or load Demo first.")
    
    if gaps:
        add_vertical_space(1)
        for g in gaps:
            badge_icon = "🔴" if g.novelty_score > 0.7 else "🟡"
            badge_text = "High Novelty" if g.novelty_score > 0.7 else "Medium Novelty"
            with st.expander(f"{badge_icon} **{badge_text}** — {g.topic[:60]}{'...' if len(g.topic) > 60 else ''}"):
                st.markdown(f"**Description:** {g.description}")
                gc1, gc2 = st.columns(2)
                with gc1: st.metric("Gap Type", g.gap_type.replace('_', ' ').title())
                with gc2: st.metric("Novelty Score", f"{g.novelty_score:.2f}")
    else:
        st.markdown("""
        <div class="empty-state">
            <p style="font-size:2.5rem; margin-bottom:12px;">🎯</p>
            <p style="font-weight:600; font-size:1.1rem; margin-bottom:8px;">No gaps detected yet</p>
            <p>Run a <strong>Deep Search</strong>, load the <strong>Demo Dataset</strong>, or click <strong>Recalculate Gaps</strong> if the graph has data.</p>
        </div>
        """, unsafe_allow_html=True)


elif page == "🧪 Hypotheses Lab":
    st.markdown('<div class="section-title">🧪 Hypotheses Lab</div>', unsafe_allow_html=True)
    st.markdown("<p style='color:#94a3b8; font-size:0.95rem; margin-bottom:1.5rem;'>Generate experiment proposals with hypotheses, methodology, and recommended datasets from detected gaps.</p>", unsafe_allow_html=True)
    
    orchestrator = get_orchestrator()
    gaps = st.session_state.get("gaps", [])
    experiments = st.session_state.get("experiments", [])
    
    if not gaps and not experiments:
        st.markdown("""
        <div class="empty-state">
            <p style="font-size:2.5rem; margin-bottom:12px;">🧪</p>
            <p style="font-weight:600; font-size:1.1rem; margin-bottom:8px;">No experiments yet</p>
            <p>Detect <strong>Research Gaps</strong> first (run Deep Search or load Demo), then generate methodology.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        if gaps:
            selected_gap = st.selectbox("Select Target Gap", [g.topic for g in gaps], key="gap_select")
            if st.button("🧪 Generate Methodology", use_container_width=True):
                target = next((g for g in gaps if g.topic == selected_gap), None)
                if target:
                    with st.spinner("Using LLM to formulate hypothesis..."):
                        new_exps = orchestrator.experiment_agent.process(gaps=[target])
                        experiments.extend(new_exps)
                        st.session_state.experiments = experiments
        
        if experiments:
            st.markdown("### 📋 Generated Proposals")
            add_vertical_space(1)
            for e in reversed(experiments):
                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                st.markdown(f"#### ✨ {e.title}")
                st.markdown(f"**Hypothesis:** {e.hypothesis}")
                st.markdown("**Methodology:**")
                st.markdown(f"<div style='background:rgba(255,255,255,0.04); padding:16px; border-radius:10px; border-left:3px solid rgba(99,102,241,0.5); line-height:1.6; color:#cbd5e1;'>{e.methodology}</div>", unsafe_allow_html=True)
                
                ec1, ec2 = st.columns(2)
                with ec1:
                    st.markdown("**Datasets:**")
                    st.markdown("\n".join(f"- {d}" for d in e.recommended_datasets))
                with ec2:
                    st.markdown("**Outcomes:**")
                    st.write(e.expected_outcomes)
                st.markdown('</div>', unsafe_allow_html=True)


elif page == "🔮 Trend Matrix":
    st.markdown('<div class="section-title">🔮 Trend Matrix</div>', unsafe_allow_html=True)
    st.markdown("<p style='color:#94a3b8; font-size:0.95rem; margin-bottom:1.5rem;'>Predict emerging research topics using citation network analysis and exponential smoothing.</p>", unsafe_allow_html=True)
    
    orchestrator = get_orchestrator()
    preds = st.session_state.get("predictions", [])
    
    if st.button("🔮 Run Trend Prediction", use_container_width=True):
        if orchestrator.kg.graph.number_of_nodes() > 0:
            with st.spinner("Computing citation trajectories..."):
                preds = orchestrator.trend_agent.process(time_horizon="5_years", top_n=8)
                st.session_state.predictions = preds
        else:
            st.error("Knowledge graph needs citation data. Run Deep Search or load Demo first.")
    
    if not preds:
        st.markdown("""
        <div class="empty-state">
            <p style="font-size:2.5rem; margin-bottom:12px;">🔮</p>
            <p style="font-weight:600; font-size:1.1rem; margin-bottom:8px;">No predictions yet</p>
            <p>Click <strong>Run Trend Prediction</strong> after loading data (Deep Search or Demo).</p>
        </div>
        """, unsafe_allow_html=True)
    elif preds:
        import plotly.express as px
        import pandas as pd
        
        # Build DataFrame for Plotly
        df = pd.DataFrame([{
            "Topic": p.topic[:30], 
            "Confidence": p.confidence_score, 
            "Growth Rate": p.growth_rate,
            "Citations": p.citation_velocity
        } for p in preds])
        
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        fig = px.scatter(df, x="Growth Rate", y="Confidence", size="Citations", 
                         color="Confidence", hover_name="Topic", text="Topic",
                         color_continuous_scale="Purples", title="Trend Trajectories")
        fig.update_traces(textposition='top center')
        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(13,13,18,0)",
            plot_bgcolor="rgba(13,13,18,0)",
            font=dict(color="#e2e8f0", size=12),
            margin=dict(l=20, r=20, t=40, b=20),
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ── Global Footer ────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <strong>ResearchAI</strong> — Autonomous Multi-Agent Research Assistant<br>
    Powered by Streamlit • Plotly • PyVis • 100% Free & Open Source
</div>
""", unsafe_allow_html=True)
