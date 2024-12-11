from api.gemini_api import GeminiAPI
from core.speech_recognition import listen_for_commands
from core.text_to_speech import speak
from datetime import datetime
import os
from dotenv import load_dotenv

def get_greeting():
    """Determine the appropriate greeting based on the time of day."""
    hour = datetime.now().hour
    if hour < 12:
        return "Good morning"
    elif 12 <= hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"

def main():
    # Load environment variables from the .env file
    load_dotenv()

    # Get the API key from the environment variable
    API_KEY = os.getenv("GEMINI_API_KEY")
    if not API_KEY:
        raise ValueError("API key not found. Please set the GEMINI_API_KEY in the .env file.")

    # Initialize GeminiAPI
    api = GeminiAPI(API_KEY)

    print("Listening for commands...")

    # Greeting state flag
    greeted = False

    while True:
        try:
            # Get user command
            command = listen_for_commands().lower()
            
            if command == "exit":
                speak("Goodbye sir... If you need me I'll be here.")
                break

            # Handle initial greeting
            if not greeted:
                if "hello jarvis" in command:
                    greeting = get_greeting()
                    response = f"{greeting} Pethum. All systems are fully operational and ready at your command."
                    print("JARVIS:", response)
                    speak(response)
                    greeted = True  # Allow further commands after the greeting
                else:
                    speak("Please say 'Hello JARVIS' to begin.")
                continue  # Wait for the correct greeting
            
            # Process other commands after greeting
            model = "gemini-1.5-flash-latest"  # Set the model to be used
            response = api.generate_content(model, command)

            if response:
                # Print the full response to understand its structure
                print("Full API Response:", response)
                
                # Try to extract the response text
                response_text = response.get('contents', [{}])[0].get('parts', [{}])[0].get('text', None)
                
                if response_text:
                    print("JARVIS:", response_text)
                    speak(response_text)
                else:
                    print("JARVIS: Sorry, no valid response content found.")
                    speak("Sorry, no valid response content found.")
            else:
                print("JARVIS: Sorry, I couldn't get a response from the API.")
                speak("Sorry, I couldn't get a response from the API.")
        
        except Exception as e:
            print(f"An error occurred: {e}")
            speak("Sorry, I encountered an error.")

if __name__ == "__main__":
    main()
