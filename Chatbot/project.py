import speech_recognition as sr
import pyttsx3




engine = pyttsx3.init()
engine.setProperty('rate',0.7)
engine.setProperty('volume',1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1])


def speak(text):
    engine.say(text)
    engine.runAndWait()
    
    
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Mendengarkan....")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            print(f"Kamu: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I cant Hear you")
            return""
        except sr.RequestError:
            print("please,reapet your voice")
            return""
        
def jarvis_command(command):
    speak("Halo sir,")
    
    if "how are you" in command:
        speak("i am fine sir,thank you")
    



def main():
    while True:
        command = listen()
        if "jarvis" in command:
            response = jarvis_command(command)
            print(f"jarvis: {response}")
            speak(response)
            if "mati" in response:
                break
            
            
            
if __name__ == "__main__":
    main()