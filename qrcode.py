#pip install pyqrcode

import pyqrcode


def qrcode():
    q=pyqrcode.create(input())
    q.png('qrcode.png', scale=6)
    print('QR Code Generated Successfully!')


if __name__=='__main__':
    qrcode()
