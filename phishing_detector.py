def load_indicators(file_path):
    try:
        with open(file_path) as f:
            return set(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        return set()

def detect_phishing(entries):
    suspicious_ips = load_indicators("indicators/blacklisted_ips.txt")
    suspicious_urls = load_indicators("indicators/suspicious_urls.txt")

    flagged = []
    for entry in entries:
        if entry["ip"] in suspicious_ips or any(ind in entry["url"] for ind in suspicious_urls):
            flagged.append(entry["raw"])
    return flagged

