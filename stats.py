def word_number(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        word_count = len(file_contents.split())
        return word_count