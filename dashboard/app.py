"""
ResearchAI - Interactive Dashboard
Streamlit multi-page app for exploring research analysis results.
"""

import sys
from pathlib import Path

# Add project root to path
project_root = str(Path(__file__).parent.parent)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import streamlit as st

# ── Page Configuration ───────────────────────────────────────────
st.set_page_config(
    page_title="ResearchAI - Multi-Agent Research Assistant",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ───────────────────────────────────────────────────
st.markdown("""
<style>
    /* Dark theme overrides with Animated Gradient Background */
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .stApp {
        background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #1a1a2e);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        color: #ffffff !important;
    }

    /* Headings */
    h1, h2, h3, h4, h5, h6, .stMarkdown p {
        color: #ffffff !important;
    }

    /* Main Title Animation */
    @keyframes pulseGlow {
        0% { text-shadow: 0 0 10px rgba(102,126,234,0.5); }
        50% { text-shadow: 0 0 20px rgba(118,75,162,0.8), 0 0 30px rgba(102,126,234,0.6); }
        100% { text-shadow: 0 0 10px rgba(102,126,234,0.5); }
    }

    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: 900;
        margin-bottom: 0px;
        animation: pulseGlow 3s infinite alternate;
    }

    .sub-header {
        color: #e2e8f0 !important;
        font-size: 1.2rem;
        margin-top: -5px;
        font-weight: 300;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }

    /* Glassmorphism Cards with Hover Effects */
    .metric-card, div[data-testid="stExpander"] {
        background: rgba(20, 20, 40, 0.6) !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 16px !important;
        padding: 15px;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
    }
    
    div[data-testid="stExpander"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px 0 rgba(102, 126, 234, 0.4);
        border-color: rgba(255, 255, 255, 0.3) !important;
    }

    /* Fix Expander Text Visibility */
    div[data-testid="stExpander"] p, div[data-testid="stExpander"] div, div[data-testid="stExpander"] span {
        color: #f8fafc !important;
    }

    /* Metrics Visibility */
    div[data-testid="stMetricValue"] {
        color: #61dafb !important;
        text-shadow: 0 0 10px rgba(97, 218, 251, 0.3);
        font-weight: bold;
    }
    div[data-testid="stMetricLabel"] {
        color: #cbd5e1 !important;
        font-weight: 500;
    }

    /* Animated Badges */
    .agent-badge {
        display: inline-block;
        padding: 6px 16px;
        border-radius: 30px;
        font-size: 0.85rem;
        font-weight: 700;
        margin: 4px;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        cursor: default;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border: 1px solid rgba(255,255,255,0.1);
    }
    
    .agent-badge:hover {
        transform: scale(1.1) translateY(-2px);
        filter: brightness(1.2);
    }

    .badge-retrieval { background: rgba(102, 126, 234, 0.25); color: #a3bffa; border-color: #667eea; box-shadow: 0 0 10px rgba(102, 126, 234, 0.4); }
    .badge-extraction { background: rgba(118, 75, 162, 0.25); color: #d6bcfa; border-color: #764ba2; box-shadow: 0 0 10px rgba(118, 75, 162, 0.4); }
    .badge-gap { background: rgba(236, 72, 153, 0.25); color: #fbcfe8; border-color: #ec4899; box-shadow: 0 0 10px rgba(236, 72, 153, 0.4); }
    .badge-experiment { background: rgba(16, 185, 129, 0.25); color: #a7f3d0; border-color: #10b981; box-shadow: 0 0 10px rgba(16, 185, 129, 0.4); }
    .badge-summary { background: rgba(245, 158, 11, 0.25); color: #fde68a; border-color: #f59e0b; box-shadow: 0 0 10px rgba(245, 158, 11, 0.4); }
    .badge-trend { background: rgba(59, 130, 246, 0.25); color: #bfdbfe; border-color: #3b82f6; box-shadow: 0 0 10px rgba(59, 130, 246, 0.4); }

    /* Elegant Sidebar */
    div[data-testid="stSidebar"] {
        background: rgba(15, 12, 41, 0.85) !important;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-right: 1px solid rgba(255,255,255,0.05);
    }
    
    /* Input Fields and Buttons */
    .stTextInput > div > div > input, .stSelectbox > div > div > div {
        background-color: rgba(30, 30, 50, 0.7) !important;
        color: white !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
        border-radius: 8px;
    }
    .stTextInput > div > div > input:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.5) !important;
    }
    
    /* Buttons */
    .stButton > button {
        border-radius: 12px;
        font-weight: bold;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .stButton > button[data-baseweb="button"] {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        border: none;
        color: white;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    .stButton > button[data-baseweb="button"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(118, 75, 162, 0.6);
        background: linear-gradient(90deg, #764ba2 0%, #667eea 100%);
    }

</style>
""", unsafe_allow_html=True)


# ── Sidebar Navigation ──────────────────────────────────────────
st.sidebar.markdown("## 🔬 ResearchAI")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "📄 Paper Explorer", "🕸️ Knowledge Graph",
     "🔍 Gap Analysis", "🧪 Experiment Lab", "📈 Trend Forecast"],
    label_visibility="collapsed",
)

st.sidebar.markdown("---")
st.sidebar.markdown("### System Status")

# Initialize session state
if "orchestrator" not in st.session_state:
    st.session_state.orchestrator = None
if "results" not in st.session_state:
    st.session_state.results = None
if "papers" not in st.session_state:
    st.session_state.papers = []

# ── Helper: Load Orchestrator ────────────────────────────────────
@st.cache_resource
def get_orchestrator():
    from src.orchestrator.agent_orchestrator import AgentOrchestrator
    return AgentOrchestrator()


# ── Page: Home ───────────────────────────────────────────────────
if page == "🏠 Home":
    st.markdown('<p class="main-header">ResearchAI</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sub-header">'
        'Autonomous Multi-Agent Research Assistant with Trend Prediction'
        '</p>',
        unsafe_allow_html=True,
    )
    st.markdown("---")

    # Agent showcase
    st.markdown("### 🤖 Agent Pipeline")
    cols = st.columns(6)
    agents = [
        ("📄", "Paper Retrieval", "badge-retrieval", "Fetch from arXiv, Semantic Scholar, PubMed"),
        ("🧠", "Knowledge Extraction", "badge-extraction", "Extract entities, build knowledge graph"),
        ("🔍", "Gap Detection", "badge-gap", "Find underexplored areas & contradictions"),
        ("🧪", "Experiment Suggestion", "badge-experiment", "Propose experiments for gaps"),
        ("📝", "Summarization", "badge-summary", "Summarize papers with BART-CNN"),
        ("📈", "Trend Prediction", "badge-trend", "Predict emerging topics (5-10 years)"),
    ]
    for col, (icon, name, badge, desc) in zip(cols, agents):
        with col:
            st.markdown(f"#### {icon}")
            st.markdown(f'<span class="agent-badge {badge}">{name}</span>', unsafe_allow_html=True)
            st.caption(desc)

    st.markdown("---")

    # Quick Start
    st.markdown("### 🚀 Quick Start")
    query = st.text_input(
        "Enter a research topic to analyze:",
        placeholder="e.g., Graph Neural Networks for Social Networks",
        key="home_query",
    )

    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        max_papers = st.slider("Max papers to retrieve", 5, 50, 20)
    with col2:
        year_from = st.number_input("From year", 2015, 2025, 2019)
    with col3:
        year_to = st.number_input("To year", 2015, 2025, 2025)

    if st.button("🔬 Run Full Analysis Pipeline", type="primary", use_container_width=True):
        if not query:
            st.warning("Please enter a research topic.")
        else:
            orchestrator = get_orchestrator()
            with st.spinner("Running multi-agent pipeline... This may take a minute."):
                progress = st.progress(0, text="Initializing agents...")
                progress.progress(10, text="📄 Fetching papers...")

                try:
                    results = orchestrator.run_full_pipeline(
                        query=query,
                        max_papers=max_papers,
                        year_from=year_from,
                        year_to=year_to,
                    )
                    progress.progress(100, text="✅ Pipeline complete!")
                    st.session_state.results = results
                    st.success(f"Analysis complete! Navigate to other pages to explore results.")
                except Exception as e:
                    st.error(f"Pipeline failed: {e}")

    # Demo mode
    st.markdown("---")
    st.markdown("### 📦 Demo Mode")
    st.info("Load sample data to explore the dashboard without running the full pipeline.")

    if st.button("Load Sample Data", use_container_width=True):
        import json
        data_dir = Path(project_root) / "data"
        with open(data_dir / "sample_papers.json", "r") as f:
            sample_papers = json.load(f)
        with open(data_dir / "sample_citations.json", "r") as f:
            sample_citations = json.load(f)

        # Build a demo graph
        orchestrator = get_orchestrator()
        from src.models.data_models import Paper, Author

        papers = []
        for p in sample_papers:
            paper = Paper(
                paper_id=p["paper_id"],
                title=p["title"],
                abstract=p.get("abstract", ""),
                authors=[Author(**a) for a in p.get("authors", [])],
                year=p.get("year"),
                venue=p.get("venue", ""),
                citation_count=p.get("citation_count", 0),
                source=p.get("source", ""),
                keywords=p.get("keywords", []),
            )
            papers.append(paper)

        st.session_state.papers = papers

        # Run knowledge extraction on sample data
        with st.spinner("Processing sample data..."):
            orchestrator.knowledge_agent.process(papers=papers)

            # Add citations
            for cite in sample_citations:
                orchestrator.kg.add_citation(cite["citing"], cite["cited"], cite.get("year", 0))

            orchestrator.kg.save()

        st.success(f"Loaded {len(papers)} papers and {len(sample_citations)} citations!")
        stats = orchestrator.get_graph_stats()
        st.json(stats)


# ── Page: Paper Explorer ─────────────────────────────────────────
elif page == "📄 Paper Explorer":
    st.markdown("## 📄 Paper Explorer")
    st.markdown("Search, filter, and summarize academic papers.")
    st.markdown("---")

    search_query = st.text_input("Search for papers:", placeholder="e.g., transformers, GNN, reinforcement learning")

    col1, col2 = st.columns(2)
    with col1:
        source_filter = st.multiselect("Sources", ["arxiv", "semantic_scholar", "pubmed"], default=["arxiv", "semantic_scholar"])
    with col2:
        sort_by = st.selectbox("Sort by", ["Relevance", "Year (newest)", "Citations"])

    if st.button("🔎 Search Papers", type="primary"):
        if search_query:
            orchestrator = get_orchestrator()
            with st.spinner("Fetching papers..."):
                papers = orchestrator.paper_agent.process(
                    query=search_query,
                    max_results=20,
                    sources=source_filter,
                )
                st.session_state.papers = papers

    # Display papers
    papers = st.session_state.get("papers", [])
    if papers:
        st.markdown(f"### Found {len(papers)} papers")

        if sort_by == "Year (newest)":
            papers = sorted(papers, key=lambda p: p.year or 0, reverse=True)
        elif sort_by == "Citations":
            papers = sorted(papers, key=lambda p: p.citation_count, reverse=True)

        for i, paper in enumerate(papers):
            with st.expander(f"📄 {paper.title}", expanded=(i < 3)):
                cols = st.columns([3, 1, 1])
                with cols[0]:
                    authors_str = ", ".join(a.name for a in paper.authors[:5])
                    st.markdown(f"**Authors:** {authors_str}")
                with cols[1]:
                    st.metric("Year", paper.year or "N/A")
                with cols[2]:
                    st.metric("Citations", paper.citation_count)

                if paper.abstract:
                    st.markdown(f"**Abstract:** {paper.abstract[:500]}...")
                if paper.venue:
                    st.markdown(f"**Venue:** {paper.venue}")
                if paper.url:
                    st.markdown(f"[🔗 View Paper]({paper.url})")

                # Summarize button
                if st.button(f"📝 Summarize", key=f"sum_{i}"):
                    orchestrator = get_orchestrator()
                    with st.spinner("Generating summary..."):
                        summaries = orchestrator.summary_agent.process(papers=[paper])
                        if summaries:
                            st.success("**Summary:**")
                            st.write(summaries[0].summary_text)
                            if summaries[0].key_contributions:
                                st.markdown("**Key Contributions:**")
                                for c in summaries[0].key_contributions:
                                    st.markdown(f"- {c}")
    else:
        st.info("Enter a search query or load sample data from the Home page.")


# ── Page: Knowledge Graph ────────────────────────────────────────
elif page == "🕸️ Knowledge Graph":
    st.markdown("## 🕸️ Knowledge Graph")
    st.markdown("Explore the research knowledge graph — papers, topics, methods, and connections.")
    st.markdown("---")

    orchestrator = get_orchestrator()
    stats = orchestrator.get_graph_stats()

    # Stats overview
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Nodes", stats.get("total_nodes", 0))
    with col2:
        st.metric("Total Edges", stats.get("total_edges", 0))
    with col3:
        node_types = stats.get("node_types", {})
        st.metric("Papers", node_types.get("paper", 0))
    with col4:
        st.metric("Topics", node_types.get("topic", 0))

    st.markdown("---")

    if stats.get("total_nodes", 0) > 0:
        # Node type filter
        filter_type = st.selectbox(
            "Filter by node type",
            ["All", "paper", "topic", "method", "dataset", "author"],
        )

        # Graph visualization with PyVis
        try:
            from pyvis.network import Network
            import tempfile
            import os

            net = Network(height="600px", width="100%", bgcolor="#0f0c29", font_color="white")
            net.barnes_hut(gravity=-3000, central_gravity=0.3, spring_length=100)

            color_map = {
                "paper": "#667eea",
                "topic": "#ec4899",
                "method": "#10b981",
                "dataset": "#f59e0b",
                "author": "#764ba2",
            }

            # Add nodes
            for node_id, data in orchestrator.kg.graph.nodes(data=True):
                node_type = data.get("node_type", "unknown")
                if filter_type != "All" and node_type != filter_type:
                    continue

                label = data.get("name", data.get("title", node_id))
                if len(label) > 30:
                    label = label[:27] + "..."

                color = color_map.get(node_type, "#718096")
                size = 20 if node_type == "paper" else 12

                net.add_node(node_id, label=label, color=color, size=size, title=f"{node_type}: {label}")

            # Add edges
            for u, v, data in orchestrator.kg.graph.edges(data=True):
                if filter_type != "All":
                    u_type = orchestrator.kg.graph.nodes.get(u, {}).get("node_type", "")
                    v_type = orchestrator.kg.graph.nodes.get(v, {}).get("node_type", "")
                    if filter_type not in [u_type, v_type]:
                        continue

                rel = data.get("relation_type", "")
                net.add_edge(u, v, title=rel, color="rgba(255,255,255,0.2)")

            # Save and display
            with tempfile.NamedTemporaryFile(delete=False, suffix=".html", mode="w") as f:
                net.save_graph(f.name)
                with open(f.name, "r", encoding="utf-8") as html_file:
                    html_content = html_file.read()
                st.components.v1.html(html_content, height=620)
                os.unlink(f.name)

        except ImportError:
            st.warning("PyVis not installed. Install with: pip install pyvis")

        # Centrality analysis
        st.markdown("### 📊 Top Nodes by Centrality (PageRank)")
        top_nodes = orchestrator.kg.get_centrality(top_n=10)
        if top_nodes:
            for rank, (node_id, score) in enumerate(top_nodes, 1):
                node = orchestrator.kg.get_node(node_id)
                name = node.get("name", node.get("title", node_id)) if node else node_id
                ntype = node.get("node_type", "?") if node else "?"
                st.markdown(f"**{rank}.** {name} ({ntype}) — PageRank: {score:.4f}")
    else:
        st.info("Knowledge graph is empty. Run the analysis pipeline or load sample data from Home.")


# ── Page: Gap Analysis ───────────────────────────────────────────
elif page == "🔍 Gap Analysis":
    st.markdown("## 🔍 Research Gap Analysis")
    st.markdown("Discover underexplored areas, contradictions, and missing methodologies.")
    st.markdown("---")

    orchestrator = get_orchestrator()

    if orchestrator.kg.graph.number_of_nodes() > 0:
        top_n = st.slider("Number of gaps to detect", 3, 20, 10)

        if st.button("🔍 Detect Research Gaps", type="primary", use_container_width=True):
            with st.spinner("Analyzing knowledge graph for research gaps..."):
                gaps = orchestrator.gap_agent.process(top_n=top_n)
                st.session_state.gaps = gaps

        gaps = st.session_state.get("gaps", [])
        if gaps:
            st.markdown(f"### Found {len(gaps)} Research Gaps")

            for gap in gaps:
                novelty_color = "🔴" if gap.novelty_score > 0.7 else "🟡" if gap.novelty_score > 0.4 else "🟢"

                with st.expander(f"{novelty_color} #{gap.priority_rank}: {gap.topic}", expanded=(gap.priority_rank <= 3)):
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Novelty Score", f"{gap.novelty_score:.2f}")
                    with col2:
                        st.metric("Gap Type", gap.gap_type.replace("_", " ").title())
                    with col3:
                        st.metric("Evidence Papers", len(gap.evidence_papers))

                    st.markdown(f"**Description:** {gap.description}")

                    if gap.evidence_papers:
                        st.markdown("**Supporting Papers:**")
                        for pid in gap.evidence_papers[:5]:
                            node = orchestrator.kg.get_node(pid)
                            if node:
                                st.markdown(f"- {node.get('title', pid)}")
        else:
            st.info("Click 'Detect Research Gaps' to run the analysis.")
    else:
        st.info("Knowledge graph is empty. Load data from the Home page first.")


# ── Page: Experiment Lab ─────────────────────────────────────────
elif page == "🧪 Experiment Lab":
    st.markdown("## 🧪 Experiment Suggestion Lab")
    st.markdown("Get concrete experiment proposals based on detected research gaps.")
    st.markdown("---")

    orchestrator = get_orchestrator()
    gaps = st.session_state.get("gaps", [])

    if gaps:
        st.markdown(f"### {len(gaps)} gaps available for experiment generation")

        selected_gaps = st.multiselect(
            "Select gaps to generate experiments for:",
            [f"#{g.priority_rank}: {g.topic}" for g in gaps],
            default=[f"#{gaps[0].priority_rank}: {gaps[0].topic}"] if gaps else [],
        )

        if st.button("🧪 Generate Experiments", type="primary", use_container_width=True):
            selected_indices = [
                int(s.split(":")[0].replace("#", "").strip()) - 1
                for s in selected_gaps
            ]
            selected_gap_objects = [gaps[i] for i in selected_indices if i < len(gaps)]

            with st.spinner("Generating experiment suggestions..."):
                experiments = orchestrator.experiment_agent.process(gaps=selected_gap_objects)
                st.session_state.experiments = experiments

        experiments = st.session_state.get("experiments", [])
        if experiments:
            for exp in experiments:
                with st.expander(f"🧪 {exp.title}", expanded=True):
                    st.markdown(f"**Hypothesis:** {exp.hypothesis}")
                    st.markdown(f"**Difficulty:** {'⭐' * {'easy': 1, 'medium': 2, 'hard': 3}.get(exp.difficulty, 2)}")

                    st.markdown("---")
                    st.markdown("**Methodology:**")
                    st.text(exp.methodology)

                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown("**Recommended Datasets:**")
                        for ds in exp.recommended_datasets:
                            st.markdown(f"- {ds}")
                    with col2:
                        st.markdown("**Variables to Measure:**")
                        for var in exp.variables:
                            st.markdown(f"- {var}")

                    st.markdown(f"**Expected Outcomes:** {exp.expected_outcomes}")

                    # Export button
                    export_md = f"# {exp.title}\n\n"
                    export_md += f"## Hypothesis\n{exp.hypothesis}\n\n"
                    export_md += f"## Methodology\n{exp.methodology}\n\n"
                    export_md += f"## Datasets\n" + "\n".join(f"- {d}" for d in exp.recommended_datasets) + "\n\n"
                    export_md += f"## Variables\n" + "\n".join(f"- {v}" for v in exp.variables) + "\n\n"
                    export_md += f"## Expected Outcomes\n{exp.expected_outcomes}\n"

                    st.download_button(
                        "📥 Export as Markdown",
                        export_md,
                        file_name=f"experiment_{exp.suggestion_id}.md",
                        key=f"export_{exp.suggestion_id}",
                    )
    else:
        st.info("Run Gap Analysis first to detect gaps, then generate experiment suggestions.")


# ── Page: Trend Forecast ─────────────────────────────────────────
elif page == "📈 Trend Forecast":
    st.markdown("## 📈 Research Trend Forecast")
    st.markdown("Predict emerging research topics using citation network analysis.")
    st.markdown("---")

    orchestrator = get_orchestrator()

    if orchestrator.kg.graph.number_of_nodes() > 0:
        col1, col2 = st.columns(2)
        with col1:
            time_horizon = st.selectbox("Prediction Horizon", ["5_years", "10_years"], format_func=lambda x: x.replace("_", " ").title())
        with col2:
            top_n = st.slider("Number of predictions", 3, 20, 10)

        if st.button("📈 Predict Trends", type="primary", use_container_width=True):
            with st.spinner("Analyzing citation patterns and computing predictions..."):
                predictions = orchestrator.trend_agent.process(
                    time_horizon=time_horizon,
                    top_n=top_n,
                )
                st.session_state.predictions = predictions

        predictions = st.session_state.get("predictions", [])
        if predictions:
            st.markdown(f"### 🔮 Predicted Emerging Topics ({time_horizon.replace('_', ' ').title()})")

            # Summary chart
            import plotly.graph_objects as go

            fig = go.Figure()
            topics = [p.topic[:25] + "..." if len(p.topic) > 25 else p.topic for p in predictions]
            confidences = [p.confidence_score for p in predictions]
            growth_rates = [max(0, p.growth_rate) for p in predictions]

            fig.add_trace(go.Bar(
                x=topics,
                y=confidences,
                name="Confidence Score",
                marker_color="rgba(102, 126, 234, 0.8)",
            ))

            fig.update_layout(
                title="Trend Prediction Confidence",
                xaxis_title="Topic",
                yaxis_title="Score",
                template="plotly_dark",
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                height=400,
            )
            st.plotly_chart(fig, use_container_width=True)

            # Detailed cards
            for pred in predictions:
                confidence_emoji = "🔥" if pred.confidence_score > 0.6 else "📈" if pred.confidence_score > 0.3 else "🌱"

                with st.expander(f"{confidence_emoji} {pred.topic}", expanded=(pred.confidence_score > 0.5)):
                    cols = st.columns(4)
                    with cols[0]:
                        st.metric("Confidence", f"{pred.confidence_score:.1%}")
                    with cols[1]:
                        st.metric("Growth Rate", f"{pred.growth_rate:+.2f} papers/yr")
                    with cols[2]:
                        st.metric("Citation Velocity", f"{pred.citation_velocity:+.2f}")
                    with cols[3]:
                        st.metric("Current Papers", pred.current_paper_count)

                    st.markdown(f"**Analysis:** {pred.description}")
        else:
            st.info("Click 'Predict Trends' to run the analysis.")
    else:
        st.info("Knowledge graph is empty. Load data from the Home page first.")


# ── Sidebar Status ───────────────────────────────────────────────
with st.sidebar:
    orchestrator = get_orchestrator()
    stats = orchestrator.get_graph_stats()
    st.markdown(f"**Nodes:** {stats.get('total_nodes', 0)}")
    st.markdown(f"**Edges:** {stats.get('total_edges', 0)}")
    st.markdown("---")
    st.markdown("*Built with 🤖 free/open-source AI*")
    st.markdown("*No paid APIs required*")
