import time


def slice_words(text,destination_file_path):
    print(len(text), text)
    print(len(destination_file_path), destination_file_path)
    time.sleep(5)
    if len(text) > len(destination_file_path):
        print(len(text), text)
        print(len(destination_file_path), destination_file_path)
        time.sleep(2)
        return True
    else:
        return False

def slice_content_words(text):
    if len(text) > 250:
        text = text[:250]
    else:
        text = text
    return text