
import ntpath
import os
import sys
import tkFileDialog
import tkMessageBox
import traceback

try:
    from Tkinter import *
except ImportError:
    print("Tkinter library is not available.")
    exit(0)

path = os.path.dirname(sys.modules[__name__].__file__)
path = os.path.join(path, '..')
sys.path.insert(0, path)


from spatialmedia import metadata_utils
from spatialmedia import mpeg
class Console(object):
    def __init__(self):
        self.log = []

    def append(self, text):
        print(text.encode('utf-8'))
        self.log.append(text)




pth = "/Users/keshav/Desktop/egok-data-collector/spatial-media-2.0/spatialmedia/a.MP4"

def inject(source, desitnation="w.MP$"):
    with open(source, "rb") as in_fh:
        metadata = metadata_utils.Metadata()
        metadata.video = metadata_utils.generate_spherical_xml(stereo=None)
        metadata.audio = metadata_utils.SPATIAL_AUDIO_DEFAULT_METADATA
        metadata_utils.inject_metadata(
            source, desitnation, metadata, Console().append)

if __name__ == "__main__":
    inject(pth,'voodo.MP4')