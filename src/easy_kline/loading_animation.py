'''
This function use for made liding animation 
'''
import time
import sys


def loading_animation(text, time_loading: int = 5):
    # Characters to use for animation
    chars = ['⣿', "⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿", '⣿']
    start_time = time.time()  # start time

    while time.time() - start_time < time_loading:  # time condition
        for char in chars:
            # Print the current character
            sys.stdout.write(
                f'\r {text}  {char} ')
            time.sleep(0.1)  # Wait for a short amount of time
    time.sleep(1)  # Wait for a short amount of time
