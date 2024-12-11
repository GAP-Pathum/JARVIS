#src/apo/gemini_api.py
import requests
import json

class GeminiAPI:
    def __init__(self, api_key):
        """
        Initialize the GeminiAPI client.

        Args:
            api_key (str): Your API key for authentication.
        """
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models"
        self.api_key = api_key

    def generate_content(self, model, prompt):
        """
        Generate content using the Gemini Generative Language API.

        Args:
            model (str): The model to use (e.g., "gemini-1.5-flash-latest").
            prompt (str): The text prompt to send to the API.

        Returns:
            dict: The API response containing the generated content.
        """
        url = f"{self.base_url}/{model}:generateContent?key={self.api_key}"
        headers = {
            "Content-Type": "application/json"
        }
        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt}
                    ]
                }
            ]
        }
        
        try:
            response = requests.post(url, headers=headers, data=json.dumps(payload))
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error during API call: {e}")
            return None

# Example usage:
if __name__ == "__main__":
    API_KEY = "AIzaSyBApv0M03F8yvcqESAzRlByjjCdHmsD-zo" 
    gemini = GeminiAPI(api_key=API_KEY)

    # Test generating content
    model = "gemini-1.5-flash-latest"
    prompt = "Explain how AI works"
    response = gemini.generate_content(model, prompt)
    
    if response:
        print("Generated Response:")
        print(json.dumps(response, indent=2))
    else:
        print("Failed to generate content.")
