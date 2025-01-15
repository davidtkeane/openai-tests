#!/usr/bin/env python3

# Created by Ranger 😎

# Import the required modules
import os
from pathlib import Path
from openai import OpenAI
import time
from tqdm import tqdm
from pydub import AudioSegment
import base64
import json
import logging
from datetime import datetime
import shutil
import hashlib
from typing import Optional, Dict, List, Union

# Constants
SUPPORTED_FORMATS = ['mp3', 'mp4', 'mpeg', 'mpga', 'm4a', 'wav', 'webm']
MAX_FILE_SIZE = 25 * 1024 * 1024  # 25 MB
COST_PER_MINUTE = 0.006  # USD per minute
EUR_RATE = 0.93

SUPPORTED_LANGUAGES = {
    'en': 'English', 'es': 'Spanish', 'fr': 'French', 
    'de': 'German', 'it': 'Italian', 'ja': 'Japanese',
    'zh': 'Chinese', 'ko': 'Korean', 'ru': 'Russian',
    'ar': 'Arabic', 'hi': 'Hindi', 'pt': 'Portuguese'
}

OUTPUT_FORMATS = ['text', 'json', 'srt', 'vtt', 'verbose_json']

logging.basicConfig(
    filename='speech_to_text.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

class AudioProcessor:
    def __init__(self):
        self.total_cost = 0
        self.processed_files = 0
        self.failed_files = []
        self.setup_directories()

    def setup_directories(self):
        directories = ['transcripts', 'temp', 'logs']
        for dir_name in directories:
            Path(dir_name).mkdir(exist_ok=True)

    def calculate_cost(self, duration_minutes: float) -> float:
        cost_usd = duration_minutes * COST_PER_MINUTE
        return cost_usd * EUR_RATE

    def validate_audio_file(self, file_path: str) -> tuple[bool, str]:
        try:
            if not os.path.exists(file_path):
                return False, "File not found"
            extension = file_path.lower().split('.')[-1]
            if extension not in SUPPORTED_FORMATS:
                return False, f"Unsupported format: {extension}"
            if os.path.getsize(file_path) == 0:
                return False, "File is empty"
            AudioSegment.from_file(file_path)
            return True, "Valid audio file"
        except Exception as e:
            return False, f"Validation error: {str(e)}"

    def process_audio(self, file_path: str, task: str = "transcribe", 
                     language: Optional[str] = None, timestamps: bool = False, 
                     output_format: str = "text", prompt: Optional[str] = None) -> Optional[dict]:
        try:
            is_valid, message = self.validate_audio_file(file_path)
            if not is_valid:
                raise ValueError(message)

            audio = AudioSegment.from_file(file_path)
            duration_minutes = len(audio) / (1000 * 60)
            cost_eur = self.calculate_cost(duration_minutes)
            self.total_cost += cost_eur

            print(f"\nProcessing: {os.path.basename(file_path)}")
            print(f"Duration: {duration_minutes:.2f} minutes")
            print(f"Estimated cost: €{cost_eur:.4f}")

            file_size = os.path.getsize(file_path)
            if file_size > MAX_FILE_SIZE:
                return self.split_and_process(file_path, task, language)

            with tqdm(total=100, desc="Processing") as pbar:
                result = self._process_single_file(file_path, task, language, 
                                                timestamps, output_format, prompt, pbar)

            output_file = self.save_output(result, task, output_format)
            self.processed_files += 1
            logging.info(f"Processed {file_path} -> {output_file}")
            return result

        except Exception as e:
            self.failed_files.append((file_path, str(e)))
            logging.error(f"Error processing {file_path}: {str(e)}")
            print(f"\nError: {str(e)}")
            return None

    def _process_single_file(self, file_path: str, task: str, language: Optional[str],
                           timestamps: bool, output_format: str, 
                           prompt: Optional[str], pbar: tqdm) -> dict:
        with open(file_path, "rb") as audio_file:
            if task == "transcribe":
                response = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file,
                    response_format="verbose_json" if timestamps else output_format,
                    language=language,
                    prompt=prompt,
                    timestamp_granularities=["word"] if timestamps else None
                )
            else:
                response = client.audio.translations.create(
                    model="whisper-1",
                    file=audio_file,
                    response_format=output_format,
                    prompt=prompt
                )
            pbar.update(100)
            return response

    def split_and_process(self, file_path: str, task: str, language: Optional[str]) -> Optional[str]:
        try:
            print("\nFile exceeds 25MB limit. Splitting into chunks...")
            audio = AudioSegment.from_file(file_path)
            chunk_length = 10 * 60 * 1000
            chunks = [audio[i:i+chunk_length] for i in range(0, len(audio), chunk_length)]
            
            results = []
            for i, chunk in enumerate(chunks, 1):
                print(f"\nProcessing chunk {i}/{len(chunks)}")
                temp_file = Path("temp") / f"chunk_{i}.mp3"
                chunk.export(temp_file, format="mp3")
                
                result = self.process_audio(str(temp_file), task, language)
                if result:
                    results.append(result)
                
                temp_file.unlink()
            
            return " ".join(results) if results else None
            
        except Exception as e:
            logging.error(f"Error splitting audio: {str(e)}")
            print(f"\nError splitting audio: {str(e)}")
            return None

    def save_output(self, response: Union[str, dict], task: str, 
                   output_format: str) -> Path:
        output_dir = Path("transcripts") / datetime.now().strftime("%Y%m%d")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        timestamp = datetime.now().strftime("%H%M%S")
        output_file = output_dir / f"{timestamp}_{task}.{output_format}"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            if isinstance(response, dict):
                json.dump(response, f, indent=2, ensure_ascii=False)
            else:
                f.write(str(response))
                
        return output_file

    def generate_summary(self) -> dict:
        return {
            "total_files_processed": self.processed_files,
            "total_cost_eur": round(self.total_cost, 4),
            "failed_files": self.failed_files,
            "timestamp": datetime.now().isoformat()
        }

def main_menu():
    processor = AudioProcessor()
    
    while True:
        clear_screen()
        print("\nEnhanced Speech-to-Text Generator")
        print("1. Transcribe Single File")
        print("2. Translate to English")
        print("3. Batch Process Directory")
        print("4. Advanced Options")
        print("5. View Supported Formats")
        print("6. View Processing Summary")
        print("7. Exit")
        
        choice = input("\nEnter choice (1-7): ")
        
        try:
            if choice == "1":
                file_path = input("\nEnter audio file path: ")
                lang = input("Enter language code (or press Enter for auto): ")
                processor.process_audio(file_path, language=lang if lang else None)
                
            elif choice == "2":
                file_path = input("\nEnter audio file path: ")
                processor.process_audio(file_path, task="translate")
                
            elif choice == "3":
                directory = input("\nEnter directory path: ")
                task = input("Choose task (transcribe/translate): ")
                for format in SUPPORTED_FORMATS:
                    for file in Path(directory).glob(f"*.{format}"):
                        processor.process_audio(str(file), task=task)
                
            elif choice == "4":
                print("\nAdvanced Options:")
                print("1. Transcribe with Timestamps")
                print("2. Custom Output Format")
                print("3. Add Custom Prompt")
                print("4. Quality Check")
                sub_choice = input("Choose option (1-4): ")
                
                file_path = input("\nEnter audio file path: ")
                if sub_choice == "1":
                    processor.process_audio(file_path, timestamps=True, 
                                         output_format="verbose_json")
                elif sub_choice == "2":
                    print("\nAvailable formats:", ", ".join(OUTPUT_FORMATS))
                    format = input("Choose format: ")
                    processor.process_audio(file_path, output_format=format)
                elif sub_choice == "3":
                    prompt = input("Enter custom prompt: ")
                    processor.process_audio(file_path, prompt=prompt)
                elif sub_choice == "4":
                    is_valid, message = processor.validate_audio_file(file_path)
                    print(f"\nQuality check result: {message}")
                
            elif choice == "5":
                print("\nSupported formats:", ", ".join(SUPPORTED_FORMATS))
                print(f"Maximum file size: {MAX_FILE_SIZE/(1024*1024)}MB")
                print("\nSupported languages:")
                for code, lang in SUPPORTED_LANGUAGES.items():
                    print(f"  {code}: {lang}")
                    
            elif choice == "6":
                summary = processor.generate_summary()
                print("\nProcessing Summary:")
                print(f"Total files processed: {summary['total_files_processed']}")
                print(f"Total cost: €{summary['total_cost_eur']}")
                if summary['failed_files']:
                    print("\nFailed files:")
                    for file, error in summary['failed_files']:
                        print(f"  {file}: {error}")
                
            elif choice == "7":
                print("\nGoodbye!")
                break
                
        except Exception as e:
            print(f"\nError: {str(e)}")
            logging.error(f"Menu error: {str(e)}")
            
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()