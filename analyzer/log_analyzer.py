def analyze_log_line(line):
    line = line.lower()

    if "timeout" in line:
        return "Possible cause: Slow response or network latency"

    elif "connection refused" in line:
        return "Possible cause: Service is down or port closed"

    elif "database" in line and "connection" in line:
        return "Possible cause: Database not reachable"

    elif "500" in line:
        return "Possible cause: Backend failure"

    elif "unavailable" in line:
        return "Possible cause: Service not running"

    return "Unknown issue"