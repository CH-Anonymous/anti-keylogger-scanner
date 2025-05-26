````markdown
# 🛡️ Anti-Keylogger Scanner

A lightweight and easy-to-use Windows tool built with Python and Tkinter to detect potential keyloggers running on your system.

![Anti-Keylogger Scanner GUI](screenshot.png)

---

## 🔍 Features

- **Startup Entry Scan** – Detects suspicious programs in the Windows registry's auto-run section.
- **Running Process Scan** – Identifies active processes that resemble common keyloggers.
- **Terminate Processes** – Allows you to safely terminate flagged processes.
- **Save Scan Results** – Export your scan report as a `.txt` file.
- **Standalone EXE** – Use without installing Python. One-click `.exe` available.

---

## 🚀 How to Use

### 🔧 Option 1: Run the Executable (Recommended for End Users)

1. Go to the [Releases](https://github.com/CH-Anonymous/anti-keylogger-scanner/releases) section.
2. Download the latest `AntiKeyloggerScanner.exe` file.
3. Double-click to launch the GUI tool.
4. Click "Scan System" to find suspicious activity.
5. Optionally terminate processes or save results.

> ✅ Works on Windows 10 and 11

---

### 🛠 Option 2: Run the Source Code (For Developers)

#### 🔗 Clone the Repo

```bash
git clone https://github.com/CH-Anonymous/anti-keylogger-scanner.git
cd anti-keylogger-scanner
````

#### 📦 Install Requirements

Make sure Python is installed. Then:

```bash
pip install -r requirements.txt
```

Or install dependencies manually:

```bash
pip install psutil
```

#### ▶️ Run the App

```bash
python anti_keylogger_gui.py
```

---

## 🛑 How to Build .EXE from Source (For Devs)

If you want to generate your own `.exe` file:

1. Install **PyInstaller**:

```bash
pip install pyinstaller
```

2. Build the executable:

```bash
pyinstaller --onefile --windowed --icon=icon.ico anti_keylogger_gui.py
```

Your `.exe` file will appear in the `dist/` directory.

---

## 🧠 How It Works

* **Registry Scan**: Looks for suspicious keys in `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`.
* **Process Scan**: Filters running processes with suspicious names or AppData paths.
* **Results Output**: Highlights all suspicious matches for user review.

---

## 📁 Project Structure

```
anti-keylogger-scanner/
├── anti_keylogger_gui.py       # Main script
├── favicon.ico                    # App icon (optional)
├── README.md                   # This file
├── dist/                       # Contains compiled .exe after build
└── requirements.txt            # Python dependencies
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the project and submit pull requests.

---

## 📧 Contact

Developed by **Chirag Khatri**
GitHub: [CH-Anonymous](https://github.com/CH-Anonymous)

```

---

Let me know if you'd like the `requirements.txt`, `LICENSE`, or icon file too.
```
