import time #Importing the module named time , it comes with python so no need to use "pip install time"
print("waiting for two seconds")
time.sleep(2) #Using a fumction from module time
print("waiting completed")
# '#' is comment 
import pyttsx3
engine = pyttsx3.init()
engine.say("Hi ")
engine.runAndWait()