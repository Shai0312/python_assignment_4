import time

def countdown(seconds):
    mins = seconds // 60
    secs = seconds % 60
    print(f'{mins:02d}:{secs:02d}', end="\r")
    time.sleep(1)
    seconds -= 1
    if seconds >= 0:
        countdown(seconds)
    else:
        print("Time's up!")

if __name__ == "__main__":
    countdown(10)  