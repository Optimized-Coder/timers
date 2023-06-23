from datetime import time
import time as pause


def start_timer(hours, minutes, seconds):
    '''
    Function: decrements time object at a 1 second interval
    Parameters: hours, minutes, seconds (int)
    Returns: None
    '''
    t = time(hours, minutes, seconds)
    print(t)
    pause.sleep(1)
    while not t == time(0, 0, 0):
        # decrement time while time is greater than 00:00:00
        if t.second > 0:
            t = t.replace(second=t.second-1)
        elif t.minute > 0:
            t = t.replace(minute=t.minute-1)\
                .replace(second=59)
        elif t.hour > 0:
            t = t.replace(hour=t.hour-1)\
                .replace(minute=59)\
                .replace(second=59)
        # print out decremented time at a 1 second interval
        print(t)
        pause.sleep(1)
    print("Time Up!")


if __name__ == "__main__":
    start_timer(1, 0, 10)
