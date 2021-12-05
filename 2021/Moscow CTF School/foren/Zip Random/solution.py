from ctypes import CDLL
import time

libc = CDLL("libc.so.6")
secs=round(time.time())
file = list(open('flag.enc', 'rb').read())
while True:
    libc.srand(secs)
    res = file.copy()
    for i in range(0, len(file)):
        res[i] ^= libc.rand() % 255
    res = "".join(map(chr, res))
    if res.startswith("MSKCTF"):
        print(res)
        break
    secs -= 1