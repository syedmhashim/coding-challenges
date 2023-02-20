def topK(s, K):
    char2count = dict()
    for c in s:
        if c in char2count:
            char2count[c] += 1
        else:
            char2count[c] = 1
    count2chars = dict()
    for v in char2count:
        k = char2count[v]
        if k in count2chars:
            count2chars[k] = count2chars[k] + [v]
        else:
            count2chars[k] = [v]
    counters = list(count2chars.keys())
    counters.sort(reverse=True)
    topK = []
    for count in counters:
        if len(topK) >= K:
            return topK[:K]
        topK = topK + count2chars[count]
    return topK[:K]

if __name__ == "__main__":
    k = 3
    test_cases = [
        "aabreijkje121a",
        "aabbcccdddd"
    ]
    print(f"K: {k}")
    for i in range(len(test_cases)):
        print("Test case:")
        print(test_cases[i])
        
        print("Result:")
        print(topK(test_cases[i], k))
