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
W, H = 1920, 960
compose = []
for x in range(6):
    for y in range(4):
        current = src[(4 * x) + y]
        start = x + randint(-5, 5) / 10.0
        scale = randint(80, 150) / 100.0
        compose.append(current.set_pos((320 * x + randint(-30, 30), 180 * y + randint(0, 60)))
                       .resize(width=320 * scale, height=180 * scale)
                       .set_start(start)
                       .fadein(.3)
                       .set_duration((60 - start) - (x * .5))
                       .fadeout(.5))


final = CompositeVideoClip(compose, size=(W, H), bg_color=(255, 0, 255))
final.write_videofile("mosaic.mov",
                      codec="prores", ffmpeg_params=["-profile:v", "3"], fps=30)
