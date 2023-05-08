import pyttsx3
from PyPDF2 import PdfReader


def speak_init():
    """
    Initializes a text-to-speech engine and sets the speaking rate to 205.
    Returns:
        pyttsx3.engine.Engine: The text-to-speech engine object.
    """
    engine = pyttsx3.init()
    rate = engine.getProperty("rate")  # getting details of current speaking rate
    print(rate)  # printing current voice rate
    engine.setProperty("rate", 205)  # setting up new voice rate
    return engine


def read_pdf(location):
    """
    Reads the content of a PDF file.
    Args:
        location (str): The file path of the PDF file to read.
    Returns:
        PyPDF2.pdf.PdfFileReader: The PDF reader object.
    """
    reader = PdfReader(location)
    return reader


def text_of_page(reader, page_no):
    """
    Extracts the text content of a specific page of a PDF file.
    Args:
        reader (PyPDF2.pdf.PdfFileReader): The PDF reader object.
        page_no (int): The page number of the PDF file to extract text from.=
    Returns:
        str: The text content of the specified page of the PDF file.
    """
    page = reader.pages[page_no]
    text = page.extract_text()
    return text


def speak(text):
    """
    Speaks out the given text using a text-to-speech engine.
    Args:
        text (str): The text to be spoken out.
    Returns:
        None
    """
    engine = speak_init()
    engine.say(text)
    engine.runAndWait()


reader = read_pdf("ONeill_WeaponsMathDestruct_30pages.pdf")
text = text_of_page(reader=reader, page_no=4)
print(text)
speak(text=text)
