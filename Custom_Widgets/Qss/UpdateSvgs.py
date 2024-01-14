import os
import codecs
import re

def getAllFolders(base_folder):
    all_folders = []
    for root, dirs, files in os.walk(base_folder):
        for dir_name in dirs:
            folder_path = os.path.relpath(os.path.join(root, dir_name), base_folder)
            all_folders.append(folder_path)
    return all_folders

def update_svg_files(directory):
    # Get a list of all SVG files in the directory and its subdirectories
    svg_files = [os.path.join(root, file) for root, dirs, files in os.walk(directory) for file in files if file.endswith(".svg")]

    # Iterate over each SVG file and update the fill attribute to have white color
    for svg_file in svg_files:
        try:
            with codecs.open(svg_file, encoding='utf-8', errors='ignore') as f:
                content = f.read()

                # Update fill attribute to have white color without the extra "/"
                new_svg = re.sub(r' fill\s*=\s*"[^"]*"</path>>', ' fill="#ffffff"></path>', content, flags=re.IGNORECASE)

            with codecs.open(svg_file, 'w', encoding='utf-8') as f:
                f.write(new_svg)

            print(f"Updated: {svg_file}")

        except Exception as e:
            print(f"Error processing {svg_file}: {e}")

# Specify the path to the folder containing SVG files
directory_path = "icons/font_awesome/"

# Call the function to get all subdirectories
subdirectories = getAllFolders(directory_path)

# Iterate through each subdirectory and update SVG files
for subdirectory in subdirectories:
    update_svg_files(os.path.join(directory_path, subdirectory))
