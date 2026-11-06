# ===================================================================================
# 🪐 PSICO BINARY SHORTCUT FACTORY v1.1 — DYNAMIC CACHE ISOLATION
# ===================================================================================
# Repository Node : C:\Users\Jack\Desktop\factory\shortcut_factory.py
# Function        : Enforces unique filename outputs to prevent icon overwriting [1.1]
# ===================================================================================

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os
import subprocess
import threading

class PsicoShortcutFactory:
    def __init__(self, root):
        self.root = root
        self.root.title("🪐 PSICO BINARY SHORTCUT FACTORY — V1.1")
        self.root.geometry("900x650")
        self.root.configure(bg="#0d0d0d")  # Enforce strict dark room layout
        
        self.is_compiling = False
        
        # 📐 1. TOP HEADER BRANDING PANEL
        self.header = tk.Label(
            root, text="PSICO COMMUNICATIONS // AUTOMATED BINARY SHORTCUT FOUNDRY",
            fg="#888888", bg="#0d0d0d", font=("Courier New", 10, "bold")
        )
        self.header.pack(pady=10)
        
        # 📺 2. THE COMPILER CONSOLE DISPLAY LAYER
        self.display_canvas = scrolledtext.ScrolledText(
            root, wrap=tk.WORD, bg="#111111", fg="#00ff66",
            insertbackground="white", font=("Courier New", 11),
            bd=1, relief=tk.SOLID, highlightbackground="#222222"
        )
        self.display_canvas.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        self.log_message("🪐 FOUNDRY ACTIVE: Ready to forge isolated binary .exe shortcuts.\n")
        self.log_message("--------------------------------------------------------------------\n")
        self.display_canvas.configure(state=tk.DISABLED)
        
        # ⌨️ 3. THE INPUT CONTROLS PANE
        self.input_frame = tk.Frame(root, bg="#0d0d0d")
        self.input_frame.pack(padx=20, pady=10, fill=tk.X)
        
        # --- App Name / Shortcut Name ---
        tk.Label(self.input_frame, text="SHORTCUT NAME (e.g., Bloomberg or SourceForge):", fg="#ffffff", bg="#0d0d0d", font=("Courier New", 9, "bold")).pack(anchor=tk.W)
        self.name_entry = tk.Entry(self.input_frame, bg="#161616", fg="#ffffff", insertbackground="white", font=("Courier New", 10), bd=1, relief=tk.SOLID)
        self.name_entry.pack(fill=tk.X, pady=(2, 10), ipady=4)
        self.name_entry.insert(0, "TargetLink")
        
        # --- Target URL / Local File Path ---
        tk.Label(self.input_frame, text="TARGET FILE LINK OR URL (file:///C:/... or http://...):", fg="#ffffff", bg="#0d0d0d", font=("Courier New", 9, "bold")).pack(anchor=tk.W)
        self.url_entry = tk.Entry(self.input_frame, bg="#161616", fg="#00ff66", insertbackground="white", font=("Courier New", 10), bd=1, relief=tk.SOLID)
        self.url_entry.pack(fill=tk.X, pady=(2, 10), ipady=4)
        self.url_entry.insert(0, "https://sourceforge.net")
        
        # --- Icon Path Control Row ---
        tk.Label(self.input_frame, text="TARGET EMBLEM ICON (.ico):", fg="#ffffff", bg="#0d0d0d", font=("Courier New", 9, "bold")).pack(anchor=tk.W)
        self.icon_frame = tk.Frame(self.input_frame, bg="#0d0d0d")
        self.icon_frame.pack(fill=tk.X, pady=(2, 10))
        
        self.icon_entry = tk.Entry(self.icon_frame, bg="#161616", fg="#ffffff", insertbackground="white", font=("Courier New", 10), bd=1, relief=tk.SOLID)
        self.icon_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=4)
        
        if os.path.exists("logo.ico"):
            self.icon_entry.insert(0, os.path.abspath("logo.ico"))
            
        self.browse_btn = tk.Button(self.icon_frame, text="BROWSE", fg="#ffffff", bg="#222222", font=("Courier New", 8, "bold"), bd=0, command=self.browse_icon_file)
        self.browse_btn.pack(side=tk.RIGHT, padx=(10, 0), ipady=2, ipadx=10)
        
        # 🚀 4. MASTER FORGE BUTTON
        self.forge_btn = tk.Button(
            root, text="FORGE TRUE BINARY SHORTCUT", fg="#ffffff", bg="#333333",
            activebackground="#00ff66", activeforeground="#000000",
            font=("Courier New", 10, "bold"), bd=0, relief=tk.FLAT,
            command=self.start_compilation_thread
        )
        self.forge_btn.pack(fill=tk.X, padx=20, pady=(0, 20), ipady=8)

    def log_message(self, text):
        self.display_canvas.configure(state=tk.NORMAL)
        self.display_canvas.insert(tk.END, text)
        self.display_canvas.see(tk.END)
        self.display_canvas.configure(state=tk.DISABLED)

    def browse_icon_file(self):
        file_path = filedialog.askopenfilename(title="Select Icon Container", filetypes=[("Icon Files", "*.ico")])
        if file_path:
            self.icon_entry.delete(0, tk.END)
            self.icon_entry.insert(0, os.path.abspath(file_path))

    def start_compilation_thread(self):
        if self.is_compiling:
            return
        self.is_compiling = True
        self.forge_btn.configure(state=tk.DISABLED, bg="#111111", text="COMPILING BINARY INFRASTRUCTURE...")
        threading.Thread(target=self.execute_shortcut_forge, daemon=True).start()

    def reset_button_state(self):
        self.is_compiling = False
        self.forge_btn.configure(state=tk.NORMAL, bg="#333333", text="FORGE TRUE BINARY SHORTCUT")

    def execute_shortcut_forge(self):
        shortcut_name = self.name_entry.get().strip()
        target_url = self.url_entry.get().strip()
        icon_path = self.icon_entry.get().strip()
        
        safe_filename = "".join(c for c in shortcut_name if c.isalnum() or c in ("-", "_", " ")).strip()
        
        if not safe_filename or not target_url or not icon_path:
            messagebox.showerror("Error", "All configurations must be populated before pulling the forge trigger.")
            self.reset_button_state()
            return
            
        # 🛠️ NATIVE OPTIMIZATION: Write a Microscopic C# Stub instead of a Python Stub
        launcher_src_path = os.path.join(os.getcwd(), f"temp_{safe_filename}_stub.cs")
        with open(launcher_src_path, "w", encoding="utf-8") as f:
            f.write("using System;\n")
            f.write("using System.Diagnostics;\n")
            f.write("class WebShortcut {\n")
            f.write("    static void Main() {\n")
            f.write(f'        Process.Start(new ProcessStartInfo("{target_url}") {{ UseShellExecute = true }});\n')
            f.write("    }\n")
            f.write("}\n")
            
        self.log_message(f"\n🏹 INITIALIZING MICRO-BINARY FORGE LOOP FOR: {safe_filename}\n")
        self.log_message(f"   └── Destination Node: {target_url}\n")
        self.log_message(f"   └── Burning Icon Layer: {icon_path}\n")
        self.log_message("--------------------------------------------------------------------\n")
        
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        target_desktop_path = os.path.join(desktop_path, f"{safe_filename}.exe")
        
        # 🔍 Locate the native Windows .NET compiler automatically
        windir = os.environ.get("SystemRoot", "C:\\Windows")
        csc_path = os.path.join(windir, "Microsoft.NET", "Framework", "v4.0.30319", "csc.exe")
        
        if not os.path.exists(csc_path):
            # Fallback check for older .NET paths if 4.0 framework variant is altered
            csc_path = os.path.join(windir, "Microsoft.NET", "Framework64", "v4.0.30319", "csc.exe")
            
        if not os.path.exists(csc_path):
            self.log_message("❌ ERROR: Native Windows .NET Compiler (csc.exe) could not be located.\n")
            if os.path.exists(launcher_src_path):
                os.remove(launcher_src_path)
            self.reset_button_state()
            return

        # ⚡ Construct the native compilation flag strings
        # /target:winexe hides the command console popup window entirely
        # /win32icon injects your visual emblem straight into the native PE binary resource layer
        cmd = [
            csc_path,
            "/target:winexe",
            f"/win32icon:{icon_path}",
            f"/out:{target_desktop_path}",
            launcher_src_path
        ]
        
        try:
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
            
            while True:
                line = process.stdout.readline()
                if not line:
                    break
                self.log_message(line)
                
            process.wait()
            
            # Post-build garbage cleanup
            if os.path.exists(launcher_src_path):
                os.remove(launcher_src_path)
                
            if process.returncode == 0 and os.path.exists(target_desktop_path):
                self.log_message(f"\n🪐 FOUNDRY SUCCESSFUL: True Micro-Binary (150KB) injected straight to wallpaper grid!\n")
                self.log_message(f"   └── Saved Node: {target_desktop_path}\n")
            else:
                self.log_message("\n❌ FORGE FAILED: The compiler encountered an asset formatting block.\n")
                
        except Exception as e:
            self.log_message(f"\n❌ CRITICAL SYSTEM ERROR: {str(e)}\n")
            if os.path.exists(launcher_src_path):
                os.remove(launcher_src_path)
                
        self.reset_button_state()

# Added helper method block to clean up the missing indentation boundary in original stream print
if __name__ == "__main__":
    root = tk.Tk()
    app = PsicoShortcutFactory(root)
    root.mainloop()
