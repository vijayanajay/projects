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
    os.chdir(tmp_path)
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

def test_pipeline_uses_config_params(tmp_path, monkeypatch):
    """
    Ensure pipeline loads initial_cash and position_size from config.json and passes them to backtest/report.
    """
    import sys, json, shutil
    os.chdir(tmp_path)
    reports_dir = tmp_path / "reports"
    if reports_dir.exists():
        shutil.rmtree(reports_dir)
    config = {
        "period": "1y",
        "initial_cash": 5555,
        "position_size": 123,
        "strategy": "naive_momentum",
        "strategy_params": {"short_window": 5, "long_window": 10}
    }
    config_path = tmp_path / "config.json"
    with open(config_path, "w") as f:
        json.dump(config, f)
    ticker = "TCS.NS"
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from pipeline import run_pipeline
    monkeypatch.chdir(tmp_path)
    run_pipeline([ticker], output_dir=tmp_path, config_path=config_path)
    md_path = tmp_path / "reports/portfolio_report.md"
    assert md_path.exists(), "Pipeline did not generate portfolio Markdown report."
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    assert "set to: 123 currency units per trade, initial cash: 5555" in text, "Report did not use config.json values for sizing."

def test_pipeline_missing_config_keys(tmp_path):
    """
    Ensure pipeline errors if config.json is missing required keys.
    """
    import sys, json
    os.chdir(tmp_path)
    config = {"period": "1y", "strategy": "naive_momentum", "strategy_params": {}}
    config_path = tmp_path / "config.json"
    with open(config_path, "w") as f:
        json.dump(config, f)
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from pipeline import run_pipeline
    try:
        run_pipeline(["TCS.NS"], output_dir=tmp_path, config_path=config_path)
        assert False, "Pipeline should error if config keys are missing."
    except KeyError as e:
        assert "initial_cash" in str(e) or "position_size" in str(e)
