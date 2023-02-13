# Input: text
# Find duplicate words
# output: Top K duplicate words based on frequency

def topK(s, k):
    list_words = s.split(" ")
    set_words = set(list_words)
    words_dict = dict((w, 0) for w in set_words)
    for w in list_words:
        words_dict[w] += 1
    frequency_dict = dict((f, []) for f in set(words_dict.values()))
    for w in words_dict:
        frequency_dict[words_dict[w]] += [w]
    freqs = sorted(frequency_dict.keys(), reverse=True)
    words = []
    for i in freqs:
        words += frequency_dict[i]
        if len(words) >= k:
            return words[:k]
    return words


input = "hello hello world random text hello text world world world"

print(topK(input, 3))
