import aspose.slides as slides
import aspose.pydrawing as drawing
import pathlib
import os
from PIL import Image

# Load presentation
pres = slides.Presentation("presentation.pptx")

class SlidesConverter:

        def __init__(self, presentation):

            self.presentation = presentation

        def convert(self, presentation):

            new_dir_name = input('presentation slides')
            new_dir = pathlib.Path('C:\Users\hamza\PycharmProjects\PresentationTool', new_dir_name)
            new_dir.mkdir(parents=True, exist_ok=True)
            # You have to make a file inside the new directory

            for index in range(pres.slides.length):
                # Get reference of slide
                slide = pres.slides[index]

                # Save as JPG
                img=slide.get_thumbnail().save("{i}.jpg".format(i=index), drawing.imaging.ImageFormat.jpeg)

                for filename in os.listdir(new_dir):
                    img = Image.open(os.path.join(new_dir, filename))  # images are color images
                    img = img.resize((1280,720), Image.ANTIALIAS)
                    img.save(new_dir + new_dir_name + '.jpeg')

