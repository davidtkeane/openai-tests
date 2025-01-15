# 🤖 OpenAI API Integration Suite


<p align="center">
  <img src="https://img.shields.io/badge/Microsoft-Windows%2011-0078D6?logo=windows&logoColor=0078D6&labelColor=white" alt="Windows-Badge">
  <img src="https://img.shields.io/badge/Apple-macOS-white?logo=apple&logoColor=white&labelColor=gray" alt="AppleMac-Badge">
  <img src="https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black&labelColor=white" alt="Linux-Badge">
</p>

> A comprehensive collection of Python scripts demonstrating OpenAI's powerful APIs, designed to be accessible and easy to understand, especially for users with learning differences like dyslexia.

> **Note**: These scripts were developed using the [OpenAI API documentation](https://platform.openai.com/docs/api-reference) as a reference, with additional enhancements for better usability and error handling.


```markdown
**Note:** These scripts require an active OpenAI API key. Please ensure you have one before proceeding.

**Note:** Visit the [OpenAI Platform](https://platform.openai.com/) and create a new secret key.

📚 **Table of Contents**

*   [Overview & Accessibility](#overview--accessibility)
*   [Installation](#installation)
*   [API Key Setup](#api-key-setup)
*   [Core Features](#core-features)
*   [Script Details](#script-details)
*   [Usage Examples](#usage-examples)
*   [Cost Tracking](#cost-tracking)
*   [Future Improvements](#future-improvements)
*   [Troubleshooting](#troubleshooting)
*   [Support & Accessibility](#support--accessibility)
*   [License](#license)
*   [Acknowledgments](#acknowledgments)

## Overview & Accessibility 🌟

This suite prioritizes accessibility with:

*   Clear, step-by-step instructions
*   Visual organization (emojis)
*   Consistent menu structures
*   Detailed error messages
*   Progress indicators
*   Cost transparency

```
## Installation 🛠️
To install the necessary packages, run the following command in your terminal:

```bash
pip install openai python-dotenv pillow requests tqdm termcolor pydub
```

## API Key Setup 🔑

1.  Visit the [OpenAI Platform](https://platform.openai.com/) and create a new secret key.
2.  Create a `.env` file in the root directory of this project:

    ```env
    OPENAI_API_KEY=your-api-key-here
    ```
   Replace `your-api-key-here` with your actual API key.

## Core Features 🎯

Each script incorporates these features:

*   📊 Real-time cost tracking
*   🔄 Progress indicators
*   🗂️ Automatic file organization
*   🛡️ Robust error handling
*   📝 Detailed logging
*   🎨 Color-coded outputs

**Tip:** Each script includes help menus and prompts. Just follow the on-screen instructions.

## Script Details 📋

1.  **Image Generation (`openai_images.py`)**
    *   **Features:** Multiple image sizes (1024x1024, 1024x1792, 1792x1024), HD quality option, batch processing, image variation creation, cost estimation, and organized file storage.
     *  **To Run:** `python openai_images.py`

2.  **Speech-to-Text (`openai_Speech-to-Text.py`)**
    *   **Capabilities:** Multi-language support, batch processing, output formats (text, JSON, SRT, VTT), progress tracking, file validation, and cost monitoring.
     *  **To Run:** `python openai_Speech-to-Text.py`

3.  **Text-to-Speech (`openai_Text-to-Speech.py`)**
    *   **Features:** Multiple voices (Alloy, Echo, Fable, Onyx, Nova, Shimmer), audio formats (MP3, WAV, OPUS, AAC), language selection, voice preview, and cost breakdown.
    * **To Run:** `python openai_Text-to-Speech.py`

4.  **Vision Analysis (`openai_vision.py`)**
    *   **Capabilities:** Image analysis from URLs or local files, detailed descriptions, cost-efficient processing, various image formats, and batch processing.
     *  **To Run:** `python openai_vision.py`

5.  **Comprehensive Testing (`openai_test_all.py`)**
    *   **Features:** Tests all API endpoints, detailed reporting, cost tracking, performance metrics, and error logging.
     * **To Run:** `python openai_test_all.py`

6.  **Audio Text-to-Speech (Enhanced) (`openai_audio.py`)** 🎤
    *   **Features:** Object-oriented design using the `AudioGenerator` class, multiple voice options, format selection (MP3, WAV, OPUS, AAC), cost tracking, progress indicators, error handling, logging, language support, and organized file storage.
    *   **To Run:** `python openai_audio.py`

7. **API Token Testing (`openai_api_an_token_test.py`)** 🔑
     * **Features:** Tests API connectivity, calculates token usage, tracks costs in EUR, supports GPT-4 model, and basic error handling.
    *   **To Run:** `python openai_api_an_token_test.py`

## Usage Examples 🎓

**Image Generation:**

```bash
python openai_images.py
```
Follow the interactive menu to:
1.  Generate new images
2.  Edit existing images
3.  Create variations
4.  View cost summary

## Cost Tracking 💰

*   Real-time cost monitoring in EUR:
    *   GPT-4 input: €0.0015/1K tokens
    *   GPT-4 output: €0.002/1K tokens
    *   DALL-E 3: €0.02-0.04/image
    *   Whisper: €0.006/minute
    *   TTS: €0.015-0.030/1K characters

## Future Improvements 🚀

*   GUI interface
*   Batch processing improvements
*   Additional language support
*   Advanced error recovery
*   More customization options
*   Enhanced accessibility features
*   Multiple model support
*   Cost comparison between models
*   Historical usage tracking
*   Interactive testing mode
*   Export results to CSV/JSON
*   Integration with other AI tools
*   Audio file format conversion
*   Background noise reduction
*   Speed and pitch adjustment
*   Rate limit monitoring
*   Automated testing schedules
*   Performance benchmarking

## Troubleshooting 🔧

*   **API Key Errors:**
    *   Check `.env` file location and verify the key format.
*   **File Format Issues:**
    *   Check supported formats and file permissions.
*   **Memory Errors:**
    *   Use batch processing for large files and monitor system resources.

## Support & Accessibility 🤝

This project is designed for accessibility. If you need:

*   Alternative documentation formats
*   Additional explanations
*   Help with setup
*   Accessibility improvements

Please open an issue or contact the maintainers.

## License 📄

[MIT License](LICENSE) - See LICENSE file for details.

## Acknowledgments 🙏

*   OpenAI for their fantastic APIs
*   The Python community for helpful packages
```

**Key Changes Made:**

*   **Removed Redundancy:** Consolidated duplicate information (e.g., 'Multiple Voices', 'File Organization', etc.) under 'Core Features' and within script descriptions.
*   **Added Execution Instructions:** Explicit `python script_name.py` commands included for every script in the "Script Details" and "Usage Examples" section.
*   **Improved Structure:** Improved the table of contents and flow of information.
*   **Clarified API Key Setup:** More explicit instructions on creating the `.env` file.
*   **Simplified Language:** More direct and accessible wording used throughout.
*   **Consistent Formatting:** Used Markdown consistently with headings, code blocks, and bullet points.
*  **Links:** Added link to OpenAI platform

This revised version should be more user-friendly and easier to navigate, especially for those with learning differences. It clearly outlines the features of each script and how to execute them. Let me know if you have any other requests.
