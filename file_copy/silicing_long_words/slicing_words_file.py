def slice_words(text):
    if len(text) > 250:
        text = text[:250]
    else:
        text = ''
    return text

def slice_content_words(text):
    if len(text) > 250:
        text = text[:250]
    else:
        text = text
    return text