# macOS-Style Linux ISO 

A custom Ubuntu-based Linux distribution featuring macOS-style aesthetics including a blurred dock, macOS-like top bar, and system information panel.

## Features

- **macOS-style Dock**: Plank dock with blur effects and smooth animations
- **macOS-like Top Bar**: Custom XFCE panel positioned at top with Apple menu and system indicators
- **System Info Panel**: Click the Apple logo menu → "About This Computer" to view:
  - CPU model and cores
  - RAM capacity
  - GPU information
  - Storage details
  - System distribution and kernel info
  - Network hostname
- **Sequoia Wallpaper**: Beautiful macOS Sequoia-inspired background
- **Pre-installed Apps**: Firefox, file manager, terminal, text editor, media player, and more
- **Blur Effects**: Compositor-powered transparency and blur throughout the desktop

## Building the ISO

### Prerequisites

You need a Debian/Ubuntu-based Linux system with the following installed:

```bash
sudo apt-get update
sudo apt-get install -y live-build debootstrap squashfs-tools xorriso isolinux syslinux-efi
```

### Build Instructions

1. Clone or download this project
2. Run the build script:

```bash
cd macos-style-linux
chmod +x build-iso.sh
./build-iso.sh
```

3. The ISO will be created as `macOS-Style-Linux.iso` in the project root

**Note**: The build process requires root privileges and takes approximately 20-30 minutes depending on your internet connection and system speed.

## Using the ISO

1. Burn the ISO to a USB drive using Rufus (Windows) or `dd` (Linux):
   ```bash
   sudo dd if=macOS-Style-Linux.iso of=/dev/sdX bs=4M status=progress
   ```
   (Replace `/dev/sdX` with your USB device)

2. Boot from the USB drive

3. Try the live system or install to your hard drive using the included Calamares installer

## Post-Installation

After installation, the macOS-style desktop will be automatically configured on first login. You can manually reconfigure by running:

```bash
setup-macos-desktop
```

## Desktop Components

### Dock (Plank)
- Positioned at bottom center
- Auto-zoom on hover (150% zoom)
- Transparent with blur background
- Pre-loaded apps: Firefox, Files, Terminal, Text Editor, Video Player

### Top Bar
- Positioned at top of screen
- Apple logo menu (whiskermenu) for applications
- Quick launchers for common apps
- System tray with network, volume, notifications
- Clock with macOS-style date/time format
- System menu with power options

### System Info Panel
Access via the Apple menu → "About This Computer"

Shows real-time system information:
- **Processor**: Model name and core count
- **Memory**: Total RAM installed
- **Graphics**: GPU vendor and model
- **Storage**: Disk usage statistics
- **System**: Distribution, kernel version, architecture, uptime
- **Network**: Hostname

## Customization

### Changing the Wallpaper
Right-click desktop → Desktop Settings → Background → Select new image

### Dock Settings
Right-click on dock → Preferences

### Panel Settings
Right-click on top panel → Panel → Panel Preferences

## Included Software

- **Desktop Environment**: XFCE4 with macOS theming
- **Web Browser**: Firefox
- **File Manager**: Thunar
- **Terminal**: XFCE4 Terminal
- **Text Editor**: Mousepad
- **Media Player**: Parole
- **System Monitor**: GNOME System Monitor
- **Calculator**: GNOME Calculator

## Technical Details

- **Base**: Ubuntu 22.04 LTS (Jammy Jellyfish)
- **Architecture**: amd64
- **Desktop**: XFCE4
- **Dock**: Plank
- **Compositor**: Picom (with dual_kawase blur)
- **Display Manager**: LightDM
- **Installer**: Calamares

## File Structure

```
.
├── build-iso.sh                          # Main build script
├── config/
│   ├── hooks/normal/                     # Build-time configuration scripts
│   │   ├── 0010-download-themes.hook.chroot    # Download themes & wallpaper
│   │   ├── 0020-configure-dock.hook.chroot     # Configure Plank dock
│   │   ├── 0030-configure-topbar.hook.chroot   # Configure top panel
│   │   └── 9990-setup-macos-desktop.hook.chroot # Final setup
│   ├── includes.chroot/
│   │   └── usr/local/bin/
│   │       ├── system-info-panel         # Python system info app
│   │       └── setup-macos-desktop       # Desktop setup script
│   └── package-lists/
│       ├── base.list.chroot              # Base system packages
│       ├── desktop.list.chroot           # Desktop environment packages
│       ├── dock.list.chroot              # Dock and compositor packages
│       └── apps.list.chroot              # Application packages
└── README.md
```

## Troubleshooting

### No blur effects
Ensure Picom is running:
```bash
picom --config ~/.config/picom/picom.conf &
```

### Dock not appearing
Start Plank manually:
```bash
plank &
```

### System info not displaying
Run the system info panel directly:
```bash
/usr/local/bin/system-info-panel
```

## Credits

- Based on Ubuntu 22.04 LTS
- McOS theme by paullinuxthemer
- Papirus icon theme
- Plank dock by elementary OS team
- XFCE desktop environment

## License

This project is provided as-is for educational and personal use. Ubuntu is a trademark of Canonical Ltd. macOS is a trademark of Apple Inc. This distribution is not affiliated with or endorsed by Apple Inc.
