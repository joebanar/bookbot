file_contents = ""

def get_file_contents(f):
    with open(f) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(file_contents):
    words = file_contents.split()
    return words

def get_character_count(file_contents):
    counts = {}
    file_contents_lowered = file_contents.lower()
    for char in file_contents_lowered:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts 

def sort_by_count(counts):
    items = list(counts.items())
    items.sort(key=lambda item: item[1], reverse=True)
    return dict(items)