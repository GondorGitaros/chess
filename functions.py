import win32api
import win32con

SCAN_X, SCAN_Y = 1864, 93

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def scan():
    click(SCAN_X, SCAN_Y)
    