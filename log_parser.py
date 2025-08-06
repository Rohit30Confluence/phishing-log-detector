import re

def parse_log(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    entries = []
    for line in lines:
        match = re.search(r'(?P<ip>\d+\.\d+\.\d+\.\d+).*?(https?://\S+)?', line)
        if match:
            entries.append({
                "ip": match.group("ip"),
                "url": match.group(2) or "",
                "raw": line.strip()
            })
    return entries

