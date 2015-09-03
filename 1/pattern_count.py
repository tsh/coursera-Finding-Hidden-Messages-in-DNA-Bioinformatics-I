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


if __name__ == '__main__':
    print (pattern_count("CGATATATCCATAG", "ATA"))