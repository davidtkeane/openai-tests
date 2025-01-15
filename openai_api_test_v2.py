import openai

# Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
api_key = 'OPENAI_API_KEY'

openai.api_key = api_key

def check_openai_connection():
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can change the engine as needed
            prompt="This is a test prompt.",
            max_tokens=5
        )
        
        if 'choices' in response and len(response['choices']) > 0:
            print("Connection to OpenAI API successful!")
        else:
            print("Connection to OpenAI API failed. Unexpected response.")
            
    except openai.error.OpenAIError as e:
        print("Connection to OpenAI API failed. Error:", str(e))

if __name__ == "__main__":
    check_openai_connection()
