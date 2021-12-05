from ctypes import CDLL

libc = CDLL("libc.so.6")
secs = 1638033382
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