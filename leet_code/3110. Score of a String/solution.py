class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = list(s)
        total = 0
        for i, char in enumerate(chars):
            if i + 1 <= len(chars) - 1:
                total += abs(ord(char) - ord(chars[i + 1]))
        return total


if __name__ == "__main__":
    start = Solution().scoreOfString("hello")
    print(start)
