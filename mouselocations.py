import pyautogui

# کلیک را صورت بدهید
pyautogui.click()

# مختصات موس را دریافت کنید
x, y = pyautogui.position()
print(f"مختصات موس: x={x}, y={y}")