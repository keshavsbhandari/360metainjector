

import os
import sys

try:
    from Tkinter import *
except ImportError:
    print("Tkinter library is not available.")

path = os.path.dirname(sys.modules[__name__].__file__)
path = os.path.join(path, '..')
sys.path.insert(0, path)


import metadata_utils
import mpeg
class Console(object):
    def __init__(self):
        self.log = []

    def append(self, text):
        print(text.encode('utf-8'))
        self.log.append(text)




pth = "/home/keshav/Desktop/egokData/EgoK360_Data/Desk_work/Desk_work/egok360-Desk_work-Desk_work-3609.MP4"

def inject(source, desitnation="w.MP$"):
    with open(source, "rb") as in_fh:
        metadata = metadata_utils.Metadata()
        metadata.video = metadata_utils.generate_spherical_xml(stereo=None)
        metadata.audio = metadata_utils.SPATIAL_AUDIO_DEFAULT_METADATA
        metadata_utils.inject_metadata(
            source, desitnation, metadata, Console().append)

if __name__ == "__main__":
    inject(pth,'voodo.MP4')