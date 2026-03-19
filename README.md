# WorkSync

> A daily task details tracker for individuals and teams — built with Python, packaged as a native Windows desktop app.

---

## Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Running from Source](#running-from-source)
- [Building the Installer](#building-the-installer)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

---

## About

**WorkSync** is a lightweight Windows desktop application that helps you log and track your daily work tasks. Whether you are managing personal to-dos or keeping an organized record of work updates, WorkSync gives you a clean and simple interface to stay on top of what you do every day.

---

## Features

- 📋 Log and track daily task details
- 🖥️ Native Windows desktop application (no browser needed)
- ⚡ Fast and lightweight — runs silently in the background
- 🔧 Easy installation via a bundled Windows installer (`.exe`)
- 🗑️ Clean uninstall with full data removal

---

## Installation

### Option 1 — Windows Installer (Recommended)

1. Download the latest installer from the [Releases](https://github.com/Vishvshah16/WorkSync/releases) page.
2. Run `WorkSync-1.0.1.exe` and follow the setup wizard.
3. WorkSync will be installed to `Program Files\WorkSync` and launched automatically.

> **Note:** Administrator privileges are required during installation.

### Option 2 — Run from Source

See the [Running from Source](#running-from-source) section below.

---

## Running from Source

### Prerequisites

- Python 3.8 or higher
- `pip` package manager

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/Vishvshah16/WorkSync.git
cd WorkSync

# 2. (Optional) Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python code/main.py
```

---

## Building the Installer

WorkSync uses [PyInstaller](https://pyinstaller.org/) to bundle the app and [Inno Setup](https://jrsoftware.org/isinfo.php) to generate the Windows installer.

### Step 1 — Build the executable with PyInstaller

```bash
pyinstaller --noconfirm --onedir --windowed --icon=assets/icon.ico --name WorkSync code/main.py
```

This creates a `dist/WorkSync/` folder containing the bundled app.

### Step 2 — Build the installer with Inno Setup

1. Install [Inno Setup](https://jrsoftware.org/isinfo.php).
2. Open `InstallerBuilder.iss` in the Inno Setup Compiler.
3. Click **Build → Compile**.
4. The installer will be generated at `Package/Windows/WorkSync-1.0.1.exe`.

---

## Project Structure

```
WorkSync/
├── assets/                  # Icons and static resources
│   └── icon.ico
├── code/                    # Application source code (Python)
├── InstallerBuilder.iss     # Inno Setup installer script
├── LICENSE                  # MIT License
└── README.md
```

---

## Requirements

| Requirement     | Details                        |
|-----------------|--------------------------------|
| OS              | Windows 10 / 11                |
| Python          | 3.8+ (for running from source) |
| PyInstaller     | For building the executable    |
| Inno Setup      | For building the installer     |

---

## Contributing

Contributions are welcome! To get started:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit: `git commit -m "Add your feature"`
4. Push to your fork: `git push origin feature/your-feature-name`
5. Open a Pull Request.

Please make sure your code is clean and well-commented before submitting.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Author

**Vishva Shah**
[LinkedIn](https://www.linkedin.com/in/vishva-shah-1870361a5/) · [GitHub](https://github.com/Vishvshah16)

<p align="center">Made with ❤️ by <a href="https://github.com/Vishvshah16">Vishva Shah</a></p>
