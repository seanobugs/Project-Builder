# Project-Builder v1
A simple Python Tkinter application to quickly generate a standardized folder structure for video editing projects, ensuring organization and consistency. Allows specifying project name, output directory, prepending the current date, and the number of cameras used to create corresponding footage subfolders.

How to Use:

1.  **Run the application:** Execute the `folder_creator.py` (or the compiled `.exe` file).

2.  **Project Builder:** In the "Project Builder" field, enter the name you want to give to your video project (e.g., "ClientName\_ProjectTitle").

3.  **Output Directory:** Click the "Browse" button to select the main folder on your computer where you want the new project folder and its subdirectories to be created. The selected path will appear in the "Output Directory" field.

4.  **Prepend current date (DD-MM-YYYY):** This checkbox is checked by default. If you leave it checked, the current date (in the format DD-MM-YYYY) will be added to the beginning of your project folder name (e.g., "31-05-2025\_ClientName\_ProjectTitle"). You can uncheck this if you don't want the date prepended.

5.  **Number of Cameras:** Use the dropdown menu to select the number of cameras used in the project (from 1 to 4). This will automatically create the corresponding number of "Camera A", "Camera B", etc., folders within the "01\_Footage" directory.

6.  **Create Structure:** Once you have entered the project name, selected the output directory, and chosen the number of cameras, click the "Create Structure" button.

7.  **Status:** A message will appear at the bottom of the application to inform you whether the folder structure was created successfully or if any errors occurred.

Folder Structure Created:

When you click "Create Structure", the application will generate the following folder structure within your chosen output directory, under a folder named after your project:

![image](https://github.com/user-attachments/assets/4ecd0b92-ed86-436b-ad42-e2d7a25bc4e7)

