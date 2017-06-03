from . import imagehash

import sys
from PIL import Image


if len(sys.argv) > 2:
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

else:
    f = sys.argv[1]
    i = Image.open(f)
    for n in 'average_hash','dhash':
        c = getattr(imagehash, n)
        if callable(c):
            print(n, c(i))
