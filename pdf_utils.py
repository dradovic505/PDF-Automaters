import os, sys
from PIL import Image
from Context import Context

def populate_files_for_path_arg(name, files, context):
    if os.path.exists(name) == False:
        print("Invalid path. Need to enter an absolute path")
        sys.exit()

    for filename in os.listdir(name):
        if context == Context.COMBINE_PDFS and filename.endswith('.pdf'):
            files.append(name + filename)
        elif context == Context.IMAGE_TO_PDF:
            files.append(name + filename)
    
    if context == Context.COMBINE_PDFS:
        files.sort(key=str.lower)

def populate_files_for_file_arg(files):
    num_files = len(sys.argv) - 1
    for i in range(num_files):
        files.append(sys.argv[i + 1])