from moviepy.editor import *
from random import *
import glob

src = []
for filename in glob.iglob('cvt_mosaic/*.mov'):
    try:
        clip = VideoFileClip(filename)
        src.append(clip)
    except Exception:
        print("Can't open: % s" % filename)
W, H = 1920, 720
compose = []
for x in range(6):
    for y in range(4):
        current = src[(4 * x) + y]
        start = .6*x + randint(-3, 3) / 10.0
        compose.append(current.set_pos((320 * x, 180 * y))
                       .set_start(start)
                       .fadein(.3)
                       .set_duration((30 - start) - (x * .5))
                       .fadeout(.5))


final = CompositeVideoClip(compose, size=(W, H)).subclip(0, 30)
final.write_videofile("mosaic.mov",
                      codec="prores", ffmpeg_params=["-profile:v", "0"], fps=30)
