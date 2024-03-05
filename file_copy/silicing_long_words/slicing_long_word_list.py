def slice_long_words_list(text):
    for word in text:
        if len(word) > 100:
            index = text.index(word)
            text[index] = word[:100]
        else:
            text = text
    return text