from pyautogui import press
import time
from pygame import mixer
# pip install pyfiglet
import pyfiglet


def generatePrintableTime(seconds):
    minute = str(seconds // 60) if seconds // 60 > 9 else "0"+str(seconds // 60)
    second = str(seconds % 60) if seconds % 60 > 9 else "0"+str(seconds % 60)
    return "\t\t\t\t{} {} : {} {}".format(minute[0],minute[1], second[0],second[1])

def playAlarm(mixer):
    mixer.music.load('AlarmClock.mp3')
    mixer.music.play(2)

def stopOrEnd(mixer):
    mixer.music.stop()


def main():
    press('f11')
    while True:

        import os
        os.system('clear')
        os.system('clear')
        welcomePromt = pyfiglet.figlet_format("Welcome to timer App\n===========")
        print(8*"\t"+welcomePromt.replace("\n", "\n"+8*"\t")+3*"\n")
        userInputPromt = pyfiglet.figlet_format("Enter seconds\n")
        seconds = int(input(8*"\t"+userInputPromt.replace("\n", "\n"+8*"\t")))
        os.system('clear')

        timeRemaining = pyfiglet.figlet_format("Time Remaining\nM M : S S").replace("\n", "\n"+10*"\t")
        ascii_banner = pyfiglet.figlet_format(generatePrintableTime(seconds))
        print(25*"\n"+10*"\t"+timeRemaining+"\n"+10*"\t"+ascii_banner.replace("\n", "\n"+10*"\t"))
        time.sleep(1)
        for i in range(seconds):
            os.system('clear')
            ascii_banner = pyfiglet.figlet_format(generatePrintableTime(seconds-i-1))
            print(25*"\n"+10*"\t"+timeRemaining+"\n"+10*"\t"+ascii_banner.replace("\n", "\n"+10*"\t"))
            time.sleep(1)

        mixer.init()
        playAlarm(mixer)
        time.sleep(10)
        stopOrEnd(mixer)
        os.system('clear')
        os.system('clear')

        exitPromt = pyfiglet.figlet_format("You time is up\n===========\nEnter Q to exit")
        print(8*"\t"+exitPromt.replace("\n", "\n"+8*"\t")+3*"\n")
        #print("\n\n\t\t\tYou time is up.\n")

        if input(8*"\t") in ("Q","q"):
            os.system('clear')
            os.system('clear')
            press('f11')
            break
        else:
            continue



if __name__ == "__main__":
    main()
