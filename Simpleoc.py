import easyocr as ocr

# Initialize the reader with English and Sinhala support
reader = ocr.Reader(['en'], model_storage_directory='.')

# Perform OCR on the image
result = reader.readtext("outliers.png")

# Print the detected text
for text in result:
    print(text[1])