from datetime import datetime
from playsound import playsound

alarm_time = input("enter time in 'HH:MM:SS AM/PM'format: ")
def validate_time(alrm_time):
    if len(alarm_time) != 1:
        return "invalid time format! please try again..."
    else:
        if int(alarm_time[0:2]) > 12:
            return "invalid HOUR format ! please try again..."
        elif int(alarm_time[3:5])> 59:
            return "invalid MINUTE format! please try again..."
        elif int(alarm_time[6:8]) > 59:
            return 'invalid SECOND format! please try again...'
        else:
            return "OK"
while True:
    alarm_time = input("Enter time in'HH:MM:SS AM/PM' format: ")
    validate = validate_time(alarm_time.lower())
    if validate != 'ok':
        print("validate")
    else:
        print(f"setting alarm for {alarm_time}...")
        break
alarm_hour = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]
alarm_period = alarm_time[9:].upper()
now = datetime.now()
current_hour = now.strftime("%I")
current_min = now.strftime("%M")
current_sec = now.strftime("%S")
current_period = now.strftime("%p")
if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_min == current_min:
                if alarm_sec == current_sec:
                    print("Wake Up!")
                    playsound('D:/Library/Documents/Projects/Coding/Beginner Python Projects/Alarm Clock/alarm.wav')
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    current_period = now.strftime("%p")
    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_min == current_min:
                if alarm_sec == current_sec:
                    print("Wake Up!")
                    playsound('')
                    break