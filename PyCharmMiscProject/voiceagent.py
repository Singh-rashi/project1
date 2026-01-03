"""
SmartCare AI - Voice Agent
Author: Rashi
Role: NLP + Voice Agent

Requires:
pip install SpeechRecognition
pip install pyttsx3
pip install requests
pip install pyaudio   (for mic)
"""

import speech_recognition as sr
import pyttsx3
import requests

# ---------------------------
# Initialize modules
# ---------------------------
listener = sr.Recognizer()
engine = pyttsx3.init()

# ---------------------------
# Speak function
# ---------------------------
def speak(text):
    print("Bot:", text)
    engine.say(text)
    engine.runAndWait()


# ---------------------------
# Listen function
# ---------------------------
def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            text = listener.recognize_google(voice)
            text = text.lower()
            print("User:", text)
            return text
    except:
        speak("Sorry, I couldn't hear clearly.")
        return ""


# ---------------------------
# Emotion Detection
# ---------------------------
def detect_emotion(sentence):
    angry_words = ["angry", "complain", "bad", "worst", "frustrated"]
    happy_words = ["thanks", "good", "great", "excellent"]

    for word in angry_words:
        if word in sentence:
            return "frustrated"

    for word in happy_words:
        if word in sentence:
            return "happy"

    return "neutral"


# ---------------------------
# Intent Recognition
# ---------------------------
def detect_intent(text):

    if "problem" in text or "issue" in text or "vibration" in text:
        return "report_fault"

    if "schedule" in text or "book" in text or "appointment" in text:
        return "schedule_service"

    if "cancel" in text:
        return "cancel_schedule"

    if "status" in text or "health" in text:
        return "machine_health"

    return "unknown"


# ---------------------------
# API calls to Backend
# ---------------------------
BASE_URL = "http://127.0.0.1:5000"     # Change if needed

def send_api_request(intent):

    if intent == "report_fault":
        r = requests.get(BASE_URL + "/predict")
        return r.text

    if intent == "schedule_service":
        r = requests.get(BASE_URL + "/schedule")
        return r.text

    if intent == "cancel_schedule":
        r = requests.get(BASE_URL + "/cancel")
        return r.text

    if intent == "machine_health":
        r = requests.get(BASE_URL + "/status")
        return r.text

    return "Sorry, I cannot process that request."


# ---------------------------
# MAIN LOOP
# ---------------------------
def main():

    speak("Welcome to SmartCare AI Voice Assistant. How may I help you today?")

    while True:

        text = listen()
        if text in ["exit", "quit", "bye"]:
            speak("Goodbye! Take care.")
            break

        emotion = detect_emotion(text)
        intent = detect_intent(text)

        print(f"Detected Emotion: {emotion}")
        print(f"Detected Intent: {intent}")

        if intent == "unknown":
            speak("Sorry, can you please rephrase?")
            continue

        result = send_api_request(intent)

        speak(result)


if __name__ == "__main__":
    main()
