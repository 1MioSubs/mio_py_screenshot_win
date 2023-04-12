import mss.tools


with mss.mss() as sct:
    # The screen part to capture
    monitor = {"top": 0, "left": 0, "width": 600, "height": 600}
    output = "../test/sct-{top}x{left}_{width}x{height}.png".format(**monitor)

    # Grab the data
    sct_img = sct.grab(monitor)

    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    print(output)