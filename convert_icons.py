import json
import os.path
import collections
import itertools
from PIL import Image
import shutil

def run(f):
    f()
    return f

def iter_folder(folder):
    for file in os.listdir(folder):
        file = os.path.join(folder, file)
        data = open(file, "rb").read().decode("utf8")

        yield json.loads(data)


@run
def convert():
    for folder in os.listdir("."):
        if not os.path.isdir(folder):
            continue
            
        infolder = os.path.join(folder, "Texture2D")

        for image in os.listdir(infolder):
            img = Image.open(os.path.join(infolder, image))
            img.save(os.path.join(folder, os.path.splitext(image)[0] + ".jpg"), "JPEG")

        shutil.rmtree(infolder)
