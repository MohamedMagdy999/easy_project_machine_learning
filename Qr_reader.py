import cv2

# a python library that will help us read the barcode and QR codes.
from pyzbar import pyzbar


def read_barcodes(frame):
    ''' send the frame that takes from camera and  #1 '''

    # Recognizing and decoding the barcode/QR code that we will be showing to the camera.
    barcodes = pyzbar.decode(frame)

    for barcode in barcodes:
        x, y, w, h = barcode.rect

        # 1
        # This helps us to see if our machine has detected the barcode/Qr code.
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0),
                      2)  # drawing a rectangle in frame

        # 2
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x+6, y-6),
                    font, 2.0, (255, 255, 255), 1)

        # 3
        with open("barcode_result.txt", mode="w") as file:
            file.write('Recognized Barcode:' + barcode_info)

    return frame


def main():
    # 1
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()

    while ret:
        ret, frame = camera.read()
        frame = read_barcodes(frame)

        cv2.imshow("Barcode / QR code reader ", frame)
        if cv2.waitKey(1) & 0xff == 27:
            break

    # 3
    camera.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
