import tkinter as tk
from tkinter import filedialog, messagebox, PhotoImage
import os
from datetime import datetime

class VideoFolderCreatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Project Builder")
        master.geometry("500x380")  # Increased height for the dropdown
        master.resizable(False, False)

        # --- Set Application Icon ---
        try:
            self.icon_image = PhotoImage(file='app_icon.png')
            master.iconphoto(False, self.icon_image)
        except tk.TclError:
            try:
                master.iconbitmap('app_icon.ico')
            except tk.TclError:
                print("Warning: Could not load application icon.")

        # --- Dark Mode Colors ---
        self.bg_color = "#2b2b2b"
        self.fg_color = "#cccccc"
        self.entry_bg_color = "#3c3c3c"
        self.button_bg_color = "#4a4a4a"
        self.button_active_bg_color = "#5a5a5a"

        master.configure(bg=self.bg_color)

        master.grid_rowconfigure(0, weight=1)
        master.grid_rowconfigure(1, weight=1)
        master.grid_rowconfigure(2, weight=1)
        master.grid_rowconfigure(3, weight=1)
        master.grid_rowconfigure(4, weight=1)
        master.grid_rowconfigure(5, weight=1)
        master.grid_rowconfigure(6, weight=1) # New row for camera count
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=3)
        master.grid_columnconfigure(2, weight=1)

        # --- Widgets ---

        # Project Name
        self.project_name_label = tk.Label(master, text="Project Builder:", bg=self.bg_color, fg=self.fg_color)
        self.project_name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.project_name_entry = tk.Entry(master, width=40, bg=self.entry_bg_color, fg=self.fg_color, insertbackground=self.fg_color)
        self.project_name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.project_name_entry.focus_set()

        # Output Directory
        self.output_dir_label = tk.Label(master, text="Output Directory:", bg=self.bg_color, fg=self.fg_color)
        self.output_dir_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.output_dir_entry = tk.Entry(master, width=40, bg=self.entry_bg_color, fg=self.fg_color, insertbackground=self.fg_color)
        self.output_dir_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        self.browse_button = tk.Button(master, text="Browse", command=self.browse_directory,
                                       bg=self.button_bg_color, fg=self.fg_color,
                                       activebackground=self.button_active_bg_color, activeforeground=self.fg_color,
                                       relief=tk.FLAT, bd=0)
        self.browse_button.grid(row=1, column=2, padx=10, pady=10, sticky="e")

        # Add Date Checkbox
        self.add_date_var = tk.BooleanVar(value=True)
        self.add_date_checkbox = tk.Checkbutton(master, text="Prepend current date (DD-MM-YYYY)", variable=self.add_date_var,
                                                bg=self.bg_color, fg=self.fg_color,
                                                selectcolor=self.entry_bg_color,
                                                activebackground=self.bg_color, activeforeground=self.fg_color)
        self.add_date_checkbox.grid(row=2, column=0, columnspan=3, padx=10, pady=5, sticky="w")

        # Number of Cameras Dropdown
        self.num_cameras_label = tk.Label(master, text="Number of Cameras:", bg=self.bg_color, fg=self.fg_color)
        self.num_cameras_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.num_cameras = tk.StringVar(master)
        self.num_cameras.set("1")  # Default value
        self.camera_options = ["1", "2", "3", "4"]
        self.camera_dropdown = tk.OptionMenu(master, self.num_cameras, *self.camera_options)
        self.camera_dropdown.config(bg=self.entry_bg_color, fg=self.fg_color, highlightthickness=0)
        self.camera_dropdown_menu = master.nametowidget(self.camera_dropdown.menuname)
        self.camera_dropdown_menu.config(bg=self.entry_bg_color, fg=self.fg_color)
        self.camera_dropdown.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

        # Create Structure Button
        self.create_button = tk.Button(master, text="Create Structure", command=self.create_folder_structure,
                                       bg="#ffc600", fg="black",
                                       activebackground="#e6b300", activeforeground="black",
                                       relief=tk.FLAT, bd=0, font=('Arial', 10, 'bold'))
        self.create_button.grid(row=4, column=0, columnspan=3, pady=10)

        # Status Label
        self.status_label = tk.Label(master, text="", fg="lightgreen", bg=self.bg_color)
        self.status_label.grid(row=5, column=0, columnspan=3, pady=10)

        # Define the base folder structure
        self.base_folder_structure = [
            "01_Footage",
            "01_Footage/Audio",
            "01_Footage/Screen Recordings",
            "01_Footage/Other Footage",
            "02_Project_Files",
            "02_Project_Files/Premiere Pro",
            "02_Project_Files/After Effects",
            "02_Project_Files/Other Project Files",
            "03_Assets",
            "03_Assets/Graphics",
            "03_Assets/Music",
            "03_Assets/Sound Effects",
            "03_Assets/Fonts",
            "03_Assets/Stock Footage",
            "04_Exports",
            "04_Exports/WIP",
            "04_Exports/Final",
            "05_Archive"
        ]

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.output_dir_entry.delete(0, tk.END)
            self.output_dir_entry.insert(0, directory)

    def create_folder_structure(self):
        project_name = self.project_name_entry.get().strip()
        output_base_dir = self.output_dir_entry.get().strip()
        num_cameras = int(self.num_cameras.get())

        if not project_name:
            self.status_label.config(text="Please enter a Project Name.", fg="red")
            return

        if not output_base_dir:
            self.status_label.config(text="Please select an Output Directory.", fg="red")
            return

        if self.add_date_var.get():
            current_date = datetime.now().strftime("%d-%m-%Y")
            project_name = f"{current_date}_{project_name}"

        project_path = os.path.join(output_base_dir, project_name)

        if os.path.exists(project_path):
            response = messagebox.askyesno(
                "Folder Exists",
                f"The folder '{project_name}' already exists in the selected directory.\n"
                "Do you want to proceed and potentially add missing subfolders?"
            )
            if not response:
                self.status_label.config(text="Operation cancelled.", fg="orange")
                return

        try:
            os.makedirs(project_path, exist_ok=True)
            self.status_label.config(text=f"Creating folders for '{project_name}'...", fg="lightgreen")
            self.master.update_idletasks()

            # Create camera folders
            for i in range(num_cameras):
                camera_folder = f"01_Footage/Camera {chr(ord('A') + i)}"
                path_to_create = os.path.join(project_path, camera_folder)
                os.makedirs(path_to_create, exist_ok=True)

            # Create the other folders under Footage
            footage_others = ["Audio", "Screen Recordings", "Other Footage"]
            for folder in footage_others:
                path_to_create = os.path.join(project_path, "01_Footage", folder)
                os.makedirs(path_to_create, exist_ok=True)

            # Create the rest of the base folders
            for folder in self.base_folder_structure:
                if not folder == "01_Footage": # Avoid trying to create the base Footage folder again
                    path_to_create = os.path.join(project_path, folder)
                    os.makedirs(path_to_create, exist_ok=True)

            self.status_label.config(text=f"Folder structure for '{project_name}' created successfully!", fg="lightgreen")

        except OSError as e:
            self.status_label.config(text=f"Error creating folders: {e}", fg="red")
        except Exception as e:
            self.status_label.config(text=f"An unexpected error occurred: {e}", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoFolderCreatorApp(root)
    root.mainloop()