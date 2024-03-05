def slice_words(text):
    if len(text) > 36:
        text = text[:36]
    else:
        text = ''
    return text