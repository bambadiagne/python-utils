from getpass import getuser
# import locale
CURRENT_USER=getuser()
ROOT_DIRECTORY=f"C:\\Users\\{CURRENT_USER}\\"
ALL_AUDIO_EXTENSION=['AAC', 'AIFF', 'DSD', 'FLAC', 'MP3', 'MQA', 'OGG', 'WAV', 'WMA']
ALL_VIDEOS_EXTENSION=['WEBM MPG', 'MP2', 'MPEG', 'MPE', 'MPV', 'OGG', 'MP4', 'M4P', 'M4V', 'AVI', 'WMV', 'MOV', 'QT', 'FLV', 'SWF', 'AVCHD']
ALL_IMAGES_EXTENSION=['JPG', 'PNG', 'GIF', 'WEBP', 'TIFF', 'PSD', 'RAW', 'BMP', 'HEIF', 'INDD', 'JPEG']
AUDIO_PATH=f"{ROOT_DIRECTORY}Music"
IMAGES_PATH=f"{ROOT_DIRECTORY}Pictures"
VIDEOS_PATH=f"{ROOT_DIRECTORY}Videos"
# AUDIO_PATH=''
# IMAGES_PATH=''
# VIDEOS_PATH=''
# if(locale.getdefaultlocale()[0]=="fr_FR"):
#     AUDIO_PATH=f"{ROOT_DIRECTORY}Musique"
#     IMAGES_PATH=f"{ROOT_DIRECTORY}Images"
#     VIDEOS_PATH=f"{ROOT_DIRECTORY}Vidéos"
# else:

def get_file_type(file_extension):
    if(file_extension in ALL_AUDIO_EXTENSION):
        return ALL_AUDIO_EXTENSION      
    if(file_extension in ALL_IMAGES_EXTENSION):
        return ALL_IMAGES_EXTENSION    
    if(file_extension in ALL_VIDEOS_EXTENSION):
        return ALL_VIDEOS_EXTENSION    