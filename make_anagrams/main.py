def remove_uncommon_chars(s, intersection, deletion):
    for chr in s:
        if chr not in intersection:
            deletion += 1
    return deletion

def calculate_char_frequency(a):
    char_frequency_dict = dict((i,0) for i in set(a))
    for chr in a:
        char_frequency_dict[chr] = char_frequency_dict[chr] + 1
    return char_frequency_dict

def make_anagrams(a, b):
    total_deletion = 0
    a_b_intersection =set(a).intersection(set(b))

    char_frequency_a = calculate_char_frequency(a)
    char_frequency_b = calculate_char_frequency(b)
     
    total_deletion = remove_uncommon_chars(a, a_b_intersection, total_deletion)
    total_deletion = remove_uncommon_chars(b, a_b_intersection, total_deletion)

    for chr in a_b_intersection:
        total_deletion += abs(char_frequency_a[chr] - char_frequency_b[chr])
    return total_deletion


if __name__ == "__main__":
    a = 'cdeca'
    b = 'abcd'
    out = make_anagrams(a,b)
    print(out)
