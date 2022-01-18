import cv2
import pytesseract

from status_pod.app.config import config


pytesseract.pytesseract.tesseract_cmd = config.TESSERACT_PATH


image = cv2.imread('shot.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
threshold_img = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

custom_config = r'--oem 3 --psm 6'
details = pytesseract.image_to_data(
    threshold_img,
    output_type=pytesseract.Output.DICT,
    config=custom_config,
    lang='eng'  # TODO добавить русский
)

print(details)
