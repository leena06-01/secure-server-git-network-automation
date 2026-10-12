#!/usr/bin/env python3

import subprocess
import socket


print("======================================")
print("       NETWORK CHECK")
print("======================================")


# Check hostname
hostname = socket.gethostname()
print("\nHostname:", hostname)


# Check IP address
try:
    ip_address = socket.gethostbyname(hostname)
    print("IP Address:", ip_address)
except socket.gaierror:
    print("IP Address: Unable to determine")


# Check localhost connectivity
print("\n===== LOCALHOST CONNECTIVITY =====")

result = subprocess.run(
    ["ping", "-c", "2", "127.0.0.1"],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)

if result.returncode == 0:
    print("Localhost: OK")
else:
    print("Localhost: FAILED")


# Check DNS resolution
print("\n===== DNS RESOLUTION =====")

try:
    socket.gethostbyname("google.com")
    print("DNS: OK")
except socket.gaierror:
    print("DNS: FAILED")


# Check HTTP connectivity
print("\n===== INTERNET CONNECTIVITY =====")

try:
    socket.create_connection(("google.com", 80), timeout=5)
    print("HTTP Connection: OK")
except OSError:
    print("HTTP Connection: FAILED")


print("\n======================================")
print("       NETWORK CHECK COMPLETE")
print("======================================")
