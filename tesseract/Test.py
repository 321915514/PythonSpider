
import pytesseract
import time
from urllib import request
from PIL import Image


def main():
    pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'
    while True:
        time_stamp = int(time.time())
        url = 'http://47.103.204.177/BookStore/Vcode?a=%d' % time_stamp
        request.urlretrieve(url, 'captcha.png')
        image = Image.open('captcha.png')
        text = pytesseract.image_to_string(image)
        print(text)
        time.sleep(2)


if __name__ == '__main__':
    main()
