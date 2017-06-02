from . import imagehash

import sys
from PIL import Image

_, method, cutoff, *files = sys.argv
cutoff = int(cutoff)

method = getattr(imagehash, method)

l = []

for f in files:
    h = method(Image.open(f))
    for ho, fo in l:
        d = ho - h
        if d <= cutoff:
            print (d,f,fo)
    l.append((h,f))

