from rapidocr_onnxruntime import RapidOCR

# Initialize OCR only once
ocr = RapidOCR()


def read_bill(path):
    """
    Reads a grocery bill image and returns extracted text.
    """

    result, _ = ocr(path)

    text = ""

    if result:
        for item in result:
            # item = [box, text, confidence]
            text += item[1] + "\n"
    print(text)
    return text