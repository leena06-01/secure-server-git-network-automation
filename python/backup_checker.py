#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime

BACKUP_DIR = Path.home() / "backups"

def check_backups():
    print("===== BACKUP CHECKER =====")

    if not BACKUP_DIR.is_dir():
        print(f"ERROR: Backup directory not found: {BACKUP_DIR}")
        return False

    backups = sorted(
        BACKUP_DIR.glob("secure-server-backup-*.tar.gz"),
        key=lambda path: path.stat().st_mtime,
        reverse=True,
    )

    if not backups:
        print("WARNING: No backup archives found.")
        return False

    for backup in backups:
        size = backup.stat().st_size
        modified = datetime.fromtimestamp(
            backup.stat().st_mtime
        ).strftime("%Y-%m-%d %H:%M:%S")

        print(f"\nFile: {backup.name}")
        print(f"Size: {size} bytes")
        print(f"Last modified: {modified}")

        if size == 0:
            print("Status: CRITICAL - Backup is empty")
        else:
            print("Status: OK - Backup file is not empty")

    print("\n===== CHECK COMPLETE =====")
    return True

if __name__ == "__main__":
    if not check_backups():
        raise SystemExit(1)
