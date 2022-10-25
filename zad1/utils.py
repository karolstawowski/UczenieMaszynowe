import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program ' \
                                        r'Files\Tesseract-OCR\tesseract '


def convert_image_to_string(image_path: str) -> str:
    img = cv2.imread(image_path)
    return pytesseract.image_to_string(img)
