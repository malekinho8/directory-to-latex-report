# This script should generate a PDF from a directory which is specifically a protocol directory. It should also be able to be run using CLI

# import modules
import os
import sys; sys.path.append('..'); sys.path.append('./')
import subprocess
import click
import pyperclip
from dir2pdf.utils import generate_latex

# specify click options
@click.command()
@click.option('--use-clipboard-for-input', '-c', is_flag=True, default=True, required=True, help='Use clipboard for input')
@click.option('--input-path', '-i', required=False, help='Path to the input protocol directory')
@click.option('--theme', '-t', required=False, default='MRL', help='Theme for the pdf')

def make_pdf(use_clipboard_for_input,input_path,theme):
    """Generate a PDF from a protocol directory."""
    if use_clipboard_for_input:
        input_path = pyperclip.paste()
    
    # obtain the latex code
    latex_path = generate_latex(input_path, theme)
        
    # compile the latex code to a pdf
    subprocess.call(['pdflatex', latex_path])

if __name__ == '__main__':
    make_pdf()