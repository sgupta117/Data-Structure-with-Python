def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    longest = 0
    substring_map = {}
    start = 0
    for i in range(len(s)):
        position = substring_map.get(s[i])
        if position is not None and position >= start:
            length = i - start
            start = position + 1
            longest = max(length, longest)
        substring_map[s[i]] = i
    longest = max(len(s) - start, longest)
    return longest

def lengthOfLongestSubstring1(s):
    result = list()
    best = list()
    if len(s) == 1:
        return 1
    for num, i in enumerate(s):
        if i in result:
            index = result.index(i)
            result = result[index + 1:]

        result.append(i)
        if len(best) < len(result):
            best = list(result)
    return len(best)

def main():
    lengthOfLongestSubstring('abcabcbb')
    lengthOfLongestSubstring1('pwwkew')

main()