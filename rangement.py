import os
files = [file for file in os.listdir() if(not os.path.isdir(file))]
file_to_jump=os.path.basename(__file__)
files.remove(file_to_jump)
files.remove(os.path.splitext(file_to_jump)[0]+'.exe')
print(files)
files_extension = []
for file in files:
    filename, file_extension = os.path.splitext(file)
    if(file_extension):
        files_extension.append(file_extension[1:])
    else:
        files_extension.append("sans extension")
files_extension = set(files_extension)
for extension in files_extension:
    directory_name = f"Fichiers {extension}"
    if(not os.path.exists(directory_name)):
        os.mkdir(directory_name)
for file in files:

    filename, file_extension = os.path.splitext(file)
    if(file_extension):
        os.replace(file, "Fichiers {0}/{1} ".format(file_extension[1:], file))
    else:
        os.replace(file, "Fichiers sans extension/{0} ".format(file))
