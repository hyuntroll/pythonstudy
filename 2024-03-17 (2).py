import pyautogui
import time
import pyperclip

pyautogui.moveTo(1423, 219, 0.2)
pyautogui.click()
time.sleep(0.5)

pyautogui.click()
pyperclip.copy("서울 날씨")
pyautogui.hotkey("ctrl", "v")
time.sleep(0.5)

pyautogui.write(["enter"])
time.sleep(1)

start = {'x': 993, 'y': 275}
end = {'x': 1656, 'y': 692}

pyautogui.screenshot('img/seuol.png', region=(start['x'], start['y'], end['x'] - start['x'], end['y'] - start['y']))

while True:
    print(pyautogui.position())
    time.sleep(0.1)
