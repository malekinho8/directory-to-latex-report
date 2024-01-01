import click
import pyperclip
import sys; sys.path.append('..'); sys.path.append('./')
from utils import compile_pdfs, generate_latex_files

@click.command()
@click.option('--use-clipboard-for-input', '-c', is_flag=True, default=True, required=True, help='Use clipboard for input')
@click.option('--input-path', '-i', required=False, help='Path to the input directory')
# add an option for the pdf theme/style
@click.option('--theme', '-t', required=False, default='MRL', help='Theme for the pdf')

def main(use_clipboard_for_input, input_path, theme):
    if use_clipboard_for_input:
        input_path = pyperclip.paste()
    
    # obtain the latex code
    latex_paths = generate_latex_files(input_path, theme)    
    
    # compile the latex code to a pdf
    compile_pdfs(latex_paths)

if __name__ == '__main__':
    main()