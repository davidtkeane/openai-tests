#!/usr/bin/env python3

# Created by Ranger 😎

# Import the required modules
from termcolor import colored
import base64
from openai import OpenAI
import os
# Load the API key from an environment variable
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

# Print welcome banner
print("")
print(colored("Made By David", "red"))
print(colored("Version 1.0.0", "red"))
print(colored("  Dec 2024", "red"))
print("")

completion = client.chat.completions.create(
    model="gpt-4o-audio-preview",
    modalities=["text", "audio"],
    audio={"voice": "alloy", "format": "wav"},
    messages=[
        {
            "role": "user",
            "content": "Can you explain the structure of a python script, how it works and what a script needs to work?"
        }
    ]
)

print(completion.choices[0])

wav_bytes = base64.b64decode(completion.choices[0].message.audio.data)
with open("python.wav", "wb") as f:
    f.write(wav_bytes)