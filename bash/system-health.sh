#!/bin/bash

echo "======================================"
echo "       SYSTEM HEALTH CHECK"
echo "======================================"

echo ""
echo "===== SYSTEM INFORMATION ====="

echo "Date: $(date)"
echo "Hostname: $(hostname)"
echo "Current User: $(whoami)"
echo "IP Address: $(hostname -I)"

echo ""
echo "===== DISK USAGE ====="

DISK_USAGE=$(df / | awk 'NR==2 {print $5}' | tr -d '%')

echo "Root Disk Usage: ${DISK_USAGE}%"

if [ "$DISK_USAGE" -ge 90 ]
then
    echo "Disk Status: CRITICAL"
elif [ "$DISK_USAGE" -ge 80 ]
then
    echo "Disk Status: WARNING"
else
    echo "Disk Status: OK"
fi

echo ""
echo "===== MEMORY USAGE ====="

MEMORY_USAGE=$(free | awk '/Mem:/ {printf "%.0f", $3/$2 * 100}')

echo "Memory Usage: ${MEMORY_USAGE}%"

if [ "$MEMORY_USAGE" -ge 90 ]
then
    echo "Memory Status: CRITICAL"
elif [ "$MEMORY_USAGE" -ge 80 ]
then
    echo "Memory Status: WARNING"
else
    echo "Memory Status: OK"
fi

echo ""
echo "===== SYSTEM LOAD ====="

uptime

echo ""
echo "===== TOP PROCESSES ====="

ps aux --sort=-%cpu | head -6

echo ""
echo "===== NGINX STATUS ====="

if systemctl is-active --quiet nginx
then
    echo "Nginx Status: OK - RUNNING"
else
    echo "Nginx Status: CRITICAL - DOWN"
fi

echo ""
echo "======================================"
echo "       HEALTH CHECK COMPLETE"
echo "======================================"
