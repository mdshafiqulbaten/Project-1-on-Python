from collections import Counter
import re

def analyze_log(file_path):
    with open(file_path) as f:
        lines = f.readlines()

    ip_count = Counter()
    for line in lines:
        match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
        if match:
            ip_count[match.group()] += 1

    print("Most common IPs:")
    for ip, count in ip_count.most_common(5):
        print(f"{ip}: {count} requests")

if __name__ == "__main__":
    path = input("Enter log file path: ")
    analyze_log(path)
