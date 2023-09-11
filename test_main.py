"""
This test tests if the barplot generated is a PNG image

"""
from PIL import Image

def is_valid_png(file_path):
    try:
        img = Image.open(file_path)
        img.verify()
        return True
    except (IOError, SyntaxError):
        return False


file_path = "djl_project2/source/bar_plot.png"
if is_valid_png(file_path):
    print("The image is valid PNG image.")
else:
    print("The image is not valid PNG image.")

