import pyttsx3

if __name__ == '__main__':
    print("Welcome to roboSpeaker1.0 created by srijan")
    while True:
        x = input("Enter what u want me to speak")
        if  x=="q":
            break

        engine = pyttsx3.init()
        engine.say(x)
        engine.runAndWait()
