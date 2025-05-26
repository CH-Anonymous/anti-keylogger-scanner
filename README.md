````markdown
# 🛡️ Anti-Keylogger Scanner

A lightweight and easy-to-use Windows tool built with Python and Tkinter to detect potential keyloggers running on your system.

![Anti-Keylogger Scanner GUI](screenshot.png)

---

## 📥 Download the EXE

> ✅ No Python installation required  
> 📦 Just one file – portable and ready to run!

**👉 [Download AntiKeyloggerScanner.exe](https://github.com/CH-Anonymous/anti-keylogger-scanner/releases/latest/download/AntiKeyloggerScanner.exe)**

---

## 🔍 Features

- **Startup Entry Scan** – Detects suspicious programs in the Windows registry's auto-run section.
- **Running Process Scan** – Identifies active processes that resemble common keyloggers.
- **Terminate Processes** – Allows you to safely terminate flagged processes.
- **Save Scan Results** – Export your scan report as a `.txt` file.
- **Standalone EXE** – Use without installing Python. One-click `.exe` available.

---

## 🚀 How to Use

### Option 1: Run the EXE (Recommended)

1. Click [here to download](https://github.com/CH-Anonymous/anti-keylogger-scanner/releases/latest/download/AntiKeyloggerScanner.exe).
2. Double-click the file to open the scanner.
3. Click **"Scan System"** to detect suspicious activity.
4. Use **"Terminate Process"** to kill flagged processes.
5. Use **"Save Scan Results"** to export your scan.

---

### Option 2: Run from Source (For Developers)

#### 🔗 Clone the Repo

```bash
git clone https://github.com/CH-Anonymous/anti-keylogger-scanner.git
cd anti-keylogger-scanner
````

#### 📦 Install Requirements

```bash
pip install psutil
```

#### ▶️ Run the App

```bash
python anti_keylogger_gui.py
```

---

## 🛠 Build the Executable Yourself

1. Install PyInstaller:

```bash
pip install pyinstaller
```

2. Run this command to create an EXE:

```bash
pyinstaller --onefile --windowed --icon=icon.ico anti_keylogger_gui.py
```

> Your EXE will be inside the `dist/` folder.

---

## 🧠 How It Works

* **Registry Scan**: Looks at startup entries under Windows registry.
* **Process Scan**: Filters running processes from `AppData` with suspicious names.
* **Results Output**: Lists suspicious startup items and running processes.

---

## 📁 Project Structure

```
anti-keylogger-scanner/
├── anti_keylogger_gui.py
├── icon.ico
├── README.md
├── dist/
└── requirements.txt
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions, bug reports, and suggestions are welcome!

---

## 📧 Contact

Created by **Chirag Khatri**
GitHub: [@CH-Anonymous](https://github.com/CH-Anonymous)

```

---

📝 **Note**: Be sure you have uploaded your `AntiKeyloggerScanner.exe` in the GitHub **Releases** section under the latest release. If not, I can guide you through that as well.
```
