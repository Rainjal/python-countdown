import time

def countdown(second_input):
    while second_input:
        minutes, seconds = divmod(second_input, 60)
        time_format = '{:02d}:{:02d}'.format(minutes, seconds)
        print(time_format)
        time.sleep(1)
        second_input -= 1

    print("stop")

time_input = int(input("Enter the Time in seconds: "))

countdown(time_input)
