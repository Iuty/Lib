from ctypes import *


user32 = windll.user32
kernel32 = windll.kernel32
def get_clipboard():
    user32.OpenClipboard(c_int(0))
    contents = c_char_p(user32.GetClipboardData(c_int(1))).value
    user32.CloseClipboard()
    str_contents = str(contents,encoding = 'gbk')
    return str_contents


if __name__ == '__main__':
	print(get_clipboard())