from moviepy.editor import *
from random import *
import glob

yt = []
for filename in glob.iglob('convertYT/*.mov'):
    try:
        clip = VideoFileClip(filename)
        yt.append(clip)
    except Exception:
        print("Can't open: % s" % filename)

vt = sorted(yt, key=lambda v: v.duration)
pool = []
for v in vt:
    d = int(v.duration)
    print("%s : %d" % (v.filename, d))
    n = 0
    maxn = 10
    i = 3
    delta = d / 10
    while n < maxn:
        cut = min(i + randint(2, 6), d)
        print("cut : %d - %d" % (i, cut))
        pool.append(v.subclip(i, cut))
        i = i + delta
        n = n + 1

shuffle(pool)

for c in range(30):
    edl = []
    duration = 0
    while duration < 60:
        v = pool.pop()
        edl.append(v)
        duration = duration + v.duration
    final = concatenate_videoclips(edl)
    final.write_videofile("cvt_mosaic/t" + c.__str__() + ".mov",
                          codec="prores", ffmpeg_params=["-profile:v","0"])
