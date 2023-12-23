from struct import *

FILEIN = 'code_text.txt'
FILEOUT = 'decoded_text.txt'
KEY = 113

f1 = open(FILEIN, 'rb')
f2 = open(FILEOUT, 'wb')

b_st = f1.read()

for x in b_st:
    x = int(x)
    y = (x - KEY) % 255
    b_y = pack('B', y)
    f2.write(b_y)

f1.close()
f2.close()
