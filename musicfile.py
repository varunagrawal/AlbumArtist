from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error

class MusicFile(MP3):
    def __init__(self, path):
        self.file = MP3(path, ID3=ID3)

    def getArtist(self):
        return self.file['TPE1']

    def getSong(self):
        return self.file['TIT2']

    def getAlbum(self):
        return self.file['TALB']

    def setAlbumArt(self, imagefile):
        ext = imagefile.split('.')[-1]
        if ext == 'png': mimetype = 'image/png'
        elif ext == 'jpeg': mimetype = 'image/jpeg'

        try:
            self.file.add_tags()
        except err:
            pass

        try:

            self.file.tags.add(
                APIC(
                    encoding=3, # 3 is for utf-8
                    mime=mimetype, # image/jpeg or image/png
                    type=3, # 3 is for the cover image
                    desc=u'Cover',
                    data=open(imagefile).read()
                )
            )
            self.file.save()

        except error:
            print("Error setting album art")


if __name__ == "__main__":
    musicdir = "/Users/varun/Music/"
    music = get_all_music_files(musicdir)
    
    print(music[0])

    mp3_file = MusicFile(music[0])
    mp3_file.getArtist()
