import pyautogui
script ="insert the words here"


for x in script.split():
    pyautogui.write(x)
    pyautogui.press("Enter")
