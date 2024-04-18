from pathlib import Path

'''
Loads assets from their relevant project folders.

This syntax is made possible by the pathlib module, which is part of the standard library in Python 3.4 and above. 
The operator simplifies the construction of file paths by handling various operating system path idiosyncrasies 
automatically.
'''
class AssetManager:
    def __init__(self):
        # Path Settings
        # Navigate up to the project root first if necessary
        self.__base_dir = Path(__file__).resolve().parent.parent
        self.__css_file = self.__base_dir / "style" / "main.css"
        self.__resume_file = self.__base_dir / "assets" / "cv.pdf"
        self.__profile_pic = self.__base_dir / "assets" / "cv_img.png"

    def get_css(self):
        with open(self.__css_file) as f:
            return f.read()

    def get_resume(self):
        with open(self.__resume_file, "rb") as pdf_file:
            return pdf_file.read()

    def get_profile_pic(self):
        return self.__profile_pic

    def get_resume_filename(self):
        return self.__resume_file
