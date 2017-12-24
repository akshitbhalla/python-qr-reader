import zbarlight

from PIL import Image
import cv2


def main():

    # Begin capturing video
    capture = cv2.VideoCapture(0)

    while True:
        # To quit this program press q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Breaks down the video into frames
        ret, frame = capture.read()

        # Displays the current frame
        cv2.imshow('Current', frame)

        # Converts image to grayscale.
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Uses PIL to convert the grayscale image into an array that zbarlight can understand.
        pil_im = Image.fromarray(gray)

        # Scans the zbarlight image.
        codes = zbarlight.scan_codes('qrcode', pil_im)

        # Prints data from image.
        print('QR codes: %s' % codes)

if __name__ == "__main__":
    main()
