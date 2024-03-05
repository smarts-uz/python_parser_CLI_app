

def slicing_long_word_url(text):
    if len(text) > 100:
        text = text[:100]
    else:
        text = text
    return text