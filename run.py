import argparse
from log_parser import parse_log
from phishing_detector import detect_phishing

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Phishing Log Detector")
    parser.add_argument("--log", required=True, help="Path to log file")
    args = parser.parse_args()

    entries = parse_log(args.log)
    results = detect_phishing(entries)

    print(f"[+] {len(results)} phishing attempts detected:")
    for line in results:
        print(line)

