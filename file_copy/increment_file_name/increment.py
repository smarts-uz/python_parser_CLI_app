import os
import re


def get_incremented_filename(filename):
    name, ext = os.path.splitext(filename)
    seq = 0
    # continue from existing sequence number if any
    rex = re.search(r"^(.*)-(\d+)$", name)
    if rex:
        name = rex[1]
        seq = int(rex[2])

    while os.path.exists(filename):
        seq += 1
        filename = f"{name}-{seq}{ext}"
    return filename


a = get_incremented_filename("D:/SmartTech Learning/____\\component.mp4")
# a = get_incremented_filename("'D:/SmartTech Learning/____\\component1.mp4'")
print(a)