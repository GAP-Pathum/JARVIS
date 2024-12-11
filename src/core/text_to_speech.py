import pyttsx3

def speak(text):
    """
    Converts text to speech and plays it.

    Args:
        text (str): The text to convert to speech.
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
