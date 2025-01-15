# 🤖 OpenAI API Integration Suite

> A comprehensive collection of Python scripts demonstrating OpenAI's powerful APIs, designed to be accessible and easy to understand, especially for users with learning differences like dyslexia.

> **Note**: These scripts were developed using the [OpenAI API documentation](https://platform.openai.com/docs/api-reference) as a reference, with additional enhancements for better usability and error handling.

## 📚 Table of Contents
- [Overview & Accessibility](#overview--accessibility-)
- [Installation](#installation-)
- [API Key Setup](#api-key-setup-)
- [Core Features](#core-features-)
- [Script Details](#script-details-)
- [Usage Examples](#usage-examples-)
- [Cost Tracking](#cost-tracking-)
- [Future Improvements](#future-improvements-)
- [Troubleshooting](#troubleshooting-)

## Overview & Accessibility 🌟

This suite is designed with accessibility in mind, featuring:
- Clear, step-by-step instructions
- Visual organization with emojis
- Consistent menu structures
- Detailed error messages
- Progress indicators
- Cost transparency

## Installation 🛠️

```bash
# Install required packages
pip install openai python-dotenv pillow requests tqdm termcolor pydub
```

## API Key Setup 🔑

1. Visit [OpenAI Platform](https://platform.openai.com/api-keys)
2. Click "Create New Secret Key"
3. Create a `.env` file:
```
OPENAI_API_KEY=your-api-key-here
```

## Core Features 🎯

Each script includes:
- 📊 Real-time cost tracking
- 🔄 Progress indicators
- � Automatic file organization
- 🛡️ Error handling
- 📝 Detailed logging
- 🎨 Color-coded outputs

💡 **Tip**: Each script includes help menus and detailed prompts to guide you through the process. Just follow the numbered options and on-screen instructions.

## Script Details 📋

### 1. Image Generation (openai_images.py)
Advanced features:
- Multiple image sizes (1024x1024, 1024x1792, 1792x1024)
- HD quality option
- Batch processing
- Image variation creation
- Cost estimation per request
- Organized file storage

### 2. Speech-to-Text (openai_Speech-to-Text.py)
Capabilities:
- Multi-language support
- Batch processing
- Multiple output formats (text, JSON, SRT, VTT)
- Progress tracking
- File validation
- Cost monitoring

### 3. Text-to-Speech (openai_Text-to-Speech.py)
Features:
- Multiple voices (Alloy, Echo, Fable, Onyx, Nova, Shimmer)
- Various audio formats (MP3, WAV, OPUS, AAC)
- Language selection
- Voice preview function
- Detailed cost breakdown

### 4. Vision Analysis (openai_vision.py)
Capabilities:
- Image analysis from URLs or local files
- Detailed descriptions
- Cost-efficient processing
- Support for various image formats
- Batch processing option

### 5. Comprehensive Testing (openai_test_all.py)
Features:
- Tests all API endpoints
- Detailed reporting
- Cost tracking across services
- Performance metrics
- Error logging


### 6. Audio Text-to-Speech (openai_audio.p) 🎤 
(Enhanced Version)
Features:
- Object-oriented design with AudioGenerator class
- Multiple voice options (alloy, echo, fable, onyx, nova, shimmer)
- Format selection (mp3, wav, opus, aac)
- Detailed cost tracking
- Progress indicators
- Error handling and logging
- Language support
- Organized file storage

```bash
python openai_audio.py
```

Key Improvements in Enhanced Version:
- 📊 Cost calculation and tracking
- 🔊 Multiple voice options
- 💾 Better file organization
- 🌍 Language support
- 📝 Logging functionality
- ⚠️ Comprehensive error handling
- 🎵 Multiple audio formats

### API Token Testing (openai_api_an_token_test.py) 🔑 

- Tests API connectivity
- Calculates token usage
- Tracks costs in EUR
- Supports GPT-4 model
- Basic error handling

```bash
python openai_api_an_token_test.py
```

## Usage Examples 🎓

### Image Generation
```bash
python openai_images.py
# Follow the interactive menu to:
# 1. Generate new images
# 2. Edit existing images
# 3. Create variations
# 4. View cost summary
```

## Cost Tracking �

Real-time cost monitoring in EUR:
- GPT-4 input: €0.0015/1K tokens
- GPT-4 output: €0.002/1K tokens
- DALL-E 3: €0.02-0.04/image
- Whisper: €0.006/minute
- TTS: €0.015-0.030/1K characters

## Future Improvements 🚀

Planned enhancements:
1. GUI interface
2. Batch processing improvements
3. Additional language support
4. Advanced error recovery
5. More customization options
6. Enhanced accessibility features

## Future Updates & Planned Improvements: 🚀
- Multiple model support
- Batch testing capabilities
- Cost comparison between models
- Historical usage tracking
- Performance metrics
- Interactive testing mode
- Export results to CSV/JSON
- Advanced logging options
- Integration with other AI tools

### Audio Processing
- Batch processing for multiple files
- More voice options
- Custom voice fine-tuning
- Real-time voice preview
- Audio file format conversion
- Background noise reduction
- Speed and pitch adjustment

### API Testing
- Interactive testing interface
- Model comparison tool
- Cost optimization suggestions
- Usage analytics dashboard
- Rate limit monitoring
- Automated testing schedules
- Performance benchmarking

## Troubleshooting 🔧

Common issues and solutions:
1. API Key errors
   - Check .env file location
   - Verify key format
2. File format issues
   - Check supported formats
   - Verify file permissions
3. Memory errors
   - Use batch processing for large files
   - Monitor system resources

## Support & Accessibility 🤝

This project aims to be accessible to all users. If you need:
- Alternative documentation formats
- Additional explanations
- Help with setup
- Accessibility improvements

Please open an issue or contact the maintainers.

## License 📄

MIT License - See LICENSE file for details.

## Acknowledgments 🙏

- OpenAI for their fantastic APIs
- The Python community for various helpful packages

---