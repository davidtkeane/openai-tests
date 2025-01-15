#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Created by: Ranger
# Created on:10/01/2025
#
# Version: 1.0.0 (Tested on Python 3.8)
# Usage: python openai-token.py

# This script provides a simple example of how to use the OpenAI API to generate a chat response.

# Set up your OpenAI API key
# 1 - Set up your OpenAI API key in your environment variables or directly in your code.
# 2 - Replace 'your_api_key' with your actual API key.
# 3 - Ensure that your environment variable is set correctly or directly in your code. For example:
# 4 - Enter the following command in your terminal: export OPENAI_API_KEY="your_api_key"
#     
# Alternatively, you can set the API key directly in your code as shown below.
# Set up your OpenAI API key in your environment variables or directly in your code.
# os.environ["OPENAI_API_KEY"] = "your_api_key"


# Import necessary libraries
import os
from openai import OpenAI

# Create an instance of the OpenAI class
os.environ["OPENAI_API_KEY"] = "your_api_key"

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)

# Print the output
print(chat_completion.choices[0].message.content)

