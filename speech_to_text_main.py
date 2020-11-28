import speech_recognition

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    audio = recognizer.listen(source)
    captured_text = recognizer.recognize_google(audio, language="en-in")

print(captured_text)