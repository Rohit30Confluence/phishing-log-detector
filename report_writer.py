import csv

def write_csv_report(results, report_path):
    with open(report_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Timestamp", "IP Address", "URL", "Reason"])
        writer.writeheader()
        for item in results:
            writer.writerow({
                "Timestamp": item["timestamp"],
                "IP Address": item["ip"],
                "URL": item["url"],
                "Reason": item["reason"]
            })

