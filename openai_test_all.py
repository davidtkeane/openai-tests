#!/usr/bin/env python3

# Created by Ranger 😎

# Import the required modules
import os
from pathlib import Path
from openai import OpenAI
import base64
from PIL import Image
import requests
from datetime import datetime
import time
from typing import Dict, Optional
import json
from pydub import AudioSegment

# API Cost Constants (USD)
COSTS = {
    'gpt-4': {
        'input': 0.01,    # Per 1K tokens
        'output': 0.03
    },
    'gpt-3.5': {
        'input': 0.0005,
        'output': 0.0015
    },
    'dalle-3': {
        'standard': 0.02,
        'hd': 0.04
    },
    'whisper': {
        'transcription': 0.006,  # Per minute
        'translation': 0.006
    },
    'tts-1': {
        'standard': 0.015,  # Per 1K characters
        'hd': 0.030
    },
    'vision': {
        'input': 0.01,
        'output': 0.03,
        'image': 0.085
    }
}

EUR_RATE = 0.93

class APITester:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.costs = {'total': 0}
        self.setup_directories()
        
    def setup_directories(self):
        """Create output directories"""
        dirs = ['output/text', 'output/images', 'output/audio', 'output/transcripts']
        for dir in dirs:
            Path(dir).mkdir(parents=True, exist_ok=True)

    def test_chat(self, prompt: str, model: str = "gpt-4") -> Dict:
        """Test chat completion and calculate costs"""
        start = time.time()
        response = self.client.chat.completions.create(
            model=f"{model}-turbo-preview",
            messages=[{"role": "user", "content": prompt}]
        )
        
        duration = time.time() - start
        tokens = response.usage.total_tokens
        cost = (tokens/1000) * COSTS[model]['input'] * EUR_RATE
        
        self.costs['total'] += cost
        self.costs[model] = self.costs.get(model, 0) + cost
        
        return {
            'response': response.choices[0].message.content,
            'tokens': tokens,
            'duration': duration,
            'cost_eur': cost
        }

    def test_image(self, prompt: str, quality: str = "standard") -> Dict:
        """Test DALL-E image generation"""
        start = time.time()
        response = self.client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            quality=quality,
            n=1
        )
        
        duration = time.time() - start
        cost = COSTS['dalle-3'][quality] * EUR_RATE
        
        self.costs['total'] += cost
        self.costs['dalle-3'] = self.costs.get('dalle-3', 0) + cost
        
        return {
            'url': response.data[0].url,
            'duration': duration,
            'cost_eur': cost
        }

    def test_vision(self, image_path: str, prompt: str) -> Dict:
        """Test GPT-4 Vision analysis"""
        with open(image_path, "rb") as img_file:
            base64_image = base64.b64encode(img_file.read()).decode('utf-8')
            
        start = time.time()
        response = self.client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[{
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                ]
            }]
        )
        
        duration = time.time() - start
        cost = COSTS['vision']['image'] * EUR_RATE
        
        self.costs['total'] += cost
        self.costs['vision'] = self.costs.get('vision', 0) + cost
        
        return {
            'response': response.choices[0].message.content,
            'duration': duration,
            'cost_eur': cost
        }

    def test_speech_to_text(self, audio_path: str, task: str = "transcribe") -> Dict:
        """Test Whisper speech-to-text"""
        audio = AudioSegment.from_file(audio_path)
        duration_minutes = len(audio) / (1000 * 60)
        
        start = time.time()
        with open(audio_path, "rb") as audio_file:
            if task == "transcribe":
                response = self.client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file
                )
            else:
                response = self.client.audio.translations.create(
                    model="whisper-1",
                    file=audio_file
                )
        
        duration = time.time() - start
        cost = duration_minutes * COSTS['whisper'][task] * EUR_RATE
        
        self.costs['total'] += cost
        self.costs['whisper'] = self.costs.get('whisper', 0) + cost
        
        return {
            'text': response.text,
            'duration': duration,
            'cost_eur': cost
        }

    def test_text_to_speech(self, text: str, voice: str = "alloy", quality: str = "standard") -> Dict:
        """Test text-to-speech generation"""
        char_count = len(text)
        start = time.time()
        
        response = self.client.audio.speech.create(
            model="tts-1",
            voice=voice,
            input=text
        )
        
        duration = time.time() - start
        cost = (char_count/1000) * COSTS['tts-1'][quality] * EUR_RATE
        
        self.costs['total'] += cost
        self.costs['tts-1'] = self.costs.get('tts-1', 0) + cost
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"output/audio/speech_{timestamp}.mp3"
        response.stream_to_file(output_file)
        
        return {
            'file': output_file,
            'duration': duration,
            'cost_eur': cost
        }

def main_menu():
    tester = APITester()
    
    while True:
        print("\nOpenAI API Test Suite")
        print("1. Test Chat Completion")
        print("2. Test Image Generation")
        print("3. Test Vision Analysis")
        print("4. Test Speech-to-Text")
        print("5. Test Text-to-Speech")
        print("6. View Cost Summary")
        print("7. Exit")
        
        choice = input("\nEnter choice (1-7): ")
        
        try:
            if choice == "1":
                model = input("Choose model (gpt-4/gpt-3.5): ")
                prompt = input("Enter prompt: ")
                result = tester.test_chat(prompt, model)
                print(f"\nResponse: {result['response']}")
                print(f"Tokens: {result['tokens']}")
                print(f"Cost: €{result['cost_eur']:.4f}")
                
            elif choice == "2":
                prompt = input("Enter image prompt: ")
                quality = input("Quality (standard/hd): ")
                result = tester.test_image(prompt, quality)
                print(f"\nImage URL: {result['url']}")
                print(f"Cost: €{result['cost_eur']:.4f}")
                
            elif choice == "3":
                image_path = input("Enter image path: ")
                prompt = input("Enter prompt: ")
                result = tester.test_vision(image_path, prompt)
                print(f"\nAnalysis: {result['response']}")
                print(f"Cost: €{result['cost_eur']:.4f}")
                
            elif choice == "4":
                audio_path = input("Enter audio file path: ")
                task = input("Task (transcribe/translate): ")
                result = tester.test_speech_to_text(audio_path, task)
                print(f"\nText: {result['text']}")
                print(f"Cost: €{result['cost_eur']:.4f}")
                
            elif choice == "5":
                text = input("Enter text: ")
                voice = input("Voice (alloy/echo/fable/onyx/nova/shimmer): ")
                result = tester.test_text_to_speech(text, voice)
                print(f"\nSaved to: {result['file']}")
                print(f"Cost: €{result['cost_eur']:.4f}")
                
            elif choice == "6":
                print("\nCost Summary:")
                for model, cost in tester.costs.items():
                    print(f"{model}: €{cost:.4f}")
                    
            elif choice == "7":
                print("\nGoodbye!")
                break
                
        except Exception as e:
            print(f"\nError: {str(e)}")
            
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()