import pyscreenshot


image = pyscreenshot.grab()
image.save("../test/pyscreenshot_full.png")

image = pyscreenshot.grab(bbox=(0, 0, 600, 600))
image.save("../test/pyscreenshot_sell.png")