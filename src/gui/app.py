import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime

from src.core.utilities import get_resource_path

class TkinterPoetryStarter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tkinter Poetry Starter")
        self.root.minsize(400, 300)
        
        self.setup_window_icon()
        self.setup_styles()
        self.setup_ui()
        

    def setup_window_icon(self):
        logo_path = get_resource_path(os.path.join("src", "assets", "logo.png"))
        if os.path.exists(logo_path):
            try:
                icon = Image.open(logo_path)
                icon = icon.resize((32, 32), Image.Resampling.LANCZOS)
                icon_photo = ImageTk.PhotoImage(icon)
                self.root.iconphoto(True, icon_photo)
            except Exception as e:
                print(f"Could not set window icon: {str(e)}")

    def setup_styles(self):
        style = ttk.Style()
        style.configure("MainFrame.TFrame", background="#ffffff")
        
        style.configure(
            "Time.TLabel",
            font=("Helvetica", 72, "bold"),
            background="#ffffff",
            foreground="#2c3e50"
        )
        
        style.configure(
            "Date.TLabel",
            font=("Helvetica", 24),
            background="#ffffff",
            foreground="#34495e"
        )

    def setup_ui(self):
        # Create main frame with padding and style
        self.main_frame = ttk.Frame(self.root, padding="40", style="MainFrame.TFrame")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configure grid weights for responsive layout
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        
        # Create time display
        self.time_label = ttk.Label(
            self.main_frame,
            style="Time.TLabel"
        )
        self.time_label.grid(row=0, column=0, pady=(0, 10))
        
        # Create date display
        self.date_label = ttk.Label(
            self.main_frame,
            style="Date.TLabel"
        )
        self.date_label.grid(row=1, column=0)

        self.update_time()

    def update_time(self):
        # Get current time and date
        current = datetime.now()
        time_string = current.strftime("%H:%M:%S")
        date_string = current.strftime("%B %d, %Y")
        
        # Update labels
        self.time_label.config(text=time_string)
        self.date_label.config(text=date_string)
        
        # Schedule next update
        self.root.after(1000, self.update_time)

    def mainloop(self):
        self.root.mainloop()


def main():
    app = TkinterPoetryStarter()
    app.mainloop()


if __name__ == "__main__":
    main()
