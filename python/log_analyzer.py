#!/usr/bin/env python3

from pathlib import Path
from collections import Counter

# Locate the project and sample log file
PROJECT_DIR = Path(__file__).resolve().parent.parent
LOG_FILE = PROJECT_DIR / "logs" / "sample-logs.md"


def analyze_logs(file_path):
    counts = Counter()
    matching_entries = []

    try:
        with file_path.open("r", encoding="utf-8") as log_file:
            for line_number, line in enumerate(log_file, start=1):
                entry = line.strip()

                if not entry:
                    continue

                parts = entry.split(maxsplit=2)

                if len(parts) < 3:
                    counts["MALFORMED"] += 1
                    continue

                level = parts[2].split(maxsplit=1)[0].upper()

                if level in ("INFO", "WARNING", "ERROR", "CRITICAL"):
                    counts[level] += 1

                    if level in ("ERROR", "CRITICAL"):
                        matching_entries.append(
                            f"Line {line_number}: {entry}"
                        )
                else:
                    counts["UNKNOWN"] += 1

    except FileNotFoundError:
        print(f"ERROR: Log file not found: {file_path}")
        return False

    print("\n===== LOG ANALYSIS REPORT =====")
    print(f"Log file: {file_path}")
    print(f"INFO entries: {counts['INFO']}")
    print(f"WARNING entries: {counts['WARNING']}")
    print(f"ERROR entries: {counts['ERROR']}")
    print(f"CRITICAL entries: {counts['CRITICAL']}")
    print(f"Malformed entries: {counts['MALFORMED']}")
    print(f"Unknown entries: {counts['UNKNOWN']}")

    print("\n===== ERRORS REQUIRING INVESTIGATION =====")

    if matching_entries:
        for entry in matching_entries:
            print(entry)
    else:
        print("No ERROR or CRITICAL entries found.")

    print("\n===== ANALYSIS COMPLETE =====")
    return True


if __name__ == "__main__":
    success = analyze_logs(LOG_FILE)

    if not success:
        raise SystemExit(1)
