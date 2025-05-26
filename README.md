
# Anti-Keylogger Scanner Tool 🛡️

A lightweight Python-based GUI tool that scans for suspicious startup entries and running processes that may indicate keylogger activity.

## 💻 Features

- Scan Windows startup registry entries
- Detect suspicious running processes
- Terminate flagged processes
- Save scan results to a `.txt` file
- Simple, user-friendly Tkinter interface
- Packaged as a standalone `.exe`

## 📦 Built With

- Python 3.12
- Tkinter
- psutil
- winreg
- PyInstaller (for `.exe` packaging)

## 🚀 How to Run

### 🐍 Python Script

```bash
python anti_keylogger_gui.py
```

### 💾 Standalone `.exe`

Run the executable from the `dist/` folder:
```
anti_keylogger_gui.exe
```

No installation required.

## 🔧 Build Your Own .exe

```bash
pyinstaller --onefile --windowed --icon=icon.ico anti_keylogger_gui.py
```

## 📝 License

MIT License

---

> Created by Chirag Khatri 🙌
# anti-keylogger-scanner
"# anti-keylogger-scanner" 
