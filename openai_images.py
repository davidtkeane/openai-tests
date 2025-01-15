#!/usr/bin/env python3

# Created by Ranger 😎

# Import the required modules
import os
from openai import OpenAI
import requests
from datetime import datetime
from PIL import Image
import io

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def clear_screen():
    os.system('clear')

def save_image(url, prefix):
    """Save image from URL with timestamp"""
    try:
        response = requests.get(url)
        img = Image.open(io.BytesIO(response.content))
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"images/{prefix}_{timestamp}.png"
        os.makedirs("images", exist_ok=True)
        img.save(filename)
        return filename
    except Exception as e:
        print(f"Error saving image: {e}")
        return None

def generate_image():
    """Generate image using DALL-E 3"""
    try:
        prompt = input("\nEnter your image prompt: ")
        size = input("Choose size (1: 1024x1024, 2: 1024x1792, 3: 1792x1024): ")
        
        size_map = {
            "1": "1024x1024",
            "2": "1024x1792",
            "3": "1792x1024"
        }
        
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size=size_map.get(size, "1024x1024"),
            quality="standard",
            n=1,
        )
        
        image_url = response.data[0].url
        filename = save_image(image_url, "dalle3")
        
        if filename:
            print(f"\nImage saved as: {filename}")
            print(f"Revised prompt: {response.data[0].revised_prompt}")
        
    except Exception as e:
        print(f"Error generating image: {e}")

def edit_image():
    """Edit image using DALL-E 2"""
    try:
        image_path = input("\nEnter path to image to edit (PNG format): ")
        mask_path = input("Enter path to mask image (PNG format): ")
        prompt = input("Enter prompt for editing: ")
        
        response = client.images.edit(
            model="dall-e-2",
            image=open(image_path, "rb"),
            mask=open(mask_path, "rb"),
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        
        filename = save_image(response.data[0].url, "dalle2_edit")
        if filename:
            print(f"\nEdited image saved as: {filename}")
            
    except Exception as e:
        print(f"Error editing image: {e}")

def create_variation():
    """Create variation using DALL-E 2"""
    try:
        image_path = input("\nEnter path to image for variation (PNG format): ")
        
        response = client.images.create_variation(
            model="dall-e-2",
            image=open(image_path, "rb"),
            n=1,
            size="1024x1024"
        )
        
        filename = save_image(response.data[0].url, "dalle2_variation")
        if filename:
            print(f"\nVariation saved as: {filename}")
            
    except Exception as e:
        print(f"Error creating variation: {e}")

def main_menu():
    while True:
        clear_screen()
        print("\nDALL-E Image Generator")
        print("1. Generate New Image (DALL-E 3)")
        print("2. Edit Image (DALL-E 2)")
        print("3. Create Variation (DALL-E 2)")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            generate_image()
        elif choice == "2":
            edit_image()
        elif choice == "3":
            create_variation()
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()