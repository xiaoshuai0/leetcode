class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        map, length, start = {}, 0, 0
        for (index, char) in enumerate(s):
            if char in map:
                start = max(start, map[char] + 1)
            length = max(length, index - start + 1)
            map[char] = index
        return length



if __name__ == '__main__':
    # print(Solution().lengthOfLongestSubstring("abcabcbb"))
    # print(Solution().lengthOfLongestSubstring("bbbb"))
    print(Solution().lengthOfLongestSubstring("pwwkew"))
    # print(Solution().lengthOfLongestSubstring(""))