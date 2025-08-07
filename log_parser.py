def read_log_file(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def parse_log_line(line):
    import re
    pattern = r'(?P<ip>\S+) - - \[(?P<timestamp>.*?)\] "\S+ (?P<url>\S+) HTTP/\S+"'
    match = re.search(pattern, line)
    if match:
        return {
            "ip": match.group("ip"),
            "timestamp": match.group("timestamp"),
            "url": match.group("url"),
            "raw": line
        }
    return {"ip": "", "timestamp": "", "url": "", "raw": line}

