#!/usr/bin/env python3

# Created by Ranger 😎

# Import the required modules
import os
import base64
from openai import OpenAI
from PIL import Image
import requests
from io import BytesIO

# Constants for costs
IMAGE_TOKENS_LOW = 85
IMAGE_TOKENS_HIGH = 170
TOKEN_COST_USD = 0.01  # Cost per 1K tokens
EUR_RATE = 0.93

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def calculate_image_cost(image_size, detail="auto"):
    if detail == "low":
        tokens = IMAGE_TOKENS_LOW
    else:
        # Calculate high detail tokens
        width, height = image_size
        scaled_width = min(width, 2048)
        scaled_height = min(height, 2048)
        tiles = ((scaled_width + 511) // 512) * ((scaled_height + 511) // 512)
        tokens = (tiles * IMAGE_TOKENS_HIGH) + IMAGE_TOKENS_LOW
    
    cost_usd = (tokens / 1000) * TOKEN_COST_USD
    cost_eur = cost_usd * EUR_RATE
    return tokens, cost_eur

def analyze_image_url(url, detail="auto"):
    try:
        # Get image size for cost calculation
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        tokens, cost = calculate_image_cost(img.size, detail)
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": [{
                    "type": "text",
                    "text": "What's in this image?"
                }, {
                    "type": "image_url",
                    "image_url": {
                        "url": url,
                        "detail": detail
                    }
                }]
            }],
            max_tokens=300
        )
        
        print(f"\nAnalysis Result:\n{response.choices[0].message.content}")
        print(f"\nToken Usage:")
        print(f"Image tokens: {tokens}")
        print(f"Cost: €{cost:.4f}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

def analyze_local_image(image_path, detail="auto"):
    try:
        # Get image size for cost calculation
        img = Image.open(image_path)
        tokens, cost = calculate_image_cost(img.size, detail)
        
        base64_image = encode_image(image_path)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": [{
                    "type": "text",
                    "text": "What's in this image?"
                }, {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}",
                        "detail": detail
                    }
                }]
            }],
            max_tokens=300
        )
        
        print(f"\nAnalysis Result:\n{response.choices[0].message.content}")
        print(f"\nToken Usage:")
        print(f"Image tokens: {tokens}")
        print(f"Cost: €{cost:.4f}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

def main_menu():
    while True:
        clear_screen()
        print("\nVision Analyzer")
        print("1. Analyze Image from URL")
        print("2. Analyze Local Image")
        print("3. High Detail Analysis")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            url = input("\nEnter image URL: ")
            analyze_image_url(url)
        elif choice == "2":
            path = input("\nEnter image path: ")
            analyze_local_image(path)
        elif choice == "3":
            print("\n1. URL")
            print("2. Local File")
            sub_choice = input("Choose source (1-2): ")
            if sub_choice == "1":
                url = input("\nEnter image URL: ")
                analyze_image_url(url, "high")
            elif sub_choice == "2":
                path = input("\nEnter image path: ")
                analyze_local_image(path, "high")
        elif choice == "4":
            print("\nGoodbye!")
            break
            
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()