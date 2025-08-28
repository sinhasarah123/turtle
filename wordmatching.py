def match_words(words):
    matched_words = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            matched_words.append(word)
    print("list of words that have the same first and last character:", matched_words)
    return len(matched_words)

count = match_words(['abc', 'xyz', 'aba', '1221'])
print("number of word having the same first and last letter:", count)