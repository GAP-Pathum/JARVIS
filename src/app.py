from api.gemini_api import GeminiAPI
from core.speech_recognition import listen_for_commands
from core.text_to_speech import speak
from datetime import datetime

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
    # Your API key (from .env)
    API_KEY = ""

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
            response_data = api.generate_content("gemini-1.5-flash-latest", command)
            
            # Extracting the generated response text from the API response
            if response_data and 'candidates' in response_data:
                response_text = response_data['candidates'][0]['content']['parts'][0]['text']
                print("JARVIS:", response_text)
                speak(response_text)  # Speak the response text
            else:
                response_text = "Sorry, I couldn't get a response from the API."
                print("JARVIS:", response_text)
                speak(response_text)

        except Exception as e:
            print(f"An error occurred: {e}")
            speak("Sorry, I encountered an error.")

if __name__ == "__main__":
    main()
