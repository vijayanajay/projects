import os
import pytest
from pathlib import Path

def test_pipeline_generates_markdown_report(tmp_path):
    """
    TDD: Integration test for pipeline orchestration.
    Runs the pipeline for a ticker and asserts that a Markdown report is generated.
    """
    import sys
    import shutil
    # Ensure reports directory is clean
    reports_dir = tmp_path / "reports"
    if reports_dir.exists():
        shutil.rmtree(reports_dir)
    # Run pipeline for a known ticker (now expects a list)
    ticker = "TCS.NS"
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from pipeline import run_pipeline
    run_pipeline([ticker], output_dir=tmp_path)
    md_path = tmp_path / "reports/portfolio_report.md"
    assert md_path.exists(), f"Pipeline did not generate portfolio Markdown report."
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    assert "Technical Analysis Report" in text, "Markdown report missing expected content."
