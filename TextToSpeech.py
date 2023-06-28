import pyttsx3
def speakingmodule(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
text = input("Enter the text: ")
speakingmodule(text)