from mss import mss


with mss() as sct:
    filename = sct.shot(mon=0, output='../test/fullscreen.png')
    print(filename)

