#!/usr/bin/env python3
"""
Alternative Windows build script for creating the Linux ISO configuration.
This generates all necessary files that can then be built on a Linux system.
"""

import os
import sys

# Since we're on Windows, create a batch file to help with setup
def create_windows_helper():
    batch_content = '''@echo off
echo ===================================================
echo macOS-Style Linux ISO - Windows Setup Helper
echo ===================================================
echo.
echo This project requires a Linux environment to build the ISO.
echo.
echo Options:
echo 1. Use WSL (Windows Subsystem for Linux)
echo 2. Use a Linux VM
echo 3. Use Docker Desktop with Linux containers
echo.
echo.
echo To build using WSL:
echo   1. Install WSL: wsl --install
echo   2. Open WSL terminal
echo   3. Navigate to this folder
echo   4. Run: chmod +x build-iso.sh ^&^& ./build-iso.sh
echo.
pause
'''
    return batch_content

def create_dockerfile():
    dockerfile = '''FROM ubuntu:22.04

# Install build dependencies
RUN apt-get update && apt-get install -y \\
    live-build \\
    debootstrap \\
    squashfs-tools \\
    xorriso \\
    isolinux \\
    syslinux-efi \\
    curl \\
    wget \\
    git \\
    && rm -rf /var/lib/apt/lists/*

WORKDIR /build

CMD ["/bin/bash"]
'''
    return dockerfile

def main():
    # Create Windows helper batch file
    batch_file = create_windows_helper()
    with open('setup-windows.bat', 'w') as f:
        f.write(batch_file)
    print("Created: setup-windows.bat")

    # Create Dockerfile for Docker-based builds
    dockerfile = create_dockerfile()
    with open('Dockerfile', 'w') as f:
        f.write(dockerfile)
    print("Created: Dockerfile")

    print("\nWindows helper files created successfully!")
    print("\nTo build this ISO on Windows, you can:")
    print("1. Use WSL2 (recommended):")
    print("   wsl --install")
    print("   Then in WSL: cd /mnt/c/path/to/project && ./build-iso.sh")
    print("\n2. Use Docker:")
    print("   docker build -t iso-builder .")
    print("   docker run -it -v %cd%:/build iso-builder")
    print("   Then in container: ./build-iso.sh")
    print("\n3. Use a Linux VM or cloud Linux server")

def main():
    # Create Windows helper batch file
    batch_file = create_windows_helper()
    with open('setup-windows.bat', 'w') as f:
        f.write(batch_file)
    print("Created: setup-windows.bat")

    # Create Dockerfile for Docker-based builds
    dockerfile = create_dockerfile()
    with open('Dockerfile', 'w') as f:
        f.write(dockerfile)
    print("Created: Dockerfile")

    print("\nWindows helper files created successfully!")
    print("\nTo build this ISO on Windows, you can:")
    print("1. Use WSL2 (recommended):")
    print("   wsl --install")
    print("   Then in WSL: cd /mnt/c/path/to/project && ./build-iso.sh")
    print("\n2. Use Docker:")
    print("   docker build -t iso-builder .")
    print("   docker run -it -v %cd%:/build iso-builder")
    print("   Then in container: ./build-iso.sh")
    print("\n3. Use a Linux VM or cloud Linux server")

if __name__ == '__main__':
    main()
