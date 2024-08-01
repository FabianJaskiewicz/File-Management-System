import os

#Note it's possible for mp4 files to be audio only and this program doesn't check for that

path_downloads = r"C:\Users\fabian\Downloads"
path_videos = r"C:\Users\fabian\Videos"
path_pictures = r"C:\Users\fabian\Pictures"
path_music = r"C:\Users\fabian\Music"
path_documents = r"C:\Users\fabian\Documents"
videos = pictures = text_documents = music = 0

video_extensions = ['.mp4', '.mov']
image_extensions = ['.jpg', '.png']
music_extensions = ['.mp3', '.wav', '.m4a', '.flac', 'wma']
text_document_extensions = ['.txt', '.docx', '.pdf', 'xlsx']


def move(name, extension):
    source = path_downloads + "\\" + name

    if extension in video_extensions:
        destination = path_videos + "\\" + name
        if not os.path.exists(destination):
            os.rename(source, destination)
            return 'v'
    elif extension in text_document_extensions:
        destination = path_documents + "\\" + name
        if not os.path.exists(destination):
            os.rename(source, destination)
            return 't'
    elif extension in image_extensions:
        destination = path_pictures + "\\" + name
        if not os.path.exists(destination):
            os.rename(source, destination)
            return 'm'
    elif extension in music_extensions:
        destination = path_music + "\\" + name
        if not os.path.exists(destination):
            os.rename(source, destination)
            return 'm'


for f in os.listdir(path_downloads):
    name, extension = os.path.splitext(f)

    if move(f, extension) == 't':
        text_documents += 1
    elif move(f, extension) == 'p':
        pictures += 1
    elif move(f, extension) == 'v':
        videos += 1
    elif move(f, extension) == 'm':
        music += 1

print(str(text_documents) + " Text document file(s) moved")
print(str(pictures) + " Image file(s) moved")
print(str(videos) + " Video file(s) moved")
print(str(music) + " Music files(s) moved")
