import os
def say(text):
    os.command('mplayer "http://fanyi.baidu.com/gettts?lan=zh&text=' + text + '&source=web')

def handleSerialCmd(cmd):
    if cmd == 0x01:
        pass
