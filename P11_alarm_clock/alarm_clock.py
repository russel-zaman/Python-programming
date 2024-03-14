import os
import time
import pygame

def play_alarm_sound():
    pygame.mixer.init()
    alarm_sound_file = "D:\Lern something\Python-programming\P11_alarm_clock/alarm_sound.wav"
    pygame.mixer.music.load(alarm_sound_file)
    pygame.mixer.music.play()

def simple_clock(minutes=None, seconds=None, alarm_time=None):
    if minutes is None and seconds is None and alarm_time is None:
        print("Please provide either minutes, seconds, or alarm time.")
        return

    if alarm_time:
        alarm_hour, alarm_minute = map(int, alarm_time.split(':'))
        while True:
            current_time = time.localtime()
            if current_time.tm_hour == alarm_hour and current_time.tm_min == alarm_minute:
                print("Time's up!")
                play_alarm_sound()
                break
            time.sleep(1)

    else:
        total_seconds = 0
        if minutes:
            total_seconds += minutes * 60
        if seconds:
            total_seconds += seconds

        print(f"Alarm set for {total_seconds} seconds from now.")
        time.sleep(total_seconds)
        print("Time's up!")
        play_alarm_sound()

if __name__ == "__main__":
    alarm_time_input = input("Please enter the alarm time (HH:MM): ")
    simple_clock(alarm_time=alarm_time_input)
