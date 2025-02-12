def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = get_word_count(text)
    num_char = get_num_char(text)
    report = get_report(text, book_path)
    #print(text)
    #print(f"There are {num_words} words in this document")
    #print(num_char)
    print(report)
    
def get_text(path):    
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)
    
def get_num_char(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else: 
            chars[lowered] = 1
    return chars

def get_report(text, path):
    report_string = "--- Begin report of " + path + " ---\n" + str(get_word_count(text)) + " words found in the document\n\n"
    num_char = get_num_char(text)
    for n in num_char:
        if n.isalpha() == True:
            report_string = report_string + "The '" + n + "' character was found " + str(num_char[n]) + " times\n"
    report_string = report_string + "--- End report ---"    
    return report_string

main()