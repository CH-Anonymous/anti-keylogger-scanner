# 🛡️ Anti-Keylogger Scanner

![GitHub release (latest by date)](https://img.shields.io/github/v/release/CH-Anonymous/anti-keylogger-scanner)
![Platform](https://img.shields.io/badge/platform-Windows-blue)
![Made with Python](https://img.shields.io/badge/made%20with-Python-3776AB?logo=python&logoColor=white)

A lightweight Windows-based Anti-Keylogger tool built in Python to detect suspicious startup entries and running processes that might be related to keylogging activities.

---

## 📦 Features

- 🔍 Scan for suspicious **startup registry entries**
- 🧠 Detect potentially harmful **background processes**
- ❌ Terminate flagged processes from within the app
- 💾 Save scan results to a `.txt` file
- 🖼️ Simple, intuitive GUI using `Tkinter`
- 🖥️ Standalone `.exe` version available for Windows

---

## 🚀 Download

👉 [Download the latest .exe](https://github.com/CH-Anonymous/anti-keylogger-scanner/releases/download/v1.0/anti_keylogger_gui.exe)

> ⚠️ Note: Windows Defender or other antivirus tools may flag the `.exe` since it interacts with processes and the registry. Rest assured, it is open-source and safe to use.

---

## 📸 Screenshots

### 🖼️ GUI Interface
![Scanner UI](images/scanner.png)
![Startup Entries](images/process_scan.png)

---

## 🧰 Installation (For Developers)

### Requirements

- Python 3.10 or later
- `psutil`
- `pyinstaller`

### Install Dependencies

```bash
pip install psutil
````

### Run the Script

```bash
python anti_keylogger_gui.py
```

### Build Executable

```bash
pyinstaller --onefile --windowed --icon=icon.ico anti_keylogger_gui.py
```

## 💻 How It Works

* Checks Windows registry startup entries (specifically keys under `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`)
* Monitors active processes and flags ones from `AppData` or with suspicious names like `log`, `winlog`, etc.
* Allows you to terminate unwanted or potentially harmful processes
* Enables saving results of the scan to a `.txt` file

---

## 📁 Project Structure

```
anti-keylogger-scanner/
│
├── images/
│   ├── scanner.png
│   └── process_scan.png                                  
├── README.md                       
├── anti_keylogger_gui.py          
├── requirements.txt         
└── setup.py                      
```

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more information.

---

## 👨‍💻 Author

**Chirag Khatri**
GitHub: [@CH-Anonymous](https://github.com/CH-Anonymous)

## ⭐ Star This Repo

If you find this project helpful or interesting, feel free to star it and share it!
