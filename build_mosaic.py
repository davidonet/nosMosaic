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
        compose.append(current.set_pos((320 * x, 180 * y))
            .fadein(1)
            .fadeout(1)
            .set_start(x*1))


final = CompositeVideoClip(compose, size=(W, H))
final.write_videofile("final.mov",
                      codec="prores", ffmpeg_params=["-profile:v", "0"], fps=30)
