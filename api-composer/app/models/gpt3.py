import openai
import os

class GPT3:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')  # Use environment variable for API key
        print(self.api_key)
        self.client = openai.OpenAI(api_key=self.api_key)  # Initialize the OpenAI client with the API key


    async def generate_text(self, prompt: str, max_tokens: int) -> str:
        try:
            response = self.client.completions.create(
                model="gpt-3.5-turbo-instruct",  # Use the correct model identifier
                prompt=prompt,
                # messages=[
                #     {"role": "system", "content": prompt},
                #     {"role": "user", "content": "Hello!"}
                # ],
                max_tokens=4000
            )
            return response.choices[0].text.strip()

        except Exception as e:
            print(f"Error generating text: {e}")    
            return "Error generating text."

