from analyzer.log_analyzer import analyze_log_line

def test_log_analysis():
    log = "ERROR: Database connection timeout"
    result = analyze_log_line(log)

    assert "possible cause" in result.lower()