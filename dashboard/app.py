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
from streamlit_extras.add_vertical_space import add_vertical_space

# ── Page Configuration ───────────────────────────────────────────
st.set_page_config(
    page_title="ResearchAI | Autonomous Assistant",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS for Premium Notion/Perplexity Aesthetic ──────────
st.markdown("""
<style>
    /* Google Fonts Import */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    /* Global Variables */
    :root {
        --bg-color: #0a0a0f;
        --card-bg: rgba(255, 255, 255, 0.03);
        --card-border: rgba(255, 255, 255, 0.08);
        --accent: #5e6ad2;
        --accent-glow: rgba(94, 106, 210, 0.4);
        --text-primary: #ffffff;
        --text-secondary: #9ca3af;
    }

    /* Core Layout & Font */
    html, body, [class*="css"]  {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        background-color: var(--bg-color) !important;
        color: var(--text-primary) !important;
    }

    /* Animated Dynamic Gradient Background */
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .stApp {
        background: radial-gradient(circle at 15% 50%, rgba(30, 20, 50, 0.8), transparent 30%),
                    radial-gradient(circle at 85% 30%, rgba(20, 30, 60, 0.8), transparent 30%),
                    #0a0a0f !important;
        background-size: 200% 200%;
        animation: gradientBG 20s ease infinite;
    }

    /* Glassmorphism Cards */
    .glass-card {
        background: var(--card-bg);
        border: 1px solid var(--card-border);
        border-radius: 16px;
        padding: 24px;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), 
                    box-shadow 0.3s ease, border-color 0.3s ease;
        margin-bottom: 20px;
    }
    .glass-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 40px var(--accent-glow);
        border-color: rgba(255, 255, 255, 0.15);
    }

    /* Typography */
    .hero-title {
        font-size: 4.5rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        line-height: 1.1;
        background: linear-gradient(135deg, #ffffff 0%, #a5b4fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        text-align: center;
    }
    
    .hero-subtitle {
        font-size: 1.25rem;
        font-weight: 400;
        color: var(--text-secondary);
        text-align: center;
        max-width: 600px;
        margin: 0 auto 3rem auto;
        line-height: 1.6;
    }

    .section-title {
        font-size: 1.5rem;
        font-weight: 600;
        letter-spacing: -0.02em;
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        gap: 10px;
        border-bottom: 1px solid var(--card-border);
        padding-bottom: 10px;
    }

    /* Inputs - Search Bar like Perplexity */
    input[type="text"] {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        color: white !important;
        font-size: 1.1rem !important;
        padding: 16px 20px !important;
        transition: all 0.3s ease !important;
    }
    input[type="text"]:focus {
        background-color: rgba(255, 255, 255, 0.08) !important;
        border-color: var(--accent) !important;
        box-shadow: 0 0 0 4px var(--accent-glow) !important;
    }

    /* Primary Button Style */
    div.stButton > button {
        background: var(--accent) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.75rem 1.5rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.5px !important;
        transition: all 0.3s ease !important;
        width: 100%;
    }
    div.stButton > button:hover {
        background: #6b77e8 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 25px var(--accent-glow) !important;
    }

    /* Sidebar Tweaks */
    section[data-testid="stSidebar"] {
        background-color: rgba(10, 10, 15, 0.8) !important;
        backdrop-filter: blur(40px) !important;
        border-right: 1px solid var(--card-border) !important;
    }
    .css-17lntkn {
        color: var(--text-secondary);
    }
    
    /* Expanders (used for papers/results) */
    div[data-testid="stExpander"] {
        background-color: rgba(255, 255, 255, 0.02) !important;
        border: 1px solid var(--card-border) !important;
        border-radius: 12px !important;
        margin-bottom: 1rem !important;
    }
    div[data-testid="stExpander"] > summary {
        background-color: transparent !important;
        color: white !important;
        font-weight: 600 !important;
    }

    /* Metric Containers */
    div[data-testid="stMetricValue"] {
        font-size: 2rem !important;
        font-weight: 700 !important;
        color: #ffffff !important;
    }
    div[data-testid="stMetricLabel"] {
        font-size: 0.9rem !important;
        color: var(--text-secondary) !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Badges */
    .status-badge {
        display: inline-flex;
        align-items: center;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        background: rgba(94, 106, 210, 0.15);
        color: #a5b4fc;
        border: 1px solid rgba(94, 106, 210, 0.3);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        font-size: 0.85rem;
        color: var(--text-secondary);
        margin-top: 5rem;
        padding-top: 2rem;
        border-top: 1px solid var(--card-border);
    }
    
    hr {
        border-color: var(--card-border) !important;
        margin: 2rem 0 !important;
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

@st.cache_resource
def get_orchestrator():
    from src.orchestrator.agent_orchestrator import AgentOrchestrator
    return AgentOrchestrator()


# ── Sidebar Navigation ──────────────────────────────────────────
with st.sidebar:
    st.markdown("### ✨ AI Research Assistant")
    add_vertical_space(2)
    
    page = st.radio(
        "NAVIGATION",
        ["🔍 Deep Search", "📖 Corpus Explorer", "🕸️ Knowledge Graph",
         "🎯 Gap Analysis", "🧪 Hypotheses Lab", "🔮 Trend Matrix"],
        label_visibility="collapsed",
    )
    
    add_vertical_space(4)
    st.markdown("<hr/>", unsafe_allow_html=True)
    
    orchestrator = get_orchestrator()
    stats = orchestrator.get_graph_stats()
    
    st.markdown("#### 🧠 Brain Capacity")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Nodes", stats.get('total_nodes', 0))
    with col2:
        st.metric("Edges", stats.get('total_edges', 0))
        
    add_vertical_space(3)
    st.caption("Powered by locally-orchestrated intelligent agents.")


# ── Page Routing ─────────────────────────────────────────────────

if page == "🔍 Deep Search":
    # ── Hero Section ─────────────────────────────────────────────
    add_vertical_space(3)
    st.markdown('<div class="hero-title">AI Research Assistant</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="hero-subtitle">Enter a topic. Our autonomous agents will retrieve relevant papers, synthesize knowledge graphs, discover literature gaps, and forecast future trends.</div>',
        unsafe_allow_html=True,
    )
    
    # ── Search Input (Centered Container) ────────────────────────
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        query = st.text_input(
            "Topic", 
            placeholder="Ask anything... e.g., 'Advancements in Graph Neural Networks'", 
            label_visibility="collapsed"
        )
        
        # Advanced settings hidden in an expander
        with st.expander("⚙️ Search Parameters"):
            sc1, sc2, sc3 = st.columns(3)
            with sc1:
                max_papers = st.slider("Scope (Papers)", 5, 50, 15)
            with sc2:
                year_from = st.number_input("Since", 2010, 2026, 2020)
            with sc3:
                year_to = st.number_input("Until", 2010, 2026, 2026)
        
        add_vertical_space(1)
        submit = st.button("Synthesize Knowledge ▸", use_container_width=True)
        
    add_vertical_space(2)

    # ── Execution Logic ──────────────────────────────────────────
    if submit:
        if not query:
            st.toast("Please enter a research topic first.", icon="⚠️")
        else:
            with st.status(f"🧠 Synthesizing knowledge for: '{query}'...", expanded=True) as status:
                orchestrator = get_orchestrator()
                
                st.write("📡 Initializing external paper retrieval...")
                # The orchestrator is already capturing logs, but we'll show a nice UI loader
                
                try:
                    results = orchestrator.run_full_pipeline(
                        query=query,
                        max_papers=max_papers,
                        year_from=year_from,
                        year_to=year_to,
                    )
                    st.session_state.results = results
                    status.update(label="Synthesis Complete!", state="complete", expanded=False)
                    st.toast("Analysis finished!", icon="✅")
                except Exception as e:
                    status.update(label=f"Synthesis Failed: {e}", state="error")
                    st.error(f"Pipeline encountered an error: {e}")

    # ── Display Last Results Overview ────────────────────────────
    if st.session_state.results:
        add_vertical_space(2)
        res = st.session_state.results
        
        st.markdown(f"### <span style='font-weight:400; color:var(--text-secondary);'>Results for</span> {res['query']}", unsafe_allow_html=True)
        
        # Overview Cards
        overview_c1, overview_c2, overview_c3, overview_c4 = st.columns(4)
        
        papers_retrieved = len(res["stages"].get("paper_retrieval", {}).get("result", []))
        gaps_found = len(res["stages"].get("gap_detection", {}).get("result", []))
        exps_suggested = len(res["stages"].get("experiment_suggestion", {}).get("result", []))
        trends_pred = len(res["stages"].get("trend_prediction", {}).get("result", []))
        
        with overview_c1:
            st.markdown(f'<div class="glass-card"><h4>📄 Papers</h4><h2>{papers_retrieved}</h2><span class="status-badge">Retrieved</span></div>', unsafe_allow_html=True)
        with overview_c2:
            st.markdown(f'<div class="glass-card"><h4>🎯 Gaps</h4><h2>{gaps_found}</h2><span class="status-badge">Identified</span></div>', unsafe_allow_html=True)
        with overview_c3:
            st.markdown(f'<div class="glass-card"><h4>🧪 Hypotheses</h4><h2>{exps_suggested}</h2><span class="status-badge">Suggested</span></div>', unsafe_allow_html=True)
        with overview_c4:
            st.markdown(f'<div class="glass-card"><h4>🔮 Trends</h4><h2>{trends_pred}</h2><span class="status-badge">Predicted</span></div>', unsafe_allow_html=True)
            
        st.info("💡 Navigation tip: Use the left sidebar to dive deep into the specific results like the Knowledge Graph or Gap Analysis.")


    # ── Demo Mode ────────────────────────────────────────────────
    st.markdown("<hr/>", unsafe_allow_html=True)
    colA, colB, colC = st.columns([1,2,1])
    with colB:
        st.markdown('<div style="text-align:center; color:gray; font-size:0.9rem;">Want to see how it works without waiting for live APIs?</div>', unsafe_allow_html=True)
        if st.button("Load Pre-computed Demo Dataset 📦"):
            import json
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
            with st.spinner("Injecting demo knowledge graph..."):
                orchestrator.knowledge_agent.process(papers=papers)
                for cite in sample_citations:
                    orchestrator.kg.add_citation(cite["citing"], cite["cited"], cite.get("year", 0))
                orchestrator.kg.save()
            st.success("Demo environment loaded. Check the sidebar tabs!")


elif page == "📖 Corpus Explorer":
    st.markdown('<div class="section-title">✨ Corpus Explorer</div>', unsafe_allow_html=True)
    st.markdown("<p style='color:var(--text-secondary);'>Search, filter, and summarize academic papers from your active session.</p>", unsafe_allow_html=True)
    
    papers = st.session_state.get("papers", [])
    if not papers:
        # Check orchestrator state as fallback
        papers = get_orchestrator().paper_agent.cache if hasattr(get_orchestrator(), 'paper_agent') else []
        
    if not papers:
        st.info("No papers currently in context. Run a Deep Search first.")
    else:
        # Toolbar
        search_query = st.text_input("Local Search:", placeholder="Filter by title or abstract keywords...")
        
        # Display papers
        filtered_papers = [p for p in papers if search_query.lower() in p.title.lower() or (p.abstract and search_query.lower() in p.abstract.lower())]
        
        st.markdown(f"**Showing {len(filtered_papers)} of {len(papers)} papers**")
        
        for i, paper in enumerate(filtered_papers):
            with st.expander(f"📄 {paper.title}"):
                c1, c2, c3 = st.columns([3, 1, 1])
                with c1:
                    st.markdown(f"**Authors:** {', '.join(a.name for a in paper.authors[:5])}")
                with c2:
                    st.markdown(f"**Year:** {paper.year or 'N/A'}")
                with c3:
                    st.markdown(f"**Citations:** {paper.citation_count}")
                
                if paper.abstract:
                    st.markdown(f"<div style='background:rgba(255,255,255,0.03); padding:15px; border-radius:8px; font-size:0.95rem; line-height:1.6; color:#cbd5e1;'><strong>Abstract:</strong><br/>{paper.abstract}</div>", unsafe_allow_html=True)
                
                add_vertical_space(1)
                bt_col1, bt_col2 = st.columns([1, 4])
                with bt_col1:
                    if st.button("📝 Summarize", key=f"sum_{paper.paper_id}"):
                        with st.spinner("Abstracting..."):
                            orchestrator = get_orchestrator()
                            summaries = orchestrator.summary_agent.process(papers=[paper])
                            if summaries:
                                st.markdown("#### ✨ AI Summary")
                                st.success(summaries[0].summary_text)


elif page == "🕸️ Knowledge Graph":
    st.markdown('<div class="section-title">🕸️ Global Knowledge Graph</div>', unsafe_allow_html=True)
    
    orchestrator = get_orchestrator()
    stats = orchestrator.get_graph_stats()
    
    if stats.get("total_nodes", 0) > 0:
        col1, col2 = st.columns([1,3])
        with col1:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.markdown("### Topology")
            filter_type = st.selectbox("Focus Entity", ["All", "paper", "topic", "method", "dataset", "author"])
            st.markdown("---")
            st.markdown("#### Top Central Nodes")
            top_nodes = orchestrator.kg.get_centrality(top_n=5)
            for rank, (nid, score) in enumerate(top_nodes, 1):
                node = orchestrator.kg.get_node(nid)
                name = node.get("name", node.get("title", nid)) if node else nid
                st.markdown(f"<small>{rank}. {name}</small>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
        with col2:
            st.markdown('<div class="glass-card" style="padding:0; overflow:hidden;">', unsafe_allow_html=True)
            try:
                from pyvis.network import Network
                import tempfile
                import os

                net = Network(height="600px", width="100%", bgcolor="#0a0a0f", font_color="#e2e8f0")
                net.barnes_hut(gravity=-2000, central_gravity=0.3, spring_length=150)

                color_map = {"paper": "#5e6ad2", "topic": "#ec4899", "method": "#10b981", "dataset": "#f59e0b", "author": "#6366f1"}

                for node_id, data in orchestrator.kg.graph.nodes(data=True):
                    ntype = data.get("node_type", "unknown")
                    if filter_type != "All" and ntype != filter_type: continue
                    label = (data.get("name", data.get("title", node_id)))[:25] + "..."
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
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("Knowledge Graph is empty. Run a Deep Search first.")


elif page == "🎯 Gap Analysis":
    st.markdown('<div class="section-title">🎯 Research Gap Detection</div>', unsafe_allow_html=True)
    st.markdown("<p style='color:var(--text-secondary);'>Algorithmic identification of contradictions and underexplored intersections in literature.</p>", unsafe_allow_html=True)

    orchestrator = get_orchestrator()
    gaps = st.session_state.get("gaps", [])
    
    c1, c2 = st.columns([1, 4])
    with c1:
        if st.button("Recalculate Gaps", use_container_width=True):
            if orchestrator.kg.graph.number_of_nodes() > 0:
                with st.spinner("Analyzing graph topology..."):
                    gaps = orchestrator.gap_agent.process(top_n=10)
                    st.session_state.gaps = gaps
            else:
                st.error("Empty Knowledge Graph.")
    
    if gaps:
        add_vertical_space(1)
        for g in gaps:
            badge_color = "🔴 High Novelty" if g.novelty_score > 0.7 else "🟡 Med Novelty"
            with st.expander(f"{badge_color} — {g.topic}"):
                st.markdown(f"**Description:** {g.description}")
                gc1, gc2 = st.columns(2)
                with gc1: st.metric("Gap Type", g.gap_type.replace('_', ' ').title())
                with gc2: st.metric("Novelty Score", f"{g.novelty_score:.2f}")


elif page == "🧪 Hypotheses Lab":
    st.markdown('<div class="section-title">🧪 Experiment Generation</div>', unsafe_allow_html=True)
    
    orchestrator = get_orchestrator()
    gaps = st.session_state.get("gaps", [])
    experiments = st.session_state.get("experiments", [])
    
    if not gaps and not experiments:
        st.info("Detect Research Gaps first before generating experiments.")
    else:
        if gaps:
            selected_gap = st.selectbox("Select Target Gap", [g.topic for g in gaps])
            if st.button("Generate Methodology"):
                target = next((g for g in gaps if g.topic == selected_gap), None)
                if target:
                    with st.spinner("Using LLM to formulate hypothesis..."):
                        new_exps = orchestrator.experiment_agent.process(gaps=[target])
                        experiments.extend(new_exps)
                        st.session_state.experiments = experiments
        
        if experiments:
            st.markdown("### Generated Proposals")
            for e in reversed(experiments):
                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                st.markdown(f"#### ✨ {e.title}")
                st.markdown(f"**Hypothesis:** {e.hypothesis}")
                st.markdown("**Methodology:**")
                st.markdown(f"<div style='background:rgba(0,0,0,0.3); padding:10px; border-radius:5px;'>{e.methodology}</div>", unsafe_allow_html=True)
                
                ec1, ec2 = st.columns(2)
                with ec1:
                    st.markdown("**Datasets:**")
                    st.markdown("\n".join(f"- {d}" for d in e.recommended_datasets))
                with ec2:
                    st.markdown("**Outcomes:**")
                    st.write(e.expected_outcomes)
                st.markdown('</div>', unsafe_allow_html=True)


elif page == "🔮 Trend Matrix":
    st.markdown('<div class="section-title">🔮 Future Trend Forecast</div>', unsafe_allow_html=True)
    
    orchestrator = get_orchestrator()
    preds = st.session_state.get("predictions", [])
    
    if st.button("Run Time-Series Prediction"):
        if orchestrator.kg.graph.number_of_nodes() > 0:
            with st.spinner("Computing citation trajectories..."):
                preds = orchestrator.trend_agent.process(time_horizon="5_years", top_n=8)
                st.session_state.predictions = preds
        else:
            st.error("Graph requires citation data to predict trends.")
            
    if preds:
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
                         color_continuous_scale="Purp", title="Trend Trajectories")
        fig.update_traces(textposition='top center')
        fig.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ── Global Footer ────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    Crafted by ResearchAI Logic • Multi-Agent System<br>
    Powered by Python, LangChain, & Streamlit
</div>
""", unsafe_allow_html=True)
