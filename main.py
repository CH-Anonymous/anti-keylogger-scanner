import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from utils import (
    push_to_github, create_github_repo, load_token, save_token,
    reset_token, delete_github_repo, list_github_repos, update_repo_remote
)

BG_COLOR = "#1e1e2f"
FG_COLOR = "#ffffff"
BTN_COLOR = "#4caf50"
RESET_COLOR = "#e53935"
ENTRY_BG = "#2e2e3e"
FONT = ("Segoe UI", 10)

root = tk.Tk()
root.title("AutoGitPush Extended")
root.geometry("600x500")
root.configure(bg=BG_COLOR)

folder_selected = tk.StringVar()
repo_name_var = tk.StringVar()
progress = None

def browse_folder():
    folder_selected.set(filedialog.askdirectory())

def push_code():
    folder = folder_selected.get()
    repo = repo_name_var.get()
    username, token = load_token()
    if not all([username, token, repo, folder]):
        messagebox.showerror("Error", "Missing required information.")
        return

    progress.start()
    root.update_idletasks()

    repo_created, repo_msg = create_github_repo(repo, username, token)
    if repo_created:
        messagebox.showinfo("Repository Created", repo_msg)
    else:
        messagebox.showwarning("Repository Info", repo_msg)

    success, push_msg = push_to_github(folder, username, repo, token)
    progress.stop()
    if success:
        messagebox.showinfo("Push Success", push_msg)
    else:
        messagebox.showerror("Push Failed", push_msg)

def first_time_setup():
    def save_and_continue():
        u = entry_username.get()
        t = entry_token.get()
        if not u or not t:
            messagebox.showerror("Error", "Please enter both username and token.")
            return
        save_token(u, t)
        popup.destroy()
        root.deiconify()
        load_repo_dropdown()

    popup = tk.Toplevel(bg=BG_COLOR)
    popup.title("GitHub Login Setup")
    popup.geometry("400x220")
    popup.configure(bg=BG_COLOR)

    tk.Label(popup, text="GitHub Username", bg=BG_COLOR, fg=FG_COLOR, font=FONT).pack(pady=(10, 0))
    entry_username = tk.Entry(popup, width=40, bg=ENTRY_BG, fg=FG_COLOR, insertbackground=FG_COLOR)
    entry_username.pack(pady=5)

    tk.Label(popup, text="GitHub Token", bg=BG_COLOR, fg=FG_COLOR, font=FONT).pack(pady=(10, 0))
    entry_token = tk.Entry(popup, width=40, show="*", bg=ENTRY_BG, fg=FG_COLOR, insertbackground=FG_COLOR)
    entry_token.pack(pady=5)

    tk.Button(popup, text="Save & Continue", command=save_and_continue, bg=BTN_COLOR, fg="white").pack(pady=15)
    root.withdraw()

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Push Tab
push_frame = tk.Frame(notebook, bg=BG_COLOR)
notebook.add(push_frame, text="Push Code")

tk.Label(push_frame, text="📁 Select Folder", bg=BG_COLOR, fg=FG_COLOR, font=FONT).pack(pady=(20, 5))
tk.Entry(push_frame, textvariable=folder_selected, width=50, bg=ENTRY_BG, fg=FG_COLOR, insertbackground=FG_COLOR).pack()
tk.Button(push_frame, text="Browse", command=browse_folder, bg=BTN_COLOR, fg="white").pack(pady=10)

tk.Label(push_frame, text="📦 Repository Name", bg=BG_COLOR, fg=FG_COLOR, font=FONT).pack(pady=(10, 5))
tk.Entry(push_frame, textvariable=repo_name_var, width=50, bg=ENTRY_BG, fg=FG_COLOR, insertbackground=FG_COLOR).pack()

tk.Button(push_frame, text="🚀 Push to GitHub", command=push_code, bg=BTN_COLOR, fg="white", height=2).pack(pady=20)

progress = ttk.Progressbar(push_frame, mode='indeterminate')
progress.pack(pady=5, fill="x", padx=50)

# Delete Repo Tab
repo_frame = tk.Frame(notebook, bg=BG_COLOR)
notebook.add(repo_frame, text="Delete Repo")

repo_listbox = tk.Listbox(repo_frame, width=50, height=10)
repo_listbox.pack(pady=10)

def refresh_repos():
    repo_listbox.delete(0, tk.END)
    _, token = load_token()
    if not token:
        return
    repos = list_github_repos(token)
    for r in repos:
        repo_listbox.insert(tk.END, r)

def delete_selected_repo():
    selected = repo_listbox.get(tk.ACTIVE)
    if selected and messagebox.askyesno("Confirm", f"Delete GitHub repo '{selected}'?"):
        _, token = load_token()
        delete_github_repo(selected, token)
        refresh_repos()

tk.Button(repo_frame, text="🔃 Refresh List", command=refresh_repos, bg=BTN_COLOR, fg="white").pack(pady=5)
tk.Button(repo_frame, text="🗑️ Delete Selected Repo", command=delete_selected_repo, bg=RESET_COLOR, fg="white").pack(pady=5)

# Upload/Replace Files Tab
update_frame = tk.Frame(notebook, bg=BG_COLOR)
notebook.add(update_frame, text="Update Repo Files")

update_repo_var = tk.StringVar()
update_folder_var = tk.StringVar()

tk.Label(update_frame, text="Select Repository", bg=BG_COLOR, fg=FG_COLOR, font=FONT).pack(pady=(10, 0))
update_repo_dropdown = ttk.Combobox(update_frame, textvariable=update_repo_var, width=40)
update_repo_dropdown.pack(pady=5)

def load_repo_dropdown():
    _, token = load_token()
    if not token:
        return
    repos = list_github_repos(token)
    update_repo_dropdown['values'] = repos
    if repos:
        update_repo_var.set(repos[0])

tk.Button(update_frame, text="🔃 Refresh Repo List", command=load_repo_dropdown, bg=BTN_COLOR, fg="white").pack()

tk.Label(update_frame, text="Select Local Repo Folder", bg=BG_COLOR, fg=FG_COLOR, font=FONT).pack(pady=(10, 0))
tk.Entry(update_frame, textvariable=update_folder_var, width=50, bg=ENTRY_BG, fg=FG_COLOR, insertbackground=FG_COLOR).pack()
tk.Button(update_frame, text="Browse", command=lambda: update_folder_var.set(filedialog.askdirectory()), bg=BTN_COLOR, fg="white").pack(pady=5)

def upload_or_replace_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    folder = update_folder_var.get()
    if not folder:
        messagebox.showerror("Error", "Please select a local folder.")
        return
    dest_path = os.path.join(folder, os.path.basename(file_path))
    try:
        with open(file_path, 'rb') as src, open(dest_path, 'wb') as dst:
            dst.write(src.read())
        messagebox.showinfo("Success", f"Uploaded/Replaced {os.path.basename(file_path)}")

        username, token = load_token()
        repo = update_repo_var.get()
        if not all([username, token, repo]):
            return
        success, msg = push_to_github(folder, username, repo, token)
        if success:
            messagebox.showinfo("Push Success", msg)
        else:
            messagebox.showerror("Push Failed", msg)

    except Exception as e:
        messagebox.showerror("Error", f"Failed: {str(e)}")

tk.Button(update_frame, text="📤 Upload or Replace File", command=upload_or_replace_file, bg=BTN_COLOR, fg="white").pack(pady=10)

def push_all_changes():
    folder = update_folder_var.get()
    repo = update_repo_var.get()
    if not all([folder, repo]):
        messagebox.showerror("Error", "Please select both folder and repository.")
        return
    username, token = load_token()
    if not all([username, token]):
        messagebox.showerror("Error", "Missing GitHub credentials.")
        return
    success, msg = push_to_github(folder, username, repo, token)
    if success:
        messagebox.showinfo("Push Success", msg)
    else:
        messagebox.showerror("Push Failed", msg)

tk.Button(update_frame, text="🚀 Push All Changes", command=push_all_changes, bg=BTN_COLOR, fg="white").pack(pady=10)

# Settings Tab
settings_frame = tk.Frame(notebook, bg=BG_COLOR)
notebook.add(settings_frame, text="Settings")

tk.Button(settings_frame, text="🔁 Reset GitHub Credentials",
          command=lambda: (reset_token(), messagebox.showinfo("Reset", "Credentials cleared. Restart the app.")),
          bg=RESET_COLOR, fg="white").pack(pady=30)

if not load_token()[0]:
    root.after(100, first_time_setup)

root.after(300, load_repo_dropdown)

root.mainloop()
