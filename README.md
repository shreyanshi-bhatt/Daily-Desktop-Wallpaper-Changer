# Daily-Desktop-Wallpaper-Changer ✨
Automate your desktop's ambiance with the Daily Desktop Wallpaper Changer. Enhance productivity and creativity by scheduling daily updates of stunning wallpapers from Wallhaven, tailored to your preferences. Customize paths easily and enjoy a fresh backdrop effortlessly. Elevate your desktop experience today!

# Installation 💻

1. **Set Up**:
   - Clone this repository to your local machine.
   - Install necessary Python dependencies (requests, beautifulsoup4, schedule, etc).

2. **Change Paths in `main.py`**:
   - Open `main.py` in a text editor.
   - Modify the `WALLPAPER_FOLDER` and `DEFAULT_IMAGE_PATH` variables to set your desired folder path for wallpapers and the fallback wallpaper respectively.

3. **Copy the Script Path (Local Path eg. C:\path\to\main.py)**:
   - Copy the local path of your (edited) main.py file to use it in the configuration phase in the next step.

4. **Set Up Task Scheduler**:
   - Use your operating system's task scheduler to automate the script execution.
   - Schedule the script to run daily at a specific time to update your desktop wallpaper automatically.
   - Here're the steps:
     
### 📂 Open Task Scheduler:

- Press Win + R to open the Run dialog.
- Type taskschd.msc and press Enter to open the Task Scheduler.
  
### ⭐ Create a New Task:

- In the Task Scheduler, go to Action > Create Task....
- Name your task (e.g., "Daily Wallpaper Changer").
- Optionally, provide a description for the task.
  
### 🔥 Configure Triggers:

- Go to the Triggers tab and click New....
- Choose how often you want the task to run (daily, weekly, etc.).
- Set the start time (e.g., daily at 5:00 AM).

### 🤖 Configure Actions:

- Go to the Actions tab and click New....
- Set the action to Start a program.
- Browse and select the Python executable (python.exe), and in the Add arguments field, enter the path to your script (C:\path\to\python.exe C:\path\to\main.py).

### 🛠 Set Conditions and Settings:

- Optionally, configure conditions under the Conditions tab (e.g., power settings, idle conditions).
- Review settings under the Settings tab and adjust as necessary.

### ✅ Save and Test:

- Click OK to save the task.
- Right-click on the task in the Task Scheduler and select Run to test if it executes correctly (change the time of wallpaper updation to current time for testing purpose).

### 👩🏻‍💻 Monitor and Debug: 

- Check the Last Run Result column in Task Scheduler to verify if the task ran successfully.
- Monitor the task initially to ensure it changes the wallpaper as expected and handles any errors appropriately.

# Output:
![image](https://github.com/shreyanshi-bhatt/Daily-Desktop-Wallpaper-Changer/assets/114408921/ddd380fd-4685-4f39-a106-d420a570d220)


# Voila! Please don't forget to star ⭐ the repo if it helped you. Thanks - SB 🙋🏻‍♀️
