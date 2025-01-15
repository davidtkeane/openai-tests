#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by: Ranger
# Created on: 08/08/2021
# Version: 1.0.0 (Tested on Python 3.8)
# Usage: python openai-token.py

# This script demonstrates how to get token usage for a given prompt using the OpenAI API.

# Set up your OpenAI API key
# 1 - Set up your OpenAI API key in your environment variables or directly in your code.
# 2 - Replace 'your_api_key' with your actual API key.
# 3 - Ensure that your environment variable is set correctly or directly in your code. For example:
# 4 - Enter the following command in your terminal: export OPENAI_API_KEY="your_api_key"
#     
# Alternatively, you can set the API key directly in your code as shown below.
# Set up your OpenAI API key in your environment variables or directly in your code.
# os.environ["OPENAI_API_KEY"] = "your_api_key"

from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = "OPENAI_API_KEY"

@app.route("/api/openai", methods=["POST"])
def openai_chat():
  # Get the message from the request body
  message = request.json["message"]

def generate_response(message):
  # Use the OpenAI API to generate a response
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"User: {message}\nOpenAI: ",
    temperature=0.5,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["\n"]
  )
  
  # Return the response as JSON
  return jsonify({"response": response.text})

if __name__ == "__main__":
  app.run()
