
#!/usr/bin/env python3
"""
Webease GUI Compiler - Graphical interface for compiling .ws files
"""

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
import webbrowser
import os
from pathlib import Path
import sys

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from src.webease.compiler import WebeaseCompiler


class WebeaseGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Webease Compiler")
        self.root.geometry("800x600")
        self.root.minsize(600, 400)
        
        # Variables
        self.input_file = tk.StringVar()
        self.output_dir = tk.StringVar(value="output")
        self.auto_open = tk.BooleanVar(value=True)
        
        # Create UI
        self.create_widgets()
        
        # Compiler instance
        self.compiler = WebeaseCompiler()
    
    def create_widgets(self):
        # Header
        header = tk.Frame(self.root, bg="#667eea", height=80)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        title = tk.Label(
            header, 
            text="🌐 Webease Compiler", 
            font=("Arial", 24, "bold"),
            bg="#667eea",
            fg="white"
        )
        title.pack(pady=20)
        
        # Main content
        content = tk.Frame(self.root, padx=20, pady=20)
        content.pack(fill=tk.BOTH, expand=True)
        
        # Input file selection
        input_frame = tk.Frame(content)
        input_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(input_frame, text="Input File (.ws):", font=("Arial", 10)).pack(anchor=tk.W)
        
        file_select = tk.Frame(input_frame)
        file_select.pack(fill=tk.X, pady=(5, 0))
        
        tk.Entry(file_select, textvariable=self.input_file, font=("Arial", 10)).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        tk.Button(file_select, text="Browse", command=self.browse_input, bg="#667eea", fg="white", font=("Arial", 10)).pack(side=tk.RIGHT)
        
        # Output directory
        output_frame = tk.Frame(content)
        output_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(output_frame, text="Output Directory:", font=("Arial", 10)).pack(anchor=tk.W)
        
        dir_select = tk.Frame(output_frame)
        dir_select.pack(fill=tk.X, pady=(5, 0))
        
        tk.Entry(dir_select, textvariable=self.output_dir, font=("Arial", 10)).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        tk.Button(dir_select, text="Browse", command=self.browse_output, bg="#667eea", fg="white", font=("Arial", 10)).pack(side=tk.RIGHT)
        
        # Options
        options_frame = tk.Frame(content)
        options_frame.pack(fill=tk.X, pady=(0, 15))
        
        tk.Checkbutton(
            options_frame, 
            text="Open in browser after compiling", 
            variable=self.auto_open,
            font=("Arial", 10)
        ).pack(anchor=tk.W)
        
        # Compile button
        tk.Button(
            content,
            text="🔨 Compile",
            command=self.compile_file,
            bg="#667eea",
            fg="white",
            font=("Arial", 14, "bold"),
            height=2,
            cursor="hand2"
        ).pack(fill=tk.X, pady=(0, 15))
        
        # Output log
        tk.Label(content, text="Compilation Log:", font=("Arial", 10, "bold")).pack(anchor=tk.W)
        
        self.log_text = scrolledtext.ScrolledText(
            content,
            height=12,
            font=("Consolas", 9),
            bg="#f5f5f5",
            wrap=tk.WORD
        )
        self.log_text.pack(fill=tk.BOTH, expand=True, pady=(5, 0))
        
        # Status bar
        self.status_bar = tk.Label(
            self.root,
            text="Ready",
            relief=tk.SUNKEN,
            anchor=tk.W,
            font=("Arial", 9)
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def browse_input(self):
        filename = filedialog.askopenfilename(
            title="Select Webease File",
            filetypes=[("Webease Files", "*.ws"), ("All Files", "*.*")]
        )
        if filename:
            self.input_file.set(filename)
    
    def browse_output(self):
        dirname = filedialog.askdirectory(
            title="Select Output Directory"
        )
        if dirname:
            self.output_dir.set(dirname)
    
    def log(self, message, level="INFO"):
        colors = {
            "INFO": "black",
            "SUCCESS": "green",
            "ERROR": "red",
            "WARNING": "orange"
        }
        
        self.log_text.insert(tk.END, f"{message}\n")
        self.log_text.see(tk.END)
        self.root.update()
    
    def compile_file(self):
        input_path = self.input_file.get()
        
        if not input_path:
            messagebox.showerror("Error", "Please select an input file!")
            return
        
        if not os.path.exists(input_path):
            messagebox.showerror("Error", f"File not found: {input_path}")
            return
        
        # Clear log
        self.log_text.delete(1.0, tk.END)
        
        # Update status
        self.status_bar.config(text="Compiling...")
        self.log(f"🔨 Compiling {input_path}...")
        
        try:
            # Compile
            html, error = self.compiler.compile_file(input_path)
            
            if error:
                self.log(f"\n❌ Compilation Failed!\n", "ERROR")
                self.log(error, "ERROR")
                self.status_bar.config(text="Compilation failed")
                messagebox.showerror("Compilation Error", "See log for details")
                return
            
            # Create output directory
            output_dir = Path(self.output_dir.get())
            output_dir.mkdir(exist_ok=True)
            
            # Generate output filename
            input_path_obj = Path(input_path)
            output_filename = input_path_obj.stem + '.html'
            output_path = output_dir / output_filename
            
            # Write HTML
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(html)
            
            self.log(f"\n✅ Successfully compiled!", "SUCCESS")
            self.log(f"📄 Output: {output_path}", "SUCCESS")
            
            # Open in browser if requested
            if self.auto_open.get():
                self.log(f"🚀 Opening in browser...", "INFO")
                webbrowser.open(f'file://{output_path.absolute()}')
            
            self.status_bar.config(text=f"Successfully compiled to {output_path}")
            messagebox.showinfo("Success", f"Compiled successfully!\n\nOutput: {output_path}")
            
        except Exception as e:
            self.log(f"\n❌ Unexpected Error!\n", "ERROR")
            self.log(str(e), "ERROR")
            self.status_bar.config(text="Error occurred")
            messagebox.showerror("Error", f"An error occurred:\n{str(e)}")


def main():
    root = tk.Tk()
    app = WebeaseGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
