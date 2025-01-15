#!/usr/bin/env python3

# Created by Ranger 😎

# Import the required modules
import os
from pathlib import Path
from openai import OpenAI
import time
from tqdm import tqdm
import shutil
import logging
from datetime import datetime

# Constants
COST_PER_1K_CHARS = 0.015
HD_COST_PER_1K_CHARS = 0.030
EUR_RATE = 0.93
SUPPORTED_LANGUAGES = ["en", "es", "fr", "de", "it", "pt", "pl", "tr"]

# Setup logging
logging.basicConfig(
    filename='tts_generator.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def generate_speech(text, voice="alloy", model="tts-1", output_format="mp3", language="en"):
    try:
        # Calculate cost
        is_hd = model == "tts-1-hd"
        cost = (len(text) / 1000) * (HD_COST_PER_1K_CHARS if is_hd else COST_PER_1K_CHARS) * EUR_RATE
        
        # Create output directory with language subfolder
        output_dir = Path("generated_audio") / language / time.strftime("%Y%m%d")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate filename with metadata
        timestamp = datetime.now().strftime("%H%M%S")
        filename = f"{voice}_{model}_{timestamp}.{output_format}"
        speech_file = output_dir / filename
        
        print(f"\nGenerating speech...")
        print(f"Language: {language.upper()}")
        print(f"Characters: {len(text):,}")
        print(f"Estimated cost: €{cost:.4f}")
        
        # Stream and save with progress bar
        with tqdm(total=100, desc="Processing") as pbar:
            response = client.audio.speech.create(
                model=model,
                voice=voice,
                input=text,
                response_format=output_format
            )
            
            with open(speech_file, 'wb') as f:
                for chunk in response.iter_bytes(chunk_size=1024):
                    f.write(chunk)
                    pbar.update(2)
        
        logging.info(f"Generated: {filename} - Cost: €{cost:.4f}")
        print(f"\nAudio saved as: {speech_file}")
        return speech_file
        
    except Exception as e:
        logging.error(f"Error generating speech: {str(e)}")
        print(f"Error: {str(e)}")
        return None

def preview_voice(voice, language="en"):
    sample_text = "This is a preview of my voice."
    preview_file = generate_speech(
        text=sample_text,
        voice=voice,
        language=language
    )
    if preview_file:
        os.system(f"afplay {preview_file}")

def main_menu():
    voices = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]
    formats = ["mp3", "opus", "aac", "flac", "pcm"]
    current_language = "en"
    
    while True:
        os.system('clear')
        print("\nText-to-Speech Generator 2.0")
        print("1. Generate Speech (Standard)")
        print("2. Generate Speech (HD)")
        print("3. Change Voice")
        print("4. Change Format")
        print("5. Change Language")
        print("6. Preview Voices")
        print("7. Exit")
        
        choice = input("\nChoice (1-7): ")
        
        if choice in ["1", "2"]:
            text = input("\nEnter text: ")
            model = "tts-1-hd" if choice == "2" else "tts-1"
            generate_speech(
                text,
                voice=voices[0],
                model=model,
                output_format=formats[0],
                language=current_language
            )
        
        elif choice == "3":
            print("\nVoices:")
            for i, voice in enumerate(voices, 1):
                print(f"{i}. {voice}")
            voice_choice = input("\nChoose voice (1-6): ")
            if voice_choice.isdigit() and 1 <= int(voice_choice) <= len(voices):
                voices[0], voices[int(voice_choice)-1] = voices[int(voice_choice)-1], voices[0]
                print(f"\nDefault voice set to: {voices[0]}")
        
        elif choice == "4":
            print("\nFormats:")
            for i, fmt in enumerate(formats, 1):
                print(f"{i}. {fmt}")
            format_choice = input("\nChoose format (1-5): ")
            if format_choice.isdigit() and 1 <= int(format_choice) <= len(formats):
                formats[0], formats[int(format_choice)-1] = formats[int(format_choice)-1], formats[0]
                print(f"\nDefault format set to: {formats[0]}")
        
        elif choice == "5":
            print("\nSupported Languages:")
            for i, lang in enumerate(SUPPORTED_LANGUAGES, 1):
                print(f"{i}. {lang.upper()}")
            lang_choice = input("\nChoose language: ")
            if lang_choice.isdigit() and 1 <= int(lang_choice) <= len(SUPPORTED_LANGUAGES):
                current_language = SUPPORTED_LANGUAGES[int(lang_choice)-1]
                print(f"\nLanguage set to: {current_language.upper()}")
        
        elif choice == "6":
            print("\nPreviewing voices...")
            for voice in voices:
                print(f"\nPreviewing {voice}...")
                preview_voice(voice, current_language)
                time.sleep(1)
        
        elif choice == "7":
            print("\nGoodbye!")
            break
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()