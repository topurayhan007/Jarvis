import pyttsx3
import datetime
 
curr_time = datetime.datetime.now()
time = curr_time.strftime("%H")

str = ""
if(time < '12'):
    str = "Good Morning"
elif('12'<= time < '17'):
    str = "Good Afternoon"
elif(time >= '17'):
    str = "Good Evening"

talko = pyttsx3.init()

output = "Welcome back Sir! "+ str
text = (output)

voices = talko.getProperty('voices')
talko.setProperty('voice', voices[0].id)

reading_speed = 130
talko.setProperty('rate', reading_speed)

talko.say(text)
print(output)
talko.runAndWait()