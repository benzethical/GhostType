import pyautogui
import time

type = input(f'Enter what you want to type: ')
delay = int(input('Enter the delay before typing (seconds): '))
pressenter = input('Do you want to press enter after typing? (y/n): ')

if pressenter == "y":
    print(f'Starting typing in {delay} seconds -->')
    time.sleep(delay)

    while True:
        pyautogui.write(type, interval=0.05)
        pyautogui.press('enter')
        time.sleep(1)

elif pressenter == 'n':
    print(f'Starting typing in {delay} seconds -->')
    time.sleep(delay)

    while True:
        pyautogui.write(type, interval=0.05)

else:
    print('Invalid input')