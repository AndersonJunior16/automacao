import pyautogui as pa
import time
import os

# Set a pause between actions to avoid overwhelming the system
pa.PAUSE = 2

# Function to locate and click an image
def locate_and_click(image_path, confidence=0.8):
    location = pa.locateCenterOnScreen(image_path, confidence=confidence)
    if location:
        pa.click(location.x, location.y)
        print(f'Clicked on {image_path} at ({location.x}, {location.y})')
    else:
        print(f'Could not find {image_path} on the screen')

# Path to the images
edge = 'edge.png'
teams = 'teams.png'

# Click on Edge icon
locate_and_click(edge)

# Click on Teams icon
locate_and_click(teams)
