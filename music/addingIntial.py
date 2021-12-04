from .models import Song
from tinytag import TinyTag
import os

import re

music_dir = r"C:\Users\Aykdk\Music\Playlists"
img_dir = r"C:\Users\Aykdk\Pictures\AlbumArt"


for files in os.listdir(music_dir):
    print(files.endswith('.mp3'))
    if files.endswith('.mp3'):
        print(os.path.join(music_dir,files))
        mpf = TinyTag.get(os.path.join(music_dir,files),image=True)
        print(mpf)
        image_data = mpf.get_image()
        # print(os.path.join(img_dir,files))
        # print(os.path.join(img_dir,mpf.album + '.jpg'))
        pattern = re.compile(r'([<>*"/?|:\\])')
        album = pattern.sub(r'',str(files.replace('.mp3','')))
        img_path = os.path.join(img_dir, album+ '.jpg')
        if not os.path.exists(img_path):
            with open(os.path.join(img_dir,img_path),'wb') as saveimg:
                print(os.path.join(img_dir, img_path))
                saveimg.write(image_data)











