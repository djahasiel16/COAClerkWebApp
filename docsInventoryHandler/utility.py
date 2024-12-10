from pdf2image import convert_from_path
from PIL import Image


def create_pdf_thumbnail(pdf_path, first_page=1, thumbnail_size=(200,300)):
    images = convert_from_path(pdf_path, first_page=1, last_page=1)

    first_page_image = images[0]

    first_page_image.thumbnail(thumbnail_size)
    
    return first_page_image