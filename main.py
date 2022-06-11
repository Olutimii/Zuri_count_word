# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open(filename) as f:
        output = f.readlines()
    return output

def count_words():
    text = read_file_content("./story.txt")
    count = {}
    for line in text:
        for word in line.split():
            count[word] = 1 + count.get(word, 0)

    return count
print(count_words())