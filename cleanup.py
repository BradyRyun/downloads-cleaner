import os
import shutil
import glob

CWD = os.getcwd()
IMAGES_DIR = os.path.join(CWD, 'images')
VIDEOS_DIR = os.path.join(CWD, 'videos')
SPREADSHEETS_DIR = os.path.join(CWD, 'spreadsheets')
EBOOKS_DIR = os.path.join(CWD, 'Ebooks')
SCRIPTS_DIR = os.path.join(CWD, 'scripts')
VPN_DIR = os.path.join(CWD, 'vpn')
MIDI_DIR= os.path.join(CWD, 'midi')
DOCUMENTS_DIR = os.path.join(CWD, 'documents')

def make_directories():
    os.makedirs(IMAGES_DIR, exist_ok=True)
    os.makedirs(VIDEOS_DIR, exist_ok=True)
    os.makedirs(SPREADSHEETS_DIR, exist_ok=True)
    os.makedirs(EBOOKS_DIR, exist_ok=True)
    os.makedirs(SCRIPTS_DIR, exist_ok=True)
    os.makedirs(VPN_DIR, exist_ok=True)
    os.makedirs(MIDI_DIR, exist_ok=True)
    os.makedirs(DOCUMENTS_DIR, exist_ok=True)

def delete_files(file_extension): 
    files = glob.glob(f'*{file_extension}')
    if not files:
        print(f"No {file_extension} files found")
    else:
        for file in files:
            print(f"Deleting {file}")
            os.remove(file)
    
def move_files(file_extension, file_location):
    files = glob.glob(f'*{file_extension}')
    if not files:
        print(f"No {file_extension} files found")
    else:
        for file in files:
            print(f"Moving {file} to {file_location}/{file}")
            shutil.move(file, os.path.join(file_location, file))

def move_image_files():
    move_files('.jpg', IMAGES_DIR)
    move_files('.jpeg', IMAGES_DIR)
    move_files('.png', IMAGES_DIR)
    move_files('.gif', IMAGES_DIR)

def move_video_files():
    move_files('.mp4', VIDEOS_DIR)
    move_files('.mov', VIDEOS_DIR)
    move_files('.avi', VIDEOS_DIR)

def move_spreadsheet_files():
    move_files('.xlsx', SPREADSHEETS_DIR)
    move_files('.xls', SPREADSHEETS_DIR)
    move_files('.csv', SPREADSHEETS_DIR)

def move_ebook_files():
    move_files('.epub', EBOOKS_DIR)
    move_files('.mobi', EBOOKS_DIR)

def move_script_files():
    move_files('.sh', SCRIPTS_DIR)

def move_vpn_files():
    move_files('.ovpn', VPN_DIR)

def move_midi_files():
    move_files('.mid', MIDI_DIR)

def move_document_files():
    move_files('.docx', DOCUMENTS_DIR)
    move_files('.doc', DOCUMENTS_DIR)
    move_files('.pdf', DOCUMENTS_DIR)

def move_all():
    move_image_files()
    move_video_files()
    move_spreadsheet_files()
    move_ebook_files()
    move_script_files()
    move_vpn_files()
    move_midi_files()
    move_document_files()

def main():
    delete_files("dmg")
    delete_files("pkg")
    delete_files("zip")
    delete_files("ics")
    delete_files("webp")
    delete_files("html")
    make_directories()
    move_all()

if __name__ == '__main__':
    main()
