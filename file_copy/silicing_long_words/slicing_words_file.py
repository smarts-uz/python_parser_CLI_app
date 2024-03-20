import time


def slice_words(text,destination_file_path):
    if len(text) > len(destination_file_path):
        return True
    else:
        return False

def slice_content_words(text):
    if len(text) > 250:
        text = text[:250]
    else:
        text = text
    return text