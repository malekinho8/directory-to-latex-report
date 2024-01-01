# import modules
import os
import sys; sys.path.append('..'); sys.path.append('./')
import subprocess
import pyFormal
from pillow_heif import register_heif_opener
from PIL import Image
from PIL.ExifTags import TAGS

register_heif_opener()

def generate_latex_files(input_path, theme):
    # 

def generate_latex(input_path, theme):
    """Generate the latex codes, save them to files, and then output the paths to the files."""
    # get the input directory name
    input_dir_name = os.path.basename(input_path)

    # get the list of files in the input directory
    file_list = os.listdir(input_path)

    # sort the file list
    file_list.sort()

    # generate the latex code
    latex_code = f''

    # add the preamble to the latex code depending on the theme
    latex_code += generate_preamble(theme)

    # for every slide we create, we will need to add label to the slide with \label{slide:folder name} and also add labels to the figure and table environments with \label{fig:folder name} and \label{tab:folder name} for future reference as needed.
    
    # if there is only a readme or reference text file in the folder and no image or pdf

    # if the text file is a readme:
    # if the text file has enumerated lines, then dont use the center environment when converting to latex code
    # if the text file has unenumerated lines, then use the center environment when converting to latex code

    # if the text file is a reference:
    # if a text file name is reference.txt then access the contents of the folder and render them into the latex code as if it were the current folder
    # whenever using a reference, we should add a frame at the beginning that has a centered note saying that the following steps are from the reference and explain what folder the reference is from

    # otherwise if there is 1 image or pdf in the folder, then proceed
    # if there is no readme or reference text file in the folder, then proceed
    # obtain the image description metadata
    # convert the image description metadata and image into a beamer frame and add it to the latex code
    # however if there is a readme or reference text file in the folder, then use the contents of the readme or reference text file as the image description metadata
    # convert the image description metadata and image into a beamer frame and add it to the latex code

    # if there is more than 1 image or pdf in the folder, then proceed

def generate_preamble(theme):
    """Generate the preamble for the latex code."""
    if theme == 'MRL':
        # read from the beamerthemeMRL.sty file
        with open('themes/beamerthemeMRL.sty', 'r') as f:
            preamble = f.read()
    return preamble

def compile_pdfs(latex_paths: list):
    """Compile a list of latex paths to pdfs."""
    for latex_path in latex_paths:
        compile_pdf(latex_path)

def compile_pdf(latex_path):
    """Compile the latex code to a pdf."""
    # compile the latex code to a pdf
    subprocess.call(['pdflatex', latex_path])

def get_jpeg_image_description(image_path):
    """Get the image description metadata from an image."""
    # Load your JPEG image
    image = Image.open(image_path)

    # Extract EXIF data
    exif_data = image._getexif()
    
    return find_metadata_description(exif_data)

def get_heic_image_description(image_path):
    """Get the image description metadata from an image."""
    # Load your JPEG image
    image = Image.open(image_path)

    # Extract EXIF data
    exif_data = image.getexif()

    return find_metadata_description(exif_data)

def find_metadata_description(exif_data):
    """Find the metadata description in the exif data."""
    # The EXIF data is a dictionary where keys are numeric codes for different types of metadata
    # We need to translate these codes to human-readable form and search for the description
    if exif_data:
        for tag_id in exif_data:
            # Translate tag
            tag = TAGS.get(tag_id, tag_id)

            # Extract data
            data = exif_data.get(tag_id)

            # Check if this is the description tag
            # The exact tag name depends on how the description is stored; it might be 'ImageDescription', 'UserComment', etc.
            if tag == 'ImageDescription':  # Replace with the correct tag as per your image's metadata
                return data
    else:
        return "No EXIF data found"