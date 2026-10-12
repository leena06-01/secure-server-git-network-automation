#!/bin/bash

set -u

LOG_FILE="$HOME/secure-server-git-network-automation/logs/sample-logs.md"

echo "===== LOG MONITOR ====="

if [ ! -f "$LOG_FILE" ]; then
    echo "ERROR: Log file not found: $LOG_FILE"
    exit 1
fi

echo "Log file: $LOG_FILE"
echo

ERROR_COUNT=$(grep -ciE 'ERROR|CRITICAL' "$LOG_FILE" || true)
WARNING_COUNT=$(grep -ci 'WARNING' "$LOG_FILE" || true)

echo "Errors/Critical entries: $ERROR_COUNT"
echo "Warning entries: $WARNING_COUNT"

echo
echo "===== ERROR DETAILS ====="

grep -inE 'ERROR|CRITICAL' "$LOG_FILE" || echo "No errors found."

echo
echo "===== MONITORING COMPLETE ====="
