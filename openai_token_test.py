import openai
from openai import OpenAI
import os
import requests

# Constants for costs
COST_PER_1K_INPUT = 0.0015    # GPT-4 input cost
COST_PER_1K_OUTPUT = 0.002    # GPT-4 output cost

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

os.system('cls' if os.name == 'nt' else 'clear')

# Print welcome banner
print("\nMade By David\nVersion 1.0.0\n")

model = "gpt-4"  # Changed from gpt-4o to gpt-4
prompt = "Create a function that takes a list of strings and returns the longest string in the list."

def get_openai_response(model, prompt):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=2048
        )
        
        # Calculate tokens
        prompt_tokens = response.usage.prompt_tokens
        completion_tokens = response.usage.completion_tokens
        total_tokens = response.usage.total_tokens
        
        # Calculate costs in USD
        prompt_cost = (prompt_tokens / 1000) * COST_PER_1K_INPUT
        completion_cost = (completion_tokens / 1000) * COST_PER_1K_OUTPUT
        total_cost_usd = prompt_cost + completion_cost
        
        # Convert to EUR (using approximate rate)
        total_cost_eur = total_cost_usd * 0.93
        
        print(f"\nToken Usage:")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Completion tokens: {completion_tokens}")
        print(f"Total tokens: {total_tokens}")
        print(f"Cost: €{total_cost_eur:.4f}")
        
        return response.choices[0].message.content
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def ping_openai():
    try:
        response = get_openai_response(model, "Hello!")
        if response:
            print("\nOpenAI API is responding!")
            return True
        return False
    except Exception as e:
        print(f"\nError connecting to OpenAI: {str(e)}")
        return False

if __name__ == "__main__":
    ping_openai()