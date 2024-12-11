import speech_recognition as sr

def listen_for_commands():
    """
    Listens for speech from the user and converts it to text.

    Returns:
        str: The text converted from speech.
    """
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("Listening for commands...")

    try:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            print("Recognizing...")

        command = recognizer.recognize_google(audio)
        print(f"User said: {command}")
        return command.lower()

    except sr.UnknownValueError:
        print("Sorry, I could not understand that.")
        return None
    except sr.RequestError:
        print("Sorry, there was an issue with the speech service.")
        return None
