from pdf2docx import Converter

def convert_pdf_to_word(pdf_path):
    word_path = pdf_path.replace('.pdf', '.docx')

    cv = Converter(pdf_path)
    cv.convert(word_path, start=0, end=None)
    cv.close()

<<<<<<< HEAD
    return word_path
=======
    return word_path
>>>>>>> 6c2842b29cf13421fdb42d1172bc248abdb39e80
