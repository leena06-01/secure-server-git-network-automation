#!/usr/bin/env python3

import socket
import platform
import subprocess
from datetime import datetime


print("=" * 45)
print("       LINUX SYSTEM INFORMATION")
print("=" * 45)

# Current date and time
print("\n===== DATE AND TIME =====")
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Hostname
print("\n===== HOSTNAME =====")
print(socket.gethostname())

# Operating system information
print("\n===== OPERATING SYSTEM =====")
print("System:", platform.system())
print("Release:", platform.release())
print("Architecture:", platform.machine())

# IP address
print("\n===== IP ADDRESS =====")

try:
    result = subprocess.run(
        ["hostname", "-I"],
        capture_output=True,
        text=True,
        check=True
    )

    print(result.stdout.strip() or "No IP address found")

except (subprocess.CalledProcessError, FileNotFoundError):
    print("Unable to retrieve IP address")

# Disk usage
print("\n===== DISK USAGE =====")

try:
    subprocess.run(["df", "-h", "/"], check=True)
except (subprocess.CalledProcessError, FileNotFoundError):
    print("Unable to retrieve disk usage")

# Memory usage
print("\n===== MEMORY USAGE =====")

try:
    subprocess.run(["free", "-h"], check=True)
except (subprocess.CalledProcessError, FileNotFoundError):
    print("Unable to retrieve memory usage")

# System uptime
print("\n===== SYSTEM UPTIME =====")

try:
    subprocess.run(["uptime"], check=True)
except (subprocess.CalledProcessError, FileNotFoundError):
    print("Unable to retrieve system uptime")

print("\n" + "=" * 45)
print("       SYSTEM REPORT COMPLETE")
print("=" * 45)
