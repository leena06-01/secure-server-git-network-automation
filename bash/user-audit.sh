#!/bin/bash

set -u

echo "===== USER ACCOUNT AUDIT ====="
echo "Date: $(date)"
echo "Hostname: $(hostname)"
echo

echo "===== TOTAL LOCAL ACCOUNTS ====="
awk 'END { print "Total accounts:", NR }' /etc/passwd

echo
echo "===== ACCOUNTS WITH LOGIN SHELLS ====="

awk -F: '
    $7 !~ /(nologin|false)$/ {
        printf "Username: %-20s Shell: %s\n", $1, $7
    }
' /etc/passwd

echo
echo "===== ACCOUNTS WITH UID 0 ====="

awk -F: '$3 == 0 {
    printf "Username: %s | UID: %s\n", $1, $3
}' /etc/passwd

echo
echo "===== AUDIT COMPLETE ====="
