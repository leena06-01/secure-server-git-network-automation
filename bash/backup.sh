#!/bin/bash

set -u

SOURCE="$HOME/secure-server-git-network-automation"
BACKUP_DIR="$HOME/backups"
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_FILE="$BACKUP_DIR/secure-server-backup-$TIMESTAMP.tar.gz"

echo "===== BACKUP STARTED ====="

# Check whether the source directory exists
if [ ! -d "$SOURCE" ]; then
    echo "ERROR: Source directory not found: $SOURCE"
    exit 1
fi

# Create the backup directory if needed
mkdir -p "$BACKUP_DIR"

# Create a compressed archive, excluding Git history
if tar -czf "$BACKUP_FILE" \
    --exclude="$SOURCE/.git" \
    -C "$(dirname "$SOURCE")" "$(basename "$SOURCE")"; then

    echo "SUCCESS: Backup created."
    echo "Location: $BACKUP_FILE"
    ls -lh "$BACKUP_FILE"
else
    echo "ERROR: Backup failed."
    rm -f "$BACKUP_FILE"
    exit 1
fi

echo "===== BACKUP COMPLETED ====="
