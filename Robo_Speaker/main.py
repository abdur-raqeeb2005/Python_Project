import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Abdur")
    while True:
        x = input("Enter what you want to speak: ")
        command = f"{x}"
        if x == "q":
            break
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()





    