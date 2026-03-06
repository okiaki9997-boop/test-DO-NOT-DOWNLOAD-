#!/bin/bash
set -e

# macOS-Style Linux ISO Builder
# This script builds a custom Ubuntu-based ISO with macOS aesthetics

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUILD_DIR="$SCRIPT_DIR/build"
ISO_NAME="mac.iso"

echo "=== macOS-Style Linux ISO Builder ==="
echo "Setting up build environment..."

# Create build directory structure
mkdir -p "$BUILD_DIR"
cd "$BUILD_DIR"

# Install required tools if not present
if ! command -v lb &> /dev/null; then
    echo "Installing live-build tools..."
    sudo apt-get update
    sudo apt-get install -y live-build debootstrap squashfs-tools xorriso isolinux syslinux-efi
fi

# Initialize live-build
lb config \
    --distribution jammy \
    --architecture amd64 \
    --binary-images iso-hybrid \
    --debian-installer none \
    --archive-areas "main restricted universe multiverse" \
    --parent-archive-areas "main restricted universe multiverse" \
    --parent-mirror-bootstrap http://archive.ubuntu.com/ubuntu/ \
    --parent-mirror-binary http://archive.ubuntu.com/ubuntu/ \
    --mirror-bootstrap http://archive.ubuntu.com/ubuntu/ \
    --mirror-binary http://archive.ubuntu.com/ubuntu/ \
    --bootappend-live "boot=casper quiet splash"

# Copy our custom configurations
cp -r "$SCRIPT_DIR/config"/* config/

# Build the ISO
echo "Building ISO (this may take 20-30 minutes)..."
sudo lb build

# Move ISO to output
mv live-image-amd64.hybrid.iso "$SCRIPT_DIR/$ISO_NAME"
echo "=== Build Complete ==="
echo "ISO created: $ISO_NAME"
