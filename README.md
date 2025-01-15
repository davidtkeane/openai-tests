# OpenAI API Integration Suite 🚀

A comprehensive collection of Python scripts demonstrating various OpenAI API integrations including GPT-4, DALL-E 3, Whisper, and TTS functionalities.

## Table of Contents 📑
- [Overview](#overview-)
- [Getting Started](#getting-started-)
- [API Key Setup](#api-key-setup-)
- [Scripts](#scripts-)
  - [Chat Completions](#chat-completions-)
  - [Image Generation](#image-generation-)
  - [Speech-to-Text](#speech-to-text-)
  - [Text-to-Speech](#text-to-speech-)
  - [Vision Analysis](#vision-analysis-)
  - [Multi-Modal Testing](#multi-modal-testing-)

## Overview 🌟

This repository contains a suite of Python scripts that showcase different OpenAI API capabilities. Each script is designed to be modular and easy to understand, with comprehensive error handling and cost tracking.

## Getting Started 🛠️

### Prerequisites
```bash
pip install openai python-dotenv pillow requests tqdm termcolor pydub
```

### API Key Setup 🔑

1. Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)
2. Create a `.env` file in your project root:
```bash
touch .env
```
3. Add your API key to the `.env` file:
```
OPENAI_API_KEY=your-api-key-here
```
4. Make sure to add `.env` to your `.gitignore` file!

## Scripts 📚

### Chat Completions 💬
**File: openai_api_an_token_test.py**
- Tests GPT-4 chat completions
- Tracks token usage and costs
- Displays costs in EUR
```bash
python openai_api_an_token_test.py
```

### Image Generation 🎨
**File: openai_images.py** (Enhanced Version)
- Generates images using DALL-E 3
- Supports multiple sizes and quality options
- Includes cost tracking and image management
```bash
python openai_images.py
```

**File: openai_images-v1.py** (Basic Version)
- Simpler implementation with basic DALL-E functionality
- Includes image editing and variation creation
```bash
python openai_images-v1.py
```

### Speech-to-Text 🎤
**File: openai_Speech-to-Text.py** (Base Version)
- Transcribes audio using Whisper API
- Supports multiple formats and languages
```bash
python openai_Speech-to-Text.py
```

**File: openai_Speech-to-Text-v2.py** (Enhanced Version)
- Adds batch processing capability
- Improved error handling and logging
- More detailed cost tracking
```bash
python openai_Speech-to-Text-v2.py
```

### Text-to-Speech 🔊
**File: openai_Text-to-Speech.py**
- Converts text to speech using OpenAI's TTS API
- Supports multiple voices and formats
- Includes cost calculation
```bash
python openai_Text-to-Speech.py
```

### Vision Analysis 👁️
**File: openai_vision.py**
- Analyzes images using GPT-4 Vision
- Supports both URL and local images
- Includes detailed cost tracking
```bash
python openai_vision.py
```

### Multi-Modal Testing 🔄
**File: openai_test_all.py**
- Comprehensive test suite for all OpenAI APIs
- Includes cost tracking for each service
- Supports batch processing
```bash
python openai_test_all.py
```

## Features ✨

- 🔐 Secure API key handling
- 💰 Detailed cost tracking
- 📊 Usage statistics
- 🗂️ Organized output management
- 🚨 Comprehensive error handling
- 📝 Logging functionality

## Cost Tracking 💸

All scripts include built-in cost tracking in EUR, helping you monitor your API usage:
- GPT-4 input: €0.0015 per 1K tokens
- GPT-4 output: €0.002 per 1K tokens
- DALL-E 3: €0.02-0.04 per image
- Whisper: €0.006 per minute
- TTS: €0.015-0.030 per 1K characters

## Contributing 🤝

Feel free to submit issues and enhancement requests!

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments 🙏

- OpenAI for their fantastic APIs
- The Python community for various helpful packages