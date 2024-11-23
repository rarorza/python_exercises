class Solution:
    def reverseWords(self, s: str):
        new_string = ""
        l, r = 0, 0
        while r < len(s):
            if s[r] != " ":
                if r == len(s) - 1:
                    new_string += "".join(s[l : r + 1][::-1])
                    return new_string
                r += 1
            else:
                new_string += "".join(s[l:r][::-1] + " ")
                r += 1
                l = r


s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))
