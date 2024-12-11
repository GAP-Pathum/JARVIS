# 🧑‍💻 **JARVIS: The Python-Based Voice Assistant** 🧑‍💻

Welcome to **JARVIS**, a cutting-edge voice assistant built in Python that integrates the **Gemini API** to generate intelligent responses. This app uses speech recognition and text-to-speech technology, allowing you to control the assistant via voice commands such as asking about the weather, setting reminders, or simply having a chat.

---

## 🌟 **Features**:
- **Voice Interaction**: Control JARVIS with your voice! 🗣️
- **Gemini API Integration**: Smart and dynamic responses from Gemini. 🤖
- **Speech Recognition**: Converts your voice into commands. 🎤
- **Text-to-Speech**: JARVIS speaks back to you! 🗣️
- **Greeting System**: Personalized greeting based on the time of day. 🌅
- **Weather and Jokes**: Ask JARVIS for the weather or a joke! ☀️🌧️😂
- **Exit Command**: Easily exit by saying "exit". 👋

---

## 🛠 **Tech Stack**:

- **Python** 🐍
- **Gemini API** 🌐
- **Speech Recognition** 🎙️
- **pyttsx3 (Text-to-Speech)** 🗣️
- **python-dotenv** 🔒
- **requests** 🔌

---

## 🚀 **Getting Started**:

### 1. **Clone the Repository**:
Clone the repository to your local machine:
```bash
git clone https://github.com/GAP-Pathum/JARVIS.git
cd JARVIS
```

### 2. **Install Dependencies**:
Install the required libraries using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 3. **Set Up the .env File**:
Create a `.env` file in the `src/` directory with your **Gemini API Key**:
```plaintext
GEMINI_API_KEY=your_api_key_here
```

### 4. **Run the Application**:
To start the assistant, simply run the `app.py` script:
```bash
python src/app.py
```

---

## 🏃‍♂️ **How It Works**:

1. **Wake Up JARVIS**:
   The assistant waits for you to say **"Hello Jarvis"** to wake up.

2. **Greeting**:
   Once activated, JARVIS greets you based on the time of day:
   - **"Good morning, Sir. All systems are fully operational!"**
   - **"Good evening, Sir. How can I assist you tonight?"**

3. **Command Processing**:
   After the greeting, you can ask JARVIS anything, like:
   - **"What's the weather today?"** 🌦️
   - **"Tell me a joke!"** 😂
   - **"Exit"** to stop the assistant. 🛑

4. **Response**:
   JARVIS processes the command via Gemini API and speaks the response aloud. 🎧

5. **Exit Command**:
   Say **"Exit"** and JARVIS will end the session with a farewell message. 👋

---

## 📁 **Folder Structure**:

```bash
JARVIS/
│
├── src/
│   ├── api/
│   │   └── gemini_api.py          # Functions for interacting with the Gemini API
│   ├── core/
│   │   ├── speech_recognition.py  # Converts speech to text
│   │   └── text_to_speech.py      # Converts text to speech
│   ├── .env                       # Store environment variables (API_KEY)
│   └── app.py                     # Main application script
└── requirements.txt               # List of dependencies
```

---

## 🔧 **Dependencies**:

- `requests` 🌐: For API requests to Gemini.
- `pyttsx3` 🎤: To convert text into speech.
- `speech_recognition` 🎙️: For recognizing voice commands.
- `python-dotenv` 🔒: To load your API key securely.

---

## 📸 **Screenshots**:

### **Greeting Screen**:
![Greeting](https://via.placeholder.com/500x300?text=Greeting+Message)

---

## 📝 **To Do**:

- 🎯 **Additional Features**: Add functionality like setting reminders or controlling IoT devices.
- 🛠️ **Error Handling**: Improve handling for API or network issues.
- 🌍 **Multiple Languages**: Expand the assistant to support other languages.

---

## 👨‍💻 **Contributing**:

Feel free to fork the repository and submit pull requests to improve the assistant!

1. Fork the repo.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

---

## ✨ **License**:

This project is open-source and licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

## 👋 **Acknowledgements**:

- **Gemini API**: For providing powerful responses to user queries.
- **Google's Speech Recognition**: For converting speech to text.
- **pyttsx3**: For converting text back into speech!

---

## 💡 **Let's make JARVIS smarter together! 🚀**

---
```
