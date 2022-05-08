import os
print("========================BIENVENUE DANS LE CLASSEUR DE FICHIERS=================================")
from folders_path import *
files = [file for file in os.listdir() if(not os.path.isdir(file))]
file_to_jump = os.path.basename(__file__)
exe_escape_file, exe_extension = os.path.splitext(file_to_jump)

if(os.path.isfile(exe_escape_file+'.exe')):
    files.remove(exe_escape_file+'.exe')
if(os.path.isfile(file_to_jump)):
    files.remove(file_to_jump)
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
        file_destination = get_file_type(file_extension[1:].upper())
        if(file_destination):        
            print("Deplacement du fichier {0} vers Fichiers {1} ".format(
            file,file_destination))
            os.replace(file, "{0}/{1} ".format(file_destination, file))
  
    else:
        print("Deplacement du fichier {0} vers Fichiers {1} ".format(
            file, file_extension[1:]))
        os.replace(file, "Fichiers sans extension/{0} ".format(file))
quit__ = input("Appuyer sur Entrée pour quitter")
