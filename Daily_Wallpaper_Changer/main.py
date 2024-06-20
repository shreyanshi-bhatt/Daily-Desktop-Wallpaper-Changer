import requests
import ctypes
import schedule
import time
import random
import os
from datetime import datetime
from bs4 import BeautifulSoup

# Path to save the wallpapers and the default image (Default image is the fallback image)
WALLPAPER_FOLDER = r"C:\Users\India\OneDrive\Desktop\PythonProjects\Daily_Wallpaper_Changer\Wallpapers"
DEFAULT_IMAGE_PATH = r"C:\Users\India\OneDrive\Desktop\PythonProjects\Daily_Wallpaper_Changer\wallhaven-8586my_1920x1080.png"


# Function to download the wallpaper
def download_wallpaper(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        return True
    return False


# Function to set the wallpaper (Windows)
def set_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)


# Function to get the top wallpaper URL
def get_top_wallpaper_url():
    url = "https://wallhaven.cc/search?categories=100&purity=100&resolutions=1920x1080&sorting=date_added&order=desc&ai_art_filter=1&page=1"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the top 10 images
    thumbnails = soup.select('li > figure > a.preview')[:10]
    if not thumbnails:
        return None

    # Choose a random thumbnail and get the corresponding page URL
    random_thumbnail = random.choice(thumbnails)
    image_page_url = random_thumbnail['href']

    # Visit the image page to get the direct image URL
    image_page_response = requests.get(image_page_url)
    image_page_soup = BeautifulSoup(image_page_response.content, 'html.parser')
    image_url = image_page_soup.select_one('img#wallpaper')['src']

    return image_url


# Function to delete old wallpapers (This enhances storage efficiency)
def delete_old_wallpapers(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")


# Main function to download and set the wallpaper
def update_wallpaper():
    try:
        # Delete old wallpapers
        delete_old_wallpapers(WALLPAPER_FOLDER)

        # Get the new wallpaper URL
        top_wallpaper_url = get_top_wallpaper_url()
        current_date = datetime.now().strftime("%Y-%m-%d")
        wallpaper_path = os.path.join(WALLPAPER_FOLDER, f"wallpaper_{current_date}.jpg")

        if top_wallpaper_url:
            # Download and set the new wallpaper
            if download_wallpaper(top_wallpaper_url, wallpaper_path):
                set_wallpaper(wallpaper_path)
                print(f"Wallpaper updated successfully: {wallpaper_path}")
                return True  # Return True indicating successful wallpaper update
            else:
                # Use the default wallpaper
                set_wallpaper(DEFAULT_IMAGE_PATH)
                print("Failed to download the new wallpaper. Default wallpaper set.")
        else:
            # Use the default wallpaper
            set_wallpaper(DEFAULT_IMAGE_PATH)
            print("No thumbnails found. Default wallpaper set.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return False  # Return False indicating wallpaper update failure


# Schedule the wallpaper update for 1 minute from the current time for testing --- Done
# now = datetime.now()
# test_time = (now + timedelta(minutes=1)).strftime("%H:%M")
# schedule.every().day.at(test_time).do(update_wallpaper)

# For refreshing the wallpaper every day at 5 am
schedule.every().day.at("05:00").do(update_wallpaper)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
    if schedule.jobs[0].last_run and schedule.jobs[0].last_run.date() == datetime.today().date():
        break
