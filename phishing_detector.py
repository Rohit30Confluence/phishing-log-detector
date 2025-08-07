def load_indicators(file_path):
    try:
        with open(file_path) as f:
            return set(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        return set()


def detect_phishing(parsed_logs, blacklisted_ips, suspicious_urls):
    detected = []
    for entry in parsed_logs:
        ip = entry.get("ip", "")
        url = entry.get("url", "")

        reasons = []
        if ip in blacklisted_ips:
            reasons.append("Blacklisted IP")
        if any(susp_url in url for susp_url in suspicious_urls):
            reasons.append("Suspicious URL")

        if reasons:
            entry["reason"] = ", ".join(reasons)
            detected.append(entry)
    return detected


