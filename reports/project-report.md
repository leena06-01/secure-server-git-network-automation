# Secure Server Git Network Automation
## Project Report

### 1. Project Overview

This project demonstrates Linux server administration,
network troubleshooting, and routine task automation using
Bash, Python, and Git.

It focuses on practical tasks commonly performed by
junior Cloud and DevOps engineers.

### 2. Objectives

- Automate system health checks.
- Monitor log files for errors and warnings.
- Create compressed backups of project files.
- Verify backup archive metadata and integrity.
- Collect Linux system information using Python.
- Check basic network connectivity and DNS resolution.
- Audit local Linux user accounts.
- Track changes using Git and GitHub.

### 3. Technologies Used

- Linux
- Bash
- Python 3
- Git and GitHub
- Networking fundamentals
- Nginx
- Linux system utilities

### 4. Implemented Automation

#### System Health
Collects system information, disk and memory usage,
uptime, process information, and Nginx status.

#### Backup Automation
Creates timestamped compressed archives and reports
whether the operation succeeded.

#### Log Monitoring
Counts warning and error entries and displays
matching log lines.

#### User Audit
Reports local account information, login-shell
configuration, and accounts with UID 0.

#### Python System Information
Collects operating-system and resource information.

#### Python Network Check
Tests the network operations implemented in the script,
such as hostname lookup, connectivity, and port access.

#### Python Log Analyzer
Counts log levels and identifies error entries.

#### Python Backup Checker
Lists matching backup archives, their sizes, and
modification times.

### 5. Testing and Validation

- Checked Python syntax.
- Checked Bash syntax.
- Executed the system health script.
- Created a compressed backup.
- Listed archive contents to test readability.
- Executed the user audit script.
- Tested network and system information scripts.
- Verified log monitoring against sample data.

### 6. Skills Gained

- Linux command-line administration
- Bash scripting
- Python automation
- Basic network troubleshooting
- Log analysis
- Backup management
- User-account auditing
- Git version control
- Troubleshooting and validation

### 7. Future Improvements

- Add automated backup retention and cleanup.
- Schedule health checks using cron.
- Improve backup verification with test extraction.
- Add automated tests for Python scripts.
- Integrate checks into a CI/CD pipeline.
- Extend monitoring to a cloud-hosted Linux server.

### 8. Conclusion

This project provides practical experience in Linux
administration, automation, networking, and version control.
It serves as a foundation for more advanced Cloud and
DevOps projects.
