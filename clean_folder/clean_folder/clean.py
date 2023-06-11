import os
import sys
from pathlib import Path
#import shutil
import zipfile
import uuid 

CATEGORIES = {'Images' : ['.jpeg', '.png', '.jpg', '.svg'], 
              'Video' : ['.avi', '.mp4', '.mov', '.mkv', '.wmv'],
              'Documents' : ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'],
              'Music': ['.mp3', '.ogg', '.wav', '.amr'],
              'Archives' : ['.zip', '.gz', '.tar'],
              'Unkknown' : []} 


#all_extentions_tmp = images_tmp + video_tmp + documents_tmp + music_tmp + archives_tmp
#all_extentions = set()




CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

#creation of dictionary for trancliteration
TRANS = {} 

for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

def normalize(text):
    text = text.translate(TRANS)
    for chr in text:
        if ord(chr) in range(48,58):# (0-9)
            continue
        elif ord(chr) in range(65,91):#(A-Z)
            continue
        elif ord(chr) in range(97,123):#(a-z)
            continue
        else:
            text = text.replace(chr, "_")
    return text


# def delete_empty_folders(path: Path) -> None:
#     for item in path.glob('**/*'):
#         #if item.is_dir() and not any(item.iterdir()):
#         if item.is_dir() and len(item) == 0:
#             item.rmdir() 


def delete_empty_folders(path):
    for root, dirs, files in os.walk(path, topdown=False):
        # os.walk iterates over all the files and directories in a directory tree recursively.

        for folder in dirs:
            folder_path = os.path.join(root, folder)
        
            if not os.listdir(folder_path):  # Check if folder is empty
                os.rmdir(folder_path)


def move_file(file: Path, root_dir: Path, category: str) -> None:

    target_dir = root_dir.joinpath(category)

    if not target_dir.exists():
        target_dir.mkdir()

    new_file_name = target_dir.joinpath(f'{normalize(file.stem)}{file.suffix}')
    # file.stem -file nam/ fil.suffix - file extention

    if new_file_name.exists():
       new_file_name = new_file_name.with_name(f"{new_file_name.stem}-{uuid.uuid4()}{file.suffix}")
       # uuid.uuid4() is a function from the uuid module used to generate a random UUID (Universally Unique Identifier)

    file.rename(new_file_name)    


def get_categories(file: Path) -> str:
    ext = file.suffix.lower()# 'file.suffix ' is an attribute of a Path object from the pathlib module (represents the file extension)
    for cat, exts in CATEGORIES.items():
        if ext in exts:
            return cat
    cat = 'Unknown'
    return cat


def sort_folder(path: Path) -> None:
    for item in path.glob('**/*'):# 'glob('**/*')' searches for all files and directories recursively
        #print(item)
        if item.is_file():# item.is_file() is a method of pathlib 
            category = get_categories(item)
            move_file(item, path, category)
    delete_empty_folders(path)
    print_lists(path)
    #unzip_archives(path)


def unzip_archives(path: Path) -> None:

    path_archives = os.path.join(path,'Archives')

    if os.path.exists(path_archives):

        for i in os.listdir(path_archives):
            file_extension = list (os.path.splitext(i))
            folder_name = file_extension[0]
        
            extraction_path = os.path.join(path_archives, folder_name)

            if not os.path.exists(extraction_path):
                os.makedirs(extraction_path)

            with zipfile.ZipFile(os.path.join(path_archives, i), 'r') as zip_ref:
                zip_ref.extractall(extraction_path)


def print_lists(path: Path)-> list:

    # Get a list of files in the directory and its subdirectories
    file_list = list(path.glob('**/*'))  # Using glob with '**/*' matches files recursively

    # Filter the list to include only files (excluding directories)
    file_list = [file for file in file_list if file.is_file()]

    # Print the file paths
    for file in file_list:
        print(file)
    

# get_pathes_create_folsers()
# sort_folder(path)
# delete_empty_folders(path)
# unzip_archivez(path_archives)
# print_lists()
def main():
    try:
        # sys.argv returns list comprising two strings: ['location of the .py file', 'location of the folder to scan']
        path = Path(sys.argv[1]) #Path - fanction from pathlib. it is allow to copy path form the explorer withot '//'
    except IndexError:
        return print ('There is no path to folder! Enter path!')
   
    if not path.exists():
        return print (f'The path <<< {path} >>> doesn\'t exist! Enter valid path!')
    sort_folder(path)
    return "Folder sorting completed successfully"
    

if __name__ == '__main__':
    print(main())

#Path to test:  python clean_folder\clean_folder\clean.py D:\VSCode_projects\Unsorted_hw6_main
#Path to test:  python clean_folder\clean_folder\clean.py D:\VSCode_projects\Unsorted_hw6_main_repeat