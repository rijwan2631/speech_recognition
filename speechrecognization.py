import speech_recognition as sr

# Create a Recognizer object
listener = sr.Recognizer()

# Use the microphone as the input source
with sr.Microphone() as input_source:
    print("I am listening...")
    # Listen for audio from the microphone
    voice_input = listener.listen(input_source)
    try:
        # Use Google's speech recognition API to recognize the speech
        text = listener.recognize_google(voice_input)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError:
        print("Sorry, I couldn't connect to the speech recognition service.")