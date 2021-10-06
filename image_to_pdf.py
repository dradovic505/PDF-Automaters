#ARGUMENTS: absolute path of folder from which you want the images converted to PDFs
#               OR
#           absolute paths of images the user wishes to convert to PDFs
#OUTPUT:    PDFs of the images that could be processed

import os, sys, pdf_utils
from PIL import Image
from Context import Context

files = []

def convert_to_pdf():
    for i in range(len(files)):
        file_name = files[i]
        if (file_name.find(".DS_Store") == -1):
            try:
                jpg_image = Image.open(file_name)
            except Image.UnidentifiedImageError:
                print("Skipped " + file_name + " as it is not a supported file type.")
            
            jpg_image_converted = jpg_image.convert('RGB')
            jpg_image_converted.save(file_name.split(".")[0] + ".pdf", "PDF")

def main():
    file_or_directory = sys.argv[1]
    
    if not file_or_directory.endswith('/'):
        file_or_directory = file_or_directory + '/'
    
    extension_position = file_or_directory.find('.')

    # if first arg is a path, convert all images to PDFs in the top-level folder
    if extension_position == -1:   #if path
        pdf_utils.populate_files_for_path_arg(file_or_directory, files, Context.IMAGE_TO_PDF)
    # if first arg is not a path, assume the args are images
    else:
        pdf_utils.populate_files_for_file_arg(files)
    
    convert_to_pdf()

if __name__ == '__main__':
    main()