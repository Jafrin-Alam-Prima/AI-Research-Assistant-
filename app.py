"""
ResearchAI - Root entry point for Streamlit.
Launches the dashboard app so 'streamlit run app.py' works.
"""
import runpy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
runpy.run_path(ROOT / "dashboard" / "app.py", run_name="__main__")
