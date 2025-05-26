import os
import psutil
import tkinter as tk
from tkinter import messagebox, ttk, filedialog

# Handle winreg only on Windows systems
try:
    import winreg
except ImportError:
    winreg = None  # For non-Windows systems or if not needed

def check_startup_entries():
    suspicious = []
    if not winreg:
        return suspicious
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
            "Software\\Microsoft\\Windows\\CurrentVersion\\Run")
        i = 0
        while True:
            try:
                name, path, _ = winreg.EnumValue(key, i)
                if "log" in name.lower() or "winlog" in path.lower():
                    suspicious.append((name, path))
                i += 1
            except OSError:
                break
        winreg.CloseKey(key)
    except Exception as e:
        print("Registry error:", e)
    return suspicious

def check_running_processes():
    flagged = []
    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        try:
            exe_path = proc.info['exe'] or ""
            name = proc.info['name'].lower()
            if "appdata" in exe_path.lower() or "log" in name or "keylog" in exe_path.lower():
                flagged.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return flagged

def scan():
    global suspicious_startup, suspicious_procs
    suspicious_startup = check_startup_entries()
    suspicious_procs = check_running_processes()

    startup_list.delete(*startup_list.get_children())
    proc_list.delete(*proc_list.get_children())

    for name, path in suspicious_startup:
        startup_list.insert("", "end", values=(name, path))

    for proc in suspicious_procs:
        proc_list.insert("", "end", values=(proc['pid'], proc['name'], proc['exe']))

def terminate_selected_process():
    selected = proc_list.selection()
    if not selected:
        messagebox.showinfo("No Selection", "Select a process to terminate.")
        return
    for item in selected:
        pid = proc_list.item(item)['values'][0]
        try:
            p = psutil.Process(pid)
            p.terminate()
            messagebox.showinfo("Terminated", f"Terminated PID: {pid}")
            proc_list.delete(item)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to terminate PID {pid}: {e}")

def save_results():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")])
    if not file_path:
        return

    try:
        with open(file_path, "w") as f:
            f.write("Suspicious Startup Entries:\n")
            for name, path in suspicious_startup:
                f.write(f"- {name}: {path}\n")
            f.write("\nSuspicious Running Processes:\n")
            for proc in suspicious_procs:
                f.write(f"- PID {proc['pid']}: {proc['name']} at {proc['exe']}\n")
        messagebox.showinfo("Saved", f"Results saved to {file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Could not save file: {e}")

# GUI Setup
root = tk.Tk()
root.title("Anti-Keylogger Scanner")

frame1 = ttk.LabelFrame(root, text="Suspicious Startup Entries")
frame1.pack(fill="both", expand=True, padx=10, pady=5)

startup_list = ttk.Treeview(frame1, columns=("Name", "Path"), show="headings")
startup_list.heading("Name", text="Name")
startup_list.heading("Path", text="Path")
startup_list.pack(fill="both", expand=True)

frame2 = ttk.LabelFrame(root, text="Suspicious Running Processes")
frame2.pack(fill="both", expand=True, padx=10, pady=5)

proc_list = ttk.Treeview(frame2, columns=("PID", "Name", "Path"), show="headings")
proc_list.heading("PID", text="PID")
proc_list.heading("Name", text="Name")
proc_list.heading("Path", text="Executable Path")
proc_list.pack(fill="both", expand=True)

button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

scan_btn = ttk.Button(button_frame, text="Scan System", command=scan)
scan_btn.grid(row=0, column=0, padx=5)

terminate_btn = ttk.Button(button_frame, text="Terminate Process", command=terminate_selected_process)
terminate_btn.grid(row=0, column=1, padx=5)

save_btn = ttk.Button(button_frame, text="Save Scan Results", command=save_results)
save_btn.grid(row=0, column=2, padx=5)

root.geometry("780x580")
root.mainloop()
