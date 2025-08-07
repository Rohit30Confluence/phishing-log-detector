import argparse
from log_parser import read_log_file, parse_log_line
from phishing_detector import detect_phishing, load_indicators
from report_writer import write_csv_report

def main():
    parser = argparse.ArgumentParser(description="Phishing Log Detector")
    parser.add_argument('--log', required=True, help='Path to log file')
    parser.add_argument('--report', required=True, help='Path to output report')
    args = parser.parse_args()

    log_lines = read_log_file(args.log)
    parsed_logs = [parse_log_line(line) for line in log_lines]

    blacklisted_ips = load_indicators("indicators/blacklisted_ips.txt")
    suspicious_urls = load_indicators("indicators/suspicious_urls.txt")

    results = detect_phishing(parsed_logs, blacklisted_ips, suspicious_urls)

    print(f"\n[+] {len(results)} phishing attempts detected:")
    for r in results:
        print(f'{r["ip"]} [{r["timestamp"]}] "{r["url"]}" - Reason: {r["reason"]}')

    write_csv_report(results, args.report)

if __name__ == "__main__":
    main()

