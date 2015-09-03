def pattern_count(text, pattern):
    """
    >>> pattern_count("CGATATATCCATAG", "ATA")
    3
    """
    count = 0
    for i in range(0, (len(text) - len(pattern))):
        if text[i:i + len(pattern)] == pattern:
            count += 1
    return count


def frequet_words(text, k):
    frequent_patterns = set()
    count = [0 for _ in range(len(text))]
    for i in range(0, len(text) - k):
        pattern = text[i:i+k]
        count[i] = pattern_count(text, pattern)
    max_count = max(count)
    for i in range(0, len(text) - k):
        if count[i] == max_count:
            frequent_patterns.add(text[i:i+k])
    return frequent_patterns



if __name__ == '__main__':
    print (pattern_count("CGATATATCCATAG", "ATA"))
    print(frequet_words("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4))